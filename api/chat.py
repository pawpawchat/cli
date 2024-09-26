import requests
from api.utils import handle_request, build_url

def create(data):
    return handle_request(requests.post, build_url("chats"), json=data)

def get_all(profile_id):
    return handle_request(requests.get, build_url("chats", profile_id=profile_id))

def get_by_id(chat_id):
    return handle_request(requests.get, build_url("chats", chat_id))

def get_members(chat_id):
    return handle_request(requests.get, build_url("chats", chat_id, "members"))

def send_message(chat_id, data):
    return handle_request(requests.post, build_url("chats", chat_id, "messages"), json=data)