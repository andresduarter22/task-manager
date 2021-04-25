from abc import ABC, abstractmethod
from enum import Enum


class AbstractDbConnector(ABC):
    """
    Parent class defining general behaviour for all db connections

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

