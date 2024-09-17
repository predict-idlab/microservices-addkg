"""
levels.py file.
Defines all required functions to handle numerical data during the transformation to the binary INK representation.
"""
from tqdm import tqdm

__author__ = 'Bram Steenwinckel'
__copyright__ = 'Copyright 2020, INK'
__credits__ = ['Filip De Turck, Femke Ongenae']
__license__ = 'IMEC License'
__version__ = '0.1.0'
__maintainer__ = 'Bram Steenwinckel'
__email__ = 'bram.steenwinckel@ugent.be'


def check_float(lvl, mapping):
    """
    Function to check whether all values within a list contains only float values

    :param lvl: List of possible numerical values.
    :type lvl: str
    :return: True when all values of the given list are numerical.
    :rtype: bool
    """
    try:
        [float(mapping[x]) for x in lvl]
    except ValueError as e:
        return False
    return True


def create_levels(dct, dct_t, orig_levels={}, mapping=None, verbose=True):
    """
    Function which create the level columns from the numerical data.
    By using this function, additional features comparing numerical data with each other are added in the node's
    neighborhoods. These are later transformed into a binary representation.

    :param dct: Neighborhood dictionary from which numerical levels are added.
    :type dct: dict
    :param dct_t: Neighborhood dictionary from previously fitted neighborhoods (dct and dct_t are equal during the
                  fit_transform function, but different when using the transform function).
    :type dct_t: dict
    :param verbose: Parameter to show tqdm tracker (default False).
    :type verbose: bool
    :return: Original neighborhood with additional level-based information.
    :rtype: dict
    """
    if verbose:
        print('## create levels')
    level_counts = {}
    black_list = set()
    n_mapping = {}
    for tup in tqdm(dct, disable=not verbose):
        for key in tup[1]:
            if check_float(tup[1][key], mapping):
                if key not in level_counts:
                    level_counts[key] = set()
                level_counts[key].update(tup[1][key])
            else:
                black_list.add(key)

    for o in orig_levels:
        added = False
        for l in level_counts:
            if mapping[o] == mapping[l]:
                level_counts[l].update(orig_levels[o])
                added = True
                break
        if not added:
            level_counts[o] = orig_levels[o]
    #print([mapping[x] for x in level_counts])

    n_dct = []
    for tup in tqdm(dct_t, disable=not verbose):
        n_levels = {}
        for key in tup[1]:
            if key in level_counts and key not in black_list:
                for lvl in level_counts[key]:
                    try:
                        n_mapping[hash(mapping[key] + '<=' + str(mapping[lvl]))] = mapping[key] + '<=' + str(mapping[lvl])
                        n_levels[hash(mapping[key] + '<=' + str(mapping[lvl]))] = any(float(mapping[x]) <= float(mapping[lvl]) for x in tup[1][key] if mapping[x] != '')
                        n_mapping[hash(mapping[key] + '>=' + str(mapping[lvl]))] = mapping[key] + '>=' + str(mapping[lvl])
                        n_levels[hash(mapping[key] + '>=' + str(mapping[lvl]))] = any(float(mapping[x]) >= float(mapping[lvl]) for x in tup[1][key] if mapping[x] != '')
                    except Exception as exp:
                        print(exp)
                        continue

        n_levels.update(tup[1])
        n_dct.append((tup[0], n_levels))
    return n_dct, n_mapping, level_counts
