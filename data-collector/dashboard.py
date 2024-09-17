import rdflib
from dash import Dash, dcc, html, Input, Output, no_update
import dash_cytoscape as cyto
import networkx as nx
from rdflib.namespace import RDF
from rdflib.extras.external_graph_libs import rdflib_to_networkx_digraph
from rdflib.term import Node

import collector
from ontology import deucalion


def get_base_name(node: Node) -> str:
    name = str(node)
    name_arr = name.split('#')
    if len(name_arr) == 1:
        name_arr = name.split('/')

    return name_arr[-1]


def get_elements_from_graph(graph: rdflib.Graph):
    elements = []

    nodes = set()
    for s, p, o in graph.triples((None, None, None)):
        if s not in nodes:
            elements.append({'data': {'id': s, 'label': get_base_name(s)}})
            nodes.add(s)

        if o not in nodes:
            elements.append({'data': {'id': o, 'label': get_base_name(o)}})
            nodes.add(o)

        elements.append({'data': {'source': s, 'label': get_base_name(p), 'target': o}})

    return elements


def show_dashboard(app_: Dash, graph: nx.Graph):
    stylesheet = [
        {
            'selector': 'node',
            'style': {
                'content': 'data(label)'
            }
        },
        {
            'selector': 'edge',
            'style': {
                'label': 'data(label)',
                'curve-style': 'bezier',
                'target-arrow-shape': 'triangle'
            }
        },
    ]

    app_.layout = html.Div([
        cyto.Cytoscape(
            id='graph',
            layout={'name': 'breadthfirst', 'directed': 'true'},
            style={'width': '100%', 'height': '1200px'},
            elements=get_elements_from_graph(graph),
            stylesheet=stylesheet
        ),
        html.P(id='tooltip')
    ])

    @app_.callback(
        Output('tooltip', 'children'),
        Input('graph', 'mouseoverNodeData'))
    def hover_node_callback(data):
        if data:
            return data['label']


if __name__ == '__main__':
    app = Dash(__name__)

    # network_topology = collector.fetch_network_topology()
    infrastructure_topology = collector.fetch_infrastructure_topology(namespace='sock-shop')
    infrastructure_topology.remove((None, RDF.type, None))

    ontology = rdflib_to_networkx_digraph(deucalion.world)

    show_dashboard(app, infrastructure_topology)

    app.run_server(debug=True)
