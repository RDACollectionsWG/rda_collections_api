from flask import request
from rda_collections_api import redis_store
from rda_collections_api.api import decode_redis, encode_redis
from rda_collections_api.api.members import get as getMember

def matching_members():
    return {}

def intersection(id, otherId):
    contents = []
    for m in redis_store.sinter(
        "collections/{}".format(id),
        "collections/{}".format(otherId)
    ):
        contents.append(getMember(id, m))

    return {
        "contents": contents,
        "next_cursor": "string",
        "prev_cursor": "string"
    }

def union(id, otherId):
    contents = []
    for m in redis_store.sunion(
        "collections/{}".format(id),
        "collections/{}".format(otherId)
    ):
        contents.append(getMember(id, m))

    return {
        "contents": contents,
        "next_cursor": "string",
        "prev_cursor": "string"
    }

def flatten():
    return {}