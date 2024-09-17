from datetime import datetime
from glob import glob
import pandas as pd
from pqdm.processes import pqdm
import pickle
from rdflib import Graph, URIRef
from rdflib.namespace import RDF
from tqdm.contrib.concurrent import process_map
from time import time

from ink.base.connectors import RDFLibConnector
from ink.base.structure import InkExtractor


# Define a function to process a single file
def process_file(file, nodes, depth=3):
    connector = RDFLibConnector(file, dataformat="ttl")
    extractor = InkExtractor(connector, verbose=False)
    X_train, _ = extractor.create_dataset(depth, set(list(nodes)), set(), skip_list=[],
                                          anonym_list=[], jobs=1)

    extracted_data = extractor.fit_transform(X_train, counts=False, levels=False, float_rpr=True)
    data = pd.DataFrame(extracted_data[0], index=extracted_data[1], columns=extracted_data[2])
    data["graph"] = file

    return data


TARGETS = [
    ("https://github.com/predict/deucalion#cluster.local", 3),
    ("https://github.com/predict/deucalion#adservice-6d47d8bb4d", 3),
    ("https://github.com/predict/deucalion#cartservice-58f875656c", 3),
    ("https://github.com/predict/deucalion#checkoutservice-6bf469c9db", 3),
    ("https://github.com/predict/deucalion#currencyservice-77d6b75564", 3),
    ("https://github.com/predict/deucalion#emailservice-5d6f97fbc6", 3),
    ("https://github.com/predict/deucalion#frontend-5b47ffb486", 3),
    ("https://github.com/predict/deucalion#paymentservice-6cb6d8949d", 3),
    ("https://github.com/predict/deucalion#productcatalogservice-7dfcfcbd76", 3),
    ("https://github.com/predict/deucalion#recommendationservice-cc747488", 3),
    ("https://github.com/predict/deucalion#shippingservice-76b95c9c96", 3)
]


def main():
    # Get the list of files using glob
    file_list = list(glob("data/2024-02-13/graphs/*.ttl"))[3450:3451]

    for target, depth in TARGETS:
        # Use the pool to process the files in parallel
        # all_frames = process_map(process_file, file_list, max_workers=10, chunksize=10)
        target_name = target.split("#")[-1].split("-")[0]
        print(target_name)

        args = zip(file_list, len(file_list) * [[target]], len(file_list) * [depth])
        frames = pqdm(args, process_file, n_jobs=10, argument_type="args")
        # all_frames = pqdm(file_list, process_file, n_jobs=10)
        print(frames[0].shape)

        with open(f"data/heroic_{depth}_{target_name}-framesdd.pickle", "wb") as f:
            pickle.dump(frames, f)

        frames = batches(frames, 500)
        all_frames = process_map(pd.concat, frames, max_workers=10, chunksize=10)

        start = datetime.now()
        df = pd.concat(all_frames)
        end = datetime.now()
        print(end - start)

        df.to_pickle(f"data/heroic_d{depth}_{target_name}dd.pickle")


def batches(lst, size: int):
    for i in range(0, len(lst), size):
        yield lst[i: i+size]


if __name__ == "__main__":
    # with open("data/heroic_d3_adservice-6d47d8bb4d.pickle", "rb") as f:
    #     frames = pickle.load(f)
    #
    # frames = batches(frames, 500)
    # all_frames = process_map(pd.concat, frames, max_workers=10, chunksize=10)
    #
    # start = datetime.now()
    # df = pd.concat(all_frames)
    # end = datetime.now()
    # print(end - start)
    #
    # df.to_pickle("heroic_d3_adservice.pickle")
    main()
    # df = pd.read_pickle("data/heroic_d3_cluster.localdd.pickle")
    # print(df.shape)