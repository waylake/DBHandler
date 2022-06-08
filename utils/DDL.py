import pymysql


class DDL:
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

    def create_table(self, conn, table_info):
        ...

    def truncate(self, conn: pymysql.connect, db, table):
        truncate_sql = f'truncate {db}.{table}'
        with conn.cursor() as curs:
            curs.execute(truncate_sql)
            curs.fetchall()
            curs.close()


