import requests
import yaml

r = requests.get("https://raw.githubusercontent.com/RDACollectionsWG/apidocs/master/swagger.yaml")
o = yaml.load(r.content)

route_mapping = {
    ('/features', 'get'): "{{ app_name }}.api.features.get",
    ('/collections', 'get'): "{{ app_name }}.api.collections.collections_list",
    ('/collections', 'post'): "{{ app_name }}.api.collections.post",
    ('/collections/{id}', 'delete'): "{{ app_name }}.api.collections.delete",
    ('/collections/{id}', 'get'): "{{ app_name }}.api.collections.get",
    ('/collections/{id}', 'put'): "{{ app_name }}.api.collections.put",
    ('/collections/{id}/capabilities', 'get'): "{{ app_name }}.api.collections.get_capabilities",
    ('/collections/{id}/members', 'get'): "{{ app_name }}.api.members.members_list",
    ('/collections/{id}/members', 'post'): "{{ app_name }}.api.members.post",
    ('/collections/{id}/members/{mid}', 'delete'): "{{ app_name }}.api.members.delete",
    ('/collections/{id}/members/{mid}', 'get'): "{{ app_name }}.api.members.get",
    ('/collections/{id}/members/{mid}', 'put'): "{{ app_name }}.api.members.put",
    ('/collections/{id}/members/{mid}/properties/{property}', 'get'): "{{ app_name }}.api.members.get_property",
    ('/collections/{id}/members/{mid}/properties/{property}', 'put'): "{{ app_name }}.api.members.put_property",
    ('/collections/{id}/members/{mid}/properties/{property}', 'gost'): "{{ app_name }}.api.members.post_property",
    ('/collections/{id}/members/{mid}/properties/{property}', 'delete'): "{{ app_name }}.api.members.delete_property",
    ('/collections/{id}/ops/flatten', 'get'): "{{ app_name }}.api.collections_ops.flatten",
    ('/collections/{id}/ops/findMatch', 'post'): "{{ app_name }}.api.collections_ops.matching_members",
    ('/collections/{id}/ops/intersection/{otherId}', 'get'): "{{ app_name }}.api.collections_ops.intersection",
    ('/collections/{id}/ops/union/{otherId}', 'get'): "{{ app_name }}.api.collections_ops.union",

}

o["host"] = "{{ hostname }}:{{ port }}"

for path_key in o["paths"]:
    for method in o["paths"][path_key]:
        if (path_key, method) in route_mapping:
            o["paths"][path_key][method]["operationId"] = route_mapping[(path_key, method)]
        else:
            print("missing path", (path_key, method))

with open("rda_collections_api/swagger.yaml", "w") as sf:
    yaml.dump(o, sf)