import json
import webbrowser
import requests

class API:

    base_url = 'https://fantasysports.yahooapis.com/fantasy/v2'
    authorize_url = 'https://api.login.yahoo.com/oauth2/request_auth'
    access_token_url = 'https://api.login.yahoo.com/oauth2/get_token'
    redirect_uri = 'oob'
    token_path = '.tokens.json'

    def __init__(self, client_id, client_secret, league_id=None):
        self.client_id = client_id
        self.client_secret = client_secret
        self.league_id = league_id
        tokens = self._load_tokens()
        if tokens:
            self._set_tokens(tokens)
        else:
            self._get_tokens()

    def _load_tokens(self):
        try:
            with open(self.token_path, 'r') as f:
                return json.loads(f.read())
        except FileNotFoundError:
            return None

    def _get_tokens(self):
        params = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'response_type': 'code',
            'language': 'en-us',
        }
        headers = {'Content-Type': 'application/json'}
        response = requests.post(self.authorize_url, params=params, headers=headers)
        webbrowser.open(response.url)
        code = input('Yahoo Share Code: ')
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'code': code,
            'grant_type': 'authorization_code',
        }
        response = requests.post(self.access_token_url, data=data)
        self._set_tokens(response.json())

    def _set_tokens(self, data):
        self.access_token = data['access_token']
        self.refresh_token = data['refresh_token']
        with open(self.token_path, 'w') as f:
            f.write(json.dumps({
                'access_token': self.access_token,
                'refresh_token': self.refresh_token,
            }))

    def refresh_tokens(self):
        data = {
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'redirect_uri': self.redirect_uri,
            'refresh_token': self.refresh_token,
            'grant_type': 'refresh_token',
        }
        response = requests.post(self.access_token_url, data=data)
        self._set_tokens(response.json())

    def get(self, end_point):
        url = f'{self.base_url}/{end_point}'
        response = requests.get(url, params={'format':'json'}, headers={'Authorization': f'Bearer {self.access_token}'})
        return response.json()
