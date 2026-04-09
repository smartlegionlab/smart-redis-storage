# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2026, Alexander Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import redis
import json


class RedisStorageManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.r = redis.Redis(host=host, port=port, db=db)

    def set_data(self, uniq_key, key, value, expiration=None):
        uniq_key = f"uniq:{uniq_key}"
        self.r.hset(uniq_key, key, json.dumps(value))
        if expiration is not None:
            self.r.expire(uniq_key, expiration)

    def get_data(self, uniq_key, key, pop=False):
        uniq_key = f"uniq:{uniq_key}"
        data = self.r.hget(uniq_key, key)
        if pop and data is not None:
            self.r.hdel(uniq_key, key)
        return json.loads(data) if data else None

    def get_all_data(self, uniq_key):
        uniq_key = f"uniq:{uniq_key}"
        data = self.r.hgetall(uniq_key)
        decoded_data = {key.decode(): json.loads(value) for key, value in data.items()}
        return decoded_data

    def delete_key(self, uniq_key, key):
        uniq_key = f"uniq:{uniq_key}"
        self.r.hdel(uniq_key, key)

    def delete_all_hash(self, uniq_key):
        uniq_key = f"uniq:{uniq_key}"
        self.r.delete(uniq_key)

    def pop_data(self, uniq_key, key):
        return self.get_data(uniq_key, key, pop=True)

    def update_data(self, uniq_key, key, value, expiration=None):
        uniq_key = f"uniq:{uniq_key}"
        self.r.hset(uniq_key, key, json.dumps(value))
        if expiration is not None:
            self.r.expire(uniq_key, expiration)

    def get_ttl(self, uniq_key):
        uniq_key = f"uniq:{uniq_key}"
        ttl = self.r.ttl(uniq_key)
        return ttl if ttl >= 0 else (0 if ttl == -2 else -1)
