from neo4j import GraphDatabase


class Conexion:

    """Constructor de la coneccion"""
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    """Funcion para cerrar la conexion"""
    def close(self):
        self.driver.close()

    ###################### Funciones para consultar, estos son llamados desde el controlador ###########################

    """Funcion para crear un nodo nuevo"""
    def createNode(self, name, tags, time, compatibility):
        with self.driver.session() as session:
            session.write_transaction(self._create_node, name, tags, time, compatibility)

    """Funcion para eliminar un nodo"""
    def deleteNode(self, name):
        with self.driver.session() as session:
            session.write_transaction(self._delete_game, name)

    """Funcion para buscar con referecia a tags"""
    def searchgame(self, tags):
        with self.driver.session() as session:
            games = session.read_transaction(self._search_by_tags, tags)
            return games

    """Funcion para buscar por tags y por tiempo"""
    def searchGameByTagsAndTime(self, tags, tMin, tMax):
        with self.driver.session() as session:
            games = session.read_transaction(self._search_by_tags_time, tags, tMin, tMax)
            return games

    """Funcion para buscar por tags, tiempo y plataformas"""
    def searchGameTagsPlatforms(self, tags, tMin, tMax, plataform):
        with self.driver.session() as session:
            games = session.read_transaction(self. _search_tags_time_platafomrs, tags, tMin, tMax, plataform)
            return games

    """Funcion para obtener todas las caracteristicas disponibles en los nodos"""
    def getCharacteristics(self):
        with self.driver.session() as session:
            return session.read_transaction(self._get_characteristics)

    """Funcion para obtener las plataformas"""
    def getPlataforms(self):
        with self.driver.session() as session:
            return session.read_transaction(self._get_plataforms)

    """Funcion para crear relaciones entre nodos"""
    def createRelation(self, game1, tag):
        games = self.searchgame([tag])
        with self.driver.session() as session:
            for game in games:
                if game1 != game:
                    session.write_transaction(self._game_relation, game1, game)

    """Funcion que retorna los nombres de los nodos"""
    def getNombres(self):
        with self.driver.session() as session:
            return session.read_transaction(self._get_names)

    ##################### Funciones que ejecutan los queries #################################################

    @staticmethod
    def _search_tags_time_platafomrs(tx, tags, tMin, tMax, platform):
        juegos = {}
        for tag in tags:
            for record in tx.run("MATCH (n:Juegos) WHERE $tag IN n.tags AND $tMin <= n.time <= $tMax "
                                 "AND $platform IN n.compatibility "
                                 "RETURN n.name", tag=tag, tMin=float(tMin), tMax=float(tMax), platform=platform):
                if tag not in juegos:
                    juegos[tag] = []
                if record["n.name"] not in juegos[tag]:
                    juegos[tag].append(record["n.name"])
        return juegos


    @staticmethod
    def _get_characteristics(tx):
        caracteristicas = []
        v = tx.run("MATCH (j:Juegos) RETURN j.tags")
        for n in v:
            for c in n["j.tags"]:
                if c not in caracteristicas:
                    caracteristicas.append(c)
        return sorted(caracteristicas)

    @staticmethod
    def _get_plataforms(tx):
        plataformas = []
        v = tx.run("MATCH (j:Juegos) RETURN j.compatibility")
        for n in v:
            for c in n["j.compatibility"]:
                if c not in plataformas:
                    plataformas.append(c)
        return sorted(plataformas)

    @staticmethod
    def _create_node(tx, name, tags, time, compatibility):
        tx.run("CREATE (:Juegos {name: $name, tags: $tags, time:$time, compatibility:$compatibility})", name=name, tags=tags, time=float(time), compatibility=compatibility)

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

    @staticmethod
    def _search_by_tags_time(tx, tags, tMin, tMax):
        juegos = {}
        for tag in tags:
            for record in tx.run("MATCH (n:Juegos) WHERE $tag IN n.tags AND $tMin <= n.time <= $tMax "
                                 "RETURN n.name", tag=tag, tMin=float(tMin), tMax=float(tMax)):
                if tag not in juegos:
                    juegos[tag] = []
                if record["n.name"] not in juegos[tag]:
                    juegos[tag].append(record["n.name"])
        return juegos

    @staticmethod
    def _game_relation(tx, game1, game2):
        tx.run("MATCH (n:Juegos {name: $game1}) "
               "MATCH (j:Juegos {name: $game2}) "
               "CREATE (n)-[:Relation]->(j)", game1=game1, game2=game2)

    @staticmethod
    def _get_names(tx):
        result = tx.run("MATCH (j:Juegos) RETURN j.name")
        nombres = []
        for res in result:
            nombres.append(res["j.name"])
        return sorted(nombres)


