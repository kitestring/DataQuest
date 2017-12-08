import json
import os
import requests


class authentication():
	
	def __init__(self):
		self.client_settings_file = os.path.join(os.getcwd(), 'client_settings_json.txt')
		with open(self.client_settings_file) as json_data:
			auth = json.load(json_data)
			self.client_settings = auth['client_settings']
	
	def get_new_token(self):
		client_auth = requests.auth.HTTPBasicAuth(self.client_settings['client_id'], self.client_settings['client_secret'] )
		headers = {'user-agent': self.client_settings['user_agent']}
		post_data = {"grant_type": "password", "username": self.client_settings[ "username" ], "password": self.client_settings[ "password" ]}
		response = requests.post( "https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
		self.token_data = response.json()
		self.client_settings['access_token'] = self.token_data['token_type'] + " " + self.token_data['access_token']
		
		# self.token_expiration = current_time + token_data[ 'expires_in' ]
		# self.reddit.set_access_credentials( token_data[ 'scope' ], token_data[ 'access_token' ] )
		self.write_client_settings_tofile()
		
	def write_client_settings_tofile(self):
		if os._exists(self.client_settings_file):
			os.remove(self.client_settings_file)
		
		auth = {'client_settings': self.client_settings, 'token_data': self.token_data}
			
		with open(self.client_settings_file, 'w') as outfile:
			json.dump(auth, outfile)
			outfile.close()