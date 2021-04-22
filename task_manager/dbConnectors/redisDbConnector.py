from abstractDbConnector import AbstractDbConnector, DbType
from redis import Redis


class RedisDbConnector(AbstractDbConnector):
    """
    Defines all the necessary behaviour for connecting to a Redis DB
    and performing the requested operations.
    ...

    Attributes
    ----------
    connection_string : str
        the string with all information necessary to connect to the db

    Methods
    -------
    connect():
        Tries to reach the DB and connect to it.

    insert():
        Inserts the given data to a db document.

    update():
        Updates some entry in a db document

    delete():
        deletes an entry in a db document

    """
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.host, self.db, self.port, self.pwd = self.parse_connection_string()
        self.r = Redis(host=self.host, db=self.db, port=self.port, pwd=self.pwd)

    def parse_connection_string(self):
        """
        splits connection_string into it's values

        Returns:
            host(str), db(int), port(int), pwd(str)

        connection_string has to have the format: 'field1=value1,field2=value2,...,fieldN=valueN'
        the fields must be named: 'host', 'db', 'port' and 'pwd' respectively
        returns None if no value found
        """
        params = self.connection_string.split(',')
        host, db, port, pwd = None, None, None, None
        for p in params:
            fld, val = p.split('=')
            if fld == 'host':
                host = val
            elif fld == 'db':
                db = val
            elif fld == 'port':
                port = val
            elif fld == 'pwd':
                pwd = val

        return host, db, port, pwd

    def connect(self):
        """
        connects to the DB.
        """
        return self.r.ping()

    def insert(self):
        """
        Inserts the given data to a db document.
        TODO
        """
        pass

    def update(self):
        """
        Updates some entry in a db document
        TODO
        """
        pass

    def delete(self):
        """
        deletes an entry in a db document
        TODO
        """
        pass

