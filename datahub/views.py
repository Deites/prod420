import requests

from django.views.generic import TemplateView

class DataTable(TemplateView):
    template_name = 'datahub/index.html'

    def get(self, *args, **kwargs):

        r_data = requests.get('http://193.122.78.15/api/ver1/events/all', headers={'Authorization' : f'Token {self.auth_token()}'}).json()
        
        return self.render_to_response({'r_data' : r_data})

    def auth_token(self):

        auth_data = {
            'username' : 'tester',
            'password' : 'tester12345678',
        }

        r_token = requests.post('http://193.122.78.15/api/ver1/api-token-auth/', auth_data).json()['token']

        return r_token
