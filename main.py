from .utils import DML, DDL

class DBHandler:
    def __init__(self):
        self.dml = DML()
        self.ddl = DDL()
