from flask import request
from rda_collections_api import redis_store
from rda_collections_api.api import decode_redis, encode_redis

from connexion import NoContent

def members_list(id):
    members = redis_store.smembers("collections/{}/members".format(id))
    ret = {"contents": []}
    for m in members:
        cbody = redis_store.hgetall("collections/{}/members/{}".format(id,m))
        ret["contents"].append(decode_redis(cbody))
    return ret

def post(id):
    mbody = request.get_json()
    redis_store.sadd("collections/{}/members".format(id), mbody["id"])
    redis_store.hmset("collections/{}/members/{}".format(id,mbody["id"]), encode_redis(mbody))
    return mbody

def get(id, mid):
    return decode_redis(redis_store.hgetall("collections/{}/members/{}".format(id,mid)))

def put(id, mid):
    mbody = request.get_json()
    redis_store.hmset("collections/{}/members/{}".format(id,mid), encode_redis(mbody))
    return NoContent, 202

def delete(id, mid):
    redis_store.srem("collections/{}/members".format(id), mid)
    redis_store.delete("collections/{}/members/{}".format(id,mid))
    return NoContent, 200

def get_property(id, mid, property):
    return decode_redis(redis_store.hget("collections/{}/members/{}".format(id,mid), property))
