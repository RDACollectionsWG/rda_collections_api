from flask import request
from rda_collections_api import redis_store
from rda_collections_api.api import decode_redis, encode_redis

from connexion import NoContent

def collections_list():

    members = redis_store.smembers("collections")
    ret = {"contents": []}
    for m in members:
        cbody = redis_store.hgetall("collections/{}".format(m))
        ret["contents"].append(decode_redis(cbody))
    return ret

def post():
    cbody = request.get_json()
    redis_store.sadd("collections", cbody["id"])
    redis_store.hmset("collections/{}".format(cbody["id"]), encode_redis(cbody))
    return cbody

def get_capabilities(id):
    return decode_redis(redis_store.hget("collections/{}".format(id), "capabilities"))

def get(id):
    return decode_redis(redis_store.hgetall("collections/{}".format(id)))

def put(id):
    cbody = request.get_json()
    redis_store.hmset("collections/{}".format(id), encode_redis(cbody))
    return NoContent, 202

def delete(id):
    redis_store.srem("collections", id)
    redis_store.delete("collections/{}".format(id))
    redis_store.delete("collections/{}/members".format(id))
    return NoContent, 200
