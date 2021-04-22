"""Main module."""
from dbConnectors.redisDbConnector import RedisDbConnector




if __name__ == "__main__":
    """Main"""
    connStr = 'host=127.0.0.1,db=1,port=6397'
    r = RedisDbConnector(connStr)
    r.connect()
