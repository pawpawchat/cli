import requests
from api.utils import handle_request, build_url

def create(data):
    return handle_request(requests.post, build_url("profiles"), json=data)

def get_by_id(profile_id):
    return handle_request(requests.get, build_url("profiles", profile_id))

