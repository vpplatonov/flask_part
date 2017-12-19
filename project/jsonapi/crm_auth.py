
import requests


class CRMApiAuth(requests.auth.AuthBase):
    def __call__(self, r):
        r.headers['Content-Type'] = 'application/json'
        r.headers['Accept'] = 'application/json'
        r.headers['X-API-KEY'] = 'secret'
        return r
