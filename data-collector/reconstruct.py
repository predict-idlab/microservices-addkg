from glob import glob
from rdflib import Graph
from rdflib.namespace import RDF
from ontology import deucalion


if __name__ == '__main__':
    file_list = list(glob('data/graph_*'))

    for f in file_list:
        g = Graph()
        g.parse(f, format='ttl')

        connections = g.objects(None, deucalion.hasConnection.ref)

        for c in connections:
            g.remove((c, None, None))
            g.remove((None, None, c))

        f_name = f.split('\\')[-1]
        g.serialize(f'data/reconstructed/{f_name}')
