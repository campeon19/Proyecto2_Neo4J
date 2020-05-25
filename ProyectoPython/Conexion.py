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

    def searchtags(self, tags):
        with self.driver.session() as session:
            games = session.read_transaction(self._search_by_tags, tags)
            return games

    @staticmethod
    def _create_node(tx, name, tags):
        tx.run("CREATE (:Juegos {name: $name, tags: $tags})", name=name, tags=tags)

    @staticmethod
    def _delete_game(tx, name):
        tx.run("MATCH (n:Juegos) WHERE n.name=$name DETACH DELETE n", name=name)


    @staticmethod
    def _search_by_tags(tx, tags):
        juegos = []
        for tag in tags:
            for elemento in tx.run("MATCH (n:Juegos) WHERE $tag IN n.tags RETURN n.name", tag=tag):
                juegos.append(elemento["n.name"])
        return juegos