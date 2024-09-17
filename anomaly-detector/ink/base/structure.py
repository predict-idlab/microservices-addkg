"""
structure.py file.
Defines the functions and classes to construct the binary INK representation.
"""

import numpy as np
from ink.base.graph import KnowledgeGraph
from ink.base.transform.counts import create_counts
from ink.base.transform.levels import create_levels
from ink.base.transform.binarize import create_representation
from tqdm import tqdm

__author__ = 'Bram Steenwinckel'
__copyright__ = 'Copyright 2020, INK'
__credits__ = ['Filip De Turck, Femke Ongenae']
__license__ = 'IMEC License'
__version__ = '0.1.0'
__maintainer__ = 'Bram Steenwinckel'
__email__ = 'bram.steenwinckel@ugent.be'


class InkExtractor:
    """
    The INK extractor.
    Constructs the binary representation from a given knowledge graph.

    :param connector: Connector instance.
    :type connector: :py:class:`ink.base.connectors.AbstractConnector`
    :param prefixes: Optional dictionary of prefixes which should be mapped.
    :type prefixes: list
    :param verbose: Parameter to show tqdm tracker (default False).
    :type verbose: bool
    """
    def __init__(self, connector, prefixes=None, extract_inverse=False, verbose=False):
        if prefixes is None:
            prefixes = []
        self.connector = connector
        self.kg = KnowledgeGraph(connector, prefixes, extract_inverse)
        self.levels = {}
        self.verbose = verbose
        self.train_data = None

    def _acquire_set(self, val):
        v_set = list()
        if isinstance(val, str):
            res = self.connector.query(val)
            for s in res:
                v_set.append(s['s']['value'])
        else:
            if val is not None and not isinstance(val, list) and not isinstance(val, set):
                with open(val) as file:
                    v_set = ['<' + r.rstrip("\n") + '>' for r in file.readlines()]
            else:
                try:
                    v_set = list(val)
                except Exception as e:
                    print(e)
        return v_set

    def create_dataset(self, depth=4, pos=None, neg=None, skip_list=[], anonym_list=[], jobs=1):
        """
        Function to create the neighborhood dataset.
        Based on the input parameters, this function creates the dictionary of neighborhoods.

        The pos parameter is required, the neg is only required when a task specific case is being solved.
        The pos and neg parameters can be either: sets or query strings.
        When a query string is given, the connector which is associated with the InkExtractor will be used to get all
        the nodes of interest.

        :param depth: The maximal depth of the neighborhood
        :type depth: int
        :param pos: Set or query string describing the positive set of nodes of interest.
        :type pos: set, str
        :param neg: Set or query string describing the negative set of nodes of interest (only for task specific cases).
        :type neg: set, str
        :param skip_list: List with relations which are not taken into account when traversing the neighborhoods.
        :type skip_list: list
        :return: The extracted neighborhoods for each node of interest and the corresponding labels (only for task
        specific cases).
        """

        pos_set = self._acquire_set(pos)
        neg_set = self._acquire_set(neg)

        if self.verbose:
            print("#Process: get neighbourhood")


        #####
        data = []

        self.kg.mapping[hash('')] = ''
        for p in pos_set + neg_set:
            self.kg.mapping[hash(p)] = p
            data.append((p, [(hash(''), hash(p))], skip_list, anonym_list))

        #noi_neighbours = self.kg.extract_neighbourhoods(data, verbose=self.verbose, jobs=jobs)
        #print(len(noi_neighbours))


        # data = []
        # for r in noi_neighbours:
        #     for m in r[2]:
        #         self.kg.mapping[m[1]] = m[0]
        #     for p in r[1]:
        #         for o in r[1][p]:
        #             data.append((r[0], [(p,o)], skip_list))
        #
        # noi_neighbours = self.kg.extract_neighbourhoods(data, verbose=self.verbose, jobs=jobs)
        # print(len(noi_neighbours))
        #
        # overall_features = {}
        # for p in noi_neighbours:
        #     if p[0] not in overall_features:
        #         overall_features[p[0]] = {}
        #     for rel in p[1]:
        #         if rel not in overall_features[p[0]]:
        #             overall_features[p[0]][rel] = []
        #         overall_features[p[0]][rel].extend(p[1][rel])
        #     #overall_features[p[0]].update(p[1])
        #     for m in p[2]:
        #         self.kg.mapping[m[1]] = m[0]
        #
        #
        # data = 0
        # for r in overall_features:
        #     if hash('http://example.com/influences.http://example.com/hasWonPrize') in overall_features[r]:
        #         data+=(len(overall_features[r][hash('http://example.com/influences.http://example.com/hasWonPrize')]))
        #
        # print(data)
        # exit(0)
        #
        # ####

        overall_features = {}
        def generate_noi(nois):
            for p in nois:
                if p[0] not in overall_features:
                    overall_features[p[0]] = {}

                for m in p[2]:
                    self.kg.mapping[m[1]] = m[0]

                for k in p[1]:
                    if k not in overall_features[p[0]]:
                        overall_features[p[0]][k] = []
                    overall_features[p[0]][k].extend(p[1][k])
                    for o in p[1][k]:
                         yield (p[0], [(k,o)], skip_list, anonym_list)

        noi_neighbours = self.kg.extract_neighbourhoods(data, verbose=self.verbose, jobs=jobs)
        for d in range(1, depth):
            noi_neighbours = self.kg.extract_neighbourhoods(generate_noi(noi_neighbours),self.verbose, jobs=jobs)
        for p in noi_neighbours:
            if p[0] not in overall_features:
                overall_features[p[0]] = {}
            for rel in p[1]:
                if rel not in overall_features[p[0]]:
                    overall_features[p[0]][rel] = []
                    overall_features[p[0]][rel].extend(p[1][rel])
            for m in p[2]:
                self.kg.mapping[m[1]] = m[0]

        # PREVIOUS CODE
        # overall_features = {}
        # ll_lenght = len(data)
        # noi_neighbours = self.kg.extract_neighbourhoods(data,verbose=self.verbose, jobs=jobs)
        # for d in range(1,depth):
        #     data=[]
        #
        #     counter = {}
        #     for p in tqdm(noi_neighbours, total=ll_lenght):
        #         if p[0] not in overall_features:
        #             overall_features[p[0]] = {}
        #         for rel in p[1]:
        #             if rel not in overall_features[p[0]]:
        #                 overall_features[p[0]][rel] = []
        #             overall_features[p[0]][rel].extend(p[1][rel])
        #         for m in p[2]:
        #             self.kg.mapping[m[1]] = m[0]
        #         for k in p[1]:
        #             for o in p[1][k]:
        #                  #if self.kg.mapping[o].startswith('http'):
        #                  data.append((p[0], [(k,o)], skip_list))
        #     noi_neighbours = self.kg.extract_neighbourhoods(data, verbose=self.verbose, jobs=jobs)
        #     ll_lenght = len(data)
        #
        # for p in tqdm(noi_neighbours, total=ll_lenght):
        #     if p[0] not in overall_features:
        #         overall_features[p[0]] = {}
        #     for rel in p[1]:
        #         if rel not in overall_features[p[0]]:
        #             overall_features[p[0]][rel] = []
        #         overall_features[p[0]][rel].extend(p[1][rel])
        #     for m in p[2]:
        #         self.kg.mapping[m[1]] = m[0]

        all_feats = [(k,overall_features[k]) for k in overall_features]

        all_noi = [n[0] for n in all_feats]

        a = []
        if len(pos_set) > 0 and len(neg_set) > 0:
            for v in all_noi:
                if v in pos_set:
                    a.append(1)
                else:
                    a.append(0)
        else:
            a = None

        return all_feats, np.array(a)

    def fit_transform(self, dct, counts=False, levels=False, float_rpr=False, create_details=True):
        """
        Fit_transform function which transforms the neighborhood of several nodes of interest into
        a binary representation.

        :param dct: Dictionary containing the neighborhoods of multiple nodes of interest. Can be acquired by using the
        create_dataset function.
        :type dct: dict
        :param counts: Boolean indication if the `ink.base.modules.counts.create_counts` function must be used.
        :type counts: bool
        :param levels: Boolean indication if the `ink.base.modules.levels.create_levels` function must be used.
        :return: tuple with sparse feature matrix, list of indices (node of interests), feature names.
        :rtype: tuple
        """
        if self.verbose:
            print('# Transform')
        if counts:
            dct, mapping = create_counts(dct, mapping=self.kg.mapping, verbose=self.verbose)
            self.kg.mapping.update(mapping)

        self.train_data = dct

        if levels:
            dct, mapping, orig_levels = create_levels(dct, dct, mapping=self.kg.mapping, verbose=self.verbose)
            self.orig_levels = orig_levels
            self.kg.mapping.update(mapping)

        cat_df = create_representation(dct, float_rpr=float_rpr, mapping=self.kg.mapping, verbose=self.verbose, create_details=create_details)

        return cat_df

    def transform(self, dct, counts=False, levels=False, float_rpr=False, create_details=True):
        """
        Fit_transform function which transforms the neighborhood of several nodes of interest into
        a binary representation.

        :param dct: Dictionary containing the neighborhoods of multiple nodes of interest. Can be acquired by using the
        create_dataset function.
        :type dct: dict
        :param counts: Boolean indication if the `ink.base.modules.counts.create_counts` function must be used.
        :type counts: bool
        :param levels: Boolean indication if the `ink.base.modules.levels.create_levels` function must be used.
        :return: tuple with sparse feature matrix, list of indices (node of interests), feature names.
        :rtype: tuple
        """
        if self.verbose:
            print('# Transform')
        if counts:
            dct, mapping = create_counts(dct, mapping=self.kg.mapping, verbose=self.verbose)
            self.kg.mapping.update(mapping)

        #self.train_data = dct
        if levels:
            dct, mapping, orig_levels = create_levels(dct, dct, orig_levels=self.orig_levels, mapping=self.kg.mapping, verbose=self.verbose)
            self.kg.mapping.update(mapping)


        # if self.verbose:
        #     print('# Transform')
        # if counts:
        #     dct = create_counts(dct, verbose=self.verbose)
        #
        # self.train_data = dct
        #
        # if levels:
        #     dct = create_levels(dct, dct, verbose=self.verbose)

        cat_df = create_representation(dct, float_rpr=float_rpr, mapping=self.kg.mapping, verbose=self.verbose,
                                       create_details=create_details)

        return cat_df