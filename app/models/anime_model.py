from app.models import DatabaseConnector
from psycopg2 import sql

class Anime(DatabaseConnector):
    anime_keys = ["id", "anime", "released_date", "seasons"]
    keys_to_compare = ["anime", "released_date", "seasons"]
    def __init__(self, *args, **kwargs):
        self.anime = kwargs["anime"].title()
        self.released_date = kwargs["released_date"]
        self.seasons = kwargs["seasons"]
    
    @staticmethod
    def serialize_anime(data, keys=anime_keys):
        if type(data) is tuple:
            return dict(zip(keys, data))
        if type(data) is list:
            return [dict(zip(keys, anime)) for anime in data]
        return "NÃO CAIU E, NENHUM IF"

    @classmethod
    def read_animes(cls):
        cls.create_table()
        cls.get_conn_cur()
        query = """
            SELECT * FROM animes
        """
        cls.cur.execute(query)
        animes = cls.cur.fetchall()
        cls.close_and_commit()
        return animes

    @classmethod
    def read_by_id(cls, anime_id):
        cls.create_table()
        cls.get_conn_cur()

        query = f"SELECT * FROM animes WHERE id = {anime_id};"
        cls.cur.execute(query)
        anime = cls.cur.fetchall()
        cls.close_and_commit()
        return anime

    def create_anime(self):
        self.create_table()
        self.get_conn_cur()
        query = """
            INSERT INTO 
                animes(anime, released_date, seasons)
            VALUES
                (%s, %s, %s)
            RETURNING *
        """
        query_values = list(self.__dict__.values())
        self.cur.execute(query, query_values)
        inserted_anime = self.cur.fetchone()
        self.close_and_commit()
        return inserted_anime
    
    @classmethod
    def update_anime(cls, anime_id, update_data):
        cls.create_table()
        cls.get_conn_cur()

        if update_data["anime"]:
            update_data["anime"] = update_data["anime"].title()
            
        keys = [sql.Identifier(key) for key in update_data.keys()]
        values = [sql.Literal(value) for value in update_data.values()]

        query = sql.SQL(
            """
                UPDATE 
                    animes
                SET
                    ({keys}) = ROW({values})
                WHERE
                    id={id}
                RETURNING *;
            """
        ).format(
            id=sql.Literal(anime_id),
            keys=sql.SQL(",").join(keys),
            values=sql.SQL(",").join(values),
        )

        cls.cur.execute(query)
        updated_anime = cls.cur.fetchone()
        cls.close_and_commit()
        return updated_anime
    
    @classmethod
    def delete_anime_by_id(cls, anime_id):
        cls.create_table()
        cls.get_conn_cur()
        query = f"DELETE FROM animes WHERE id = {anime_id} RETURNING *;"

        cls.cur.execute(query)
        deleted_anime = cls.cur.fetchall()
        cls.close_and_commit()
        return deleted_anime