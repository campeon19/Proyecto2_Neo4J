from neo4j import GraphDatabase


class Conexion:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password), encrypted=False)

    def close(self):
        self.driver.close()

    # Envia el codigo del metodo '_create_person' a la base de datos.
    def save_name(self, name, age, preference):
        with self.driver.session() as session:
            session.write_transaction(self._create_person, name, age, preference)

    def save_place(self, place_name, location):
        with self.driver.session() as session_save_place:
            session_save_place.write_transaction(self._create_place, place_name, location)

    def find_user(self, username):
        with self.driver.session() as session_find_user:
            session_find_user.read_transaction(self._search_user, username)

    def delete_user(self, username):
        with self.driver.session() as session_delete_user:
            session_delete_user.write_transaction(self._delete_user, username)


conexion = Conexion("bolt://localhost:7687", "neo4j", "prueba123")
