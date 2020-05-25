from neo4j import GraphDatabase


class Conexion:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    def close(self):
        self.driver.close()

    def createNode(self, name, tags):
        with self.driver.session() as session:
            session.write_transaction(self._create_node, name, tags)

    def deleteNode(self, name):
        with self.driver.session() as session:
            session.write_transaction(self._delete_game, name)

    @staticmethod
    def _create_node(tx, name, tags):
        tx.run("CREATE (:Juegos {name: $name, tags: $tags, n:0})", name=name, tags=tags)

    @staticmethod
    def _delete_game(tx, name):
        tx.run("MATCH (n:Juegos) WHERE n.name=$name DETACH DELETE n", name=name)
