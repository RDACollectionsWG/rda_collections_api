import json
import copy

def decode_redis(o):
    rv = copy.deepcopy(o)
    if isinstance(rv, dict):
        for k, v in rv.items():
            if v.startswith("{"):
                rv[k] = json.loads(v)
    elif isinstance(rv, str) and rv.startswith("{"):
        rv = json.loads(rv)
    return rv

def encode_redis(o):
    rv = copy.deepcopy(o)
    if isinstance(rv, dict):
        for k, v in rv.items():
            if isinstance(v, dict) or isinstance(v, list):
                rv[k] = json.dumps(v)
    return rv
