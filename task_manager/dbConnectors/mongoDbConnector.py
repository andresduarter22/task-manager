from abstractDbConnector import AbstractDbConnector, DbType


class MongoDbConnector(AbstractDbConnector):
    """
    Defines all the necessary behaviour for connecting to a Mongo DB
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

    validate():
        validates if the input data is the right format

    """

    def __init__(self, connection_string):
        self.connection_string = connection_string

    def connect(self):
        """
        connects to the DB.
        TODO
        """
        pass

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

    def validate(self):
        """
        validates if the input data is the right format
        TODO
        """
        pass
