import redis


class MyRedis:
    def __init__(self, host='localhost', port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.pool = redis.ConnectionPool(host=self.host, port=self.port, db=self.db)

    def connect(self):
        _redis = redis.Redis(connection_pool=self.pool)
        return _redis










