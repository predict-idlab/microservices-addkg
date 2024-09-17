from rdflib_ontology import Ontology, Thing, ObjectProperty, DatatypeProperty


deucalion = Ontology(
    base_uri='https://github.com/predict/deucalion#',
    version='0.0.1',
    creators=['Pieter Moens'],
    preferred_namespace_prefix='deucalion',
)

# Classes


class Cluster(Thing):
    namespace = deucalion


class Node(Thing):
    namespace = deucalion


class Workload(Thing):
    namespace = deucalion


class ReplicaSet(Workload):
    namespace = deucalion


class Deployment(Workload):
    namespace = deucalion


class Pod(Thing):
    namespace = deucalion


class Container(Thing):
    namespace = deucalion


class Image(Thing):
    namespace = deucalion


class Resource(Thing):
    namespace = deucalion

    label: str
    description: str


class CPU(Resource):
    namespace = deucalion


class Memory(Resource):
    namespace = deucalion


class FileSystem(Resource):
    namespace = deucalion


class Service(Thing):
    namespace = deucalion


class Connection(Thing):
    namespace = deucalion


# Properties
class HasNode(ObjectProperty):
    namespace = deucalion

    domain = [Cluster]
    range = [Node]


class IsControlledBy(ObjectProperty):
    namespace = deucalion

    domain = [Pod, Workload]
    range = [Workload]


class Controls(ObjectProperty):
    namespace = deucalion
    inverse_of = IsControlledBy

    domain = [Workload]
    range = [Pod, Workload]


class IsServedBy(ObjectProperty):
    namespace = deucalion

    domain = [Pod]
    range = [Service]


class Serves(ObjectProperty):
    namespace = deucalion
    inverse_of = IsServedBy

    domain = [Service]
    range = [Pod]


class HasContainer(ObjectProperty):
    namespace = deucalion

    domain = [Pod]
    range = [Container]


class HasPod(ObjectProperty):
    namespace = deucalion

    domain = [Node]
    range = [Pod]


class HasMetricName(DatatypeProperty):
    pass


class HasCPU(DatatypeProperty):
    namespace = deucalion

    domain = [Node, Container]
    range = [float]


class HasMemory(DatatypeProperty):
    namespace = deucalion

    domain = [Node, Container]
    range = [float]


class HasFileSystem(DatatypeProperty):
    namespace = deucalion

    domain = [Node]
    range = [float]


class HasFileSystemAvailable(HasFileSystem):
    namespace = deucalion

    domain = [Node]
    range = [float]


class HasFileSystemSize(HasFileSystem):
    namespace = deucalion

    domain = [Node]
    range = [float]


class HasConnection(ObjectProperty):
    namespace = deucalion

    domain = [Pod]
    range = [Connection]


class HasSource(ObjectProperty):
    namespace = deucalion

    domain = [Connection]
    range = [Pod]


class HasDestination(ObjectProperty):
    namespace = deucalion

    domain = [Connection]
    range = [Service]


class HasRequestCount(DatatypeProperty):
    namespace = deucalion

    domain = [Connection]
    range = [float]


class HasRequestCount4XX(DatatypeProperty):
    namespace = deucalion

    domain = [Connection]
    range = [float]


class HasRequestCount5XX(DatatypeProperty):
    namespace = deucalion

    domain = [Connection]
    range = [float]


class HasRequestDuration(DatatypeProperty):
    namespace = deucalion

    domain = [Connection]
    range = [float]


class HasRequestSize(DatatypeProperty):
    namespace = deucalion

    domain = [Connection]
    range = [float]


class HasImage(ObjectProperty):
    namespace = deucalion

    domain = [Container]
    range = [Image]


class HasName(DatatypeProperty):
    namespace = deucalion

    domain = [Image]
    range = [str]


class HasTag(DatatypeProperty):
    namespace = deucalion

    domain = [Image]
    range = [str]


if __name__ == '__main__':
    node = Node(name='nodes/n1')
    pod = Pod(name='pods/p1')

    node.has_pod = pod

    for n in Node.instances:
        print(n)

    for triple in deucalion.world.triples((None, None, None)):
        print(triple)
