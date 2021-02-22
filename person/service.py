import json

import urllib3


def _make_request_to_api(url: str, data: dict[str] = {}, *, token: str = None, method="POST"):
    if token is not None:
        auth_header = {
            "Authorization": f"Bearer {token}"
        }
    else:
        auth_header = {}

    data = json.dumps(data)
    http = urllib3.PoolManager()
    response = http.request(
        method.upper(),
        f"http://127.0.0.1:8000/api/v1/{url}",
        body=data,
        headers={'Content-Type': 'application/json', **auth_header}
    )
    return json.loads(response.data.decode('utf-8'))


def create_user(data: dict[str]) -> None:
    _make_request_to_api('user/', data)


def create_post(data: dict[str], token: str) -> int:
    post_data = _make_request_to_api('post/', data, token=token)
    return post_data["id"]


def get_access_token(credentials: dict[str]) -> str:
    res_data = _make_request_to_api('token/', credentials)
    access_token = res_data["access"]
    return access_token


def like_posts(token: str, post_ids: list[int]) -> None:
    for post_id in post_ids:
        res = _make_request_to_api(f'like/{post_id}/', token=token, method="PUT")
