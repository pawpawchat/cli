from requests.exceptions import ConnectionError
from json import dumps


API_URL = "http://localhost:9400/api"
def build_url(*path_parts, **kwargs):
    base_url = "/".join([API_URL, *map(str, path_parts)])
    
    if kwargs:
        query_params = "&".join([f"{key}={value}" for key, value in kwargs.items()])
        return f"{base_url}?{query_params}"
    
    return base_url


def handle_request(request_func, *args, **kwargs):
    try:
        response = request_func(*args, **kwargs)

        if response.status_code in [200, 201]:
            return dumps(extract_json(response), indent=4), None
        
        if response.status_code == 405:
            return dumps({
                "code": response.status_code, 
                "error": "method not allowed", 
                "method": response.request.method, 
                "url":response.url
            }, indent=4), "error"

        if response.status_code in [400, 404]:
            return dumps({
                "code":response.status_code, 
                "error": extract_json(response), 
                "url": response.url
            }, indent=4), "error"

        return extract_json(response), "unknown error"

    except ConnectionError:
        return dumps({"error":"connection refused"}, indent=4), "error"


def extract_json(response):
    try:
        return response.json()
    except ValueError:
        return {}
