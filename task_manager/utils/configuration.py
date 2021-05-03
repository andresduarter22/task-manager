config = {
    "redis_db": "127.0.0.1",
    "redis_port": 6379,
    "log_level": 10
}


class Configuration:
    def __init__(self):
        self.config = config

    def get_config_var(self, key):
        return self.config.get(key, default=None)
