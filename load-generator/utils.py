import copy
import networkx as nx
from pyvis import network as pvnet


def plot_g_pyviz(graph: nx.Graph, name='graph.html', height='1000px', width='1000px'):
    g = copy.deepcopy(graph)
    net = pvnet.Network(notebook=True, directed=True, height=height, width=width)
    opts = '''
        var options = {
          "physics": {
            "minVelocity": 0.75,
            "timestep": 0.22
          }
        }
    '''

    net.set_options(opts)
    # uncomment this to play with layout
    # net.show_buttons(filter_=['physics'])
    net.from_nx(g)
    return net.show(name)
