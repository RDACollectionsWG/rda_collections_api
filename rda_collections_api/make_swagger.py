import requests
import yaml

r = requests.get("https://raw.githubusercontent.com/RDACollectionsWG/apidocs/master/swagger.yaml")
o = yaml.load(r.content)

route_mapping = {
    ('/capabilities', 'get'): "{{ app_name }}.api.capabilities.get",
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
    ('/collections/{id}/ops/intersectionOf/{otherId}', 'get'): "{{ app_name }}.api.collections_ops.intersection",
    ('/collections/{id}/ops/matchingMembers', 'post'): "{{ app_name }}.api.collections_ops.matching_members",
    ('/collections/{id}/ops/unionOf/{otherId}', 'get'): "{{ app_name }}.api.collections_ops.union",
}

for path_key in o["paths"]:
    for method in o["paths"][path_key]:
        if (path_key, method) in route_mapping:
            o["paths"][path_key][method]["operationId"] = route_mapping[(path_key, method)]

with open("collections_demo/swagger.yaml", "w") as sf:
    yaml.dump(o, sf)