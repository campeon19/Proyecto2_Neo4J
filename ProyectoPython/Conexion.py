from neo4j import GraphDatabase


class Conexion:

    """Constructor de la coneccion"""
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    """FUncion para cerrar la conexion"""
    def close(self):
        self.driver.close()

    ###################### Funciones para consultar, estos son llamados desde el controlador ###########################

    """Funcion para crear un nodo nuevo"""
    def createNode(self, name, tags):
        with self.driver.session() as session:
            session.write_transaction(self._create_node, name, tags)

    """Funcion para eliminar un nodo"""
    def deleteNode(self, name):
        with self.driver.session() as session:
            session.write_transaction(self._delete_game, name)

    """Funcion para buscar con referecia a tags"""
    def searchtags(self, tags):
        with self.driver.session() as session:
            games = session.read_transaction(self._search_by_tags, tags)
            return games


    ##################### Funciones que ejecutan los queries #################################################
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
            for record in tx.run("MATCH (n:Juegos) WHERE $tag IN n.tags RETURN n.name", tag=tag):
                if record["n.name"] not in juegos:
                    juegos.append(record["n.name"])
        return juegos