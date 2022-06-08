import pymysql

class DML:
    def __init__(self, host, db, user, password, port):
        self.host = host
        self.db = db
        self.user = user
        self.password = password
        self.port = port
        self.conn = self.get_conn()

    def get_conn(self) -> pymysql.connect:
        connection = pymysql.connect(host=self.host,
                                    db=self.db,
                                    user=self.user,
                                    password=self.password,
                                    port=self.port,
                                    autocommit=True,
                                    cursorclass=pymysql.cursors.DictCursor,
                                    charset='utf8',
                                    max_allowed_packet=16 * 1024)
        return connection

    def insert_rows(self, rows, table_info):
        ...

    def get_last_id(self, conn, db, table, id):
        last_id_sql = f"SELECT {id} FROM  {db}.{table} ORDER BY {id} DESC LIMIT 1"
        with conn.cursor() as curs:
            curs.execute(last_id_sql)
            result = curs.fetchall()
            curs.close()
            last_db_id = result[0][id]
            return last_db_id
