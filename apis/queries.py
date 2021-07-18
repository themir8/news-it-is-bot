from apis.models import Article
import requests
from vedis import Vedis


db = Vedis('./db')


def get_updates() -> Article:
    """Get a latest article from dev.to"""
    r = requests.get("https://dev.to/api/articles/latest",
                     params={"per_page": 1}).json()

    id = str(r[0]["id"])
    db['lastid'] = r[0]["id"]
    Article(**r)

    return r, id
