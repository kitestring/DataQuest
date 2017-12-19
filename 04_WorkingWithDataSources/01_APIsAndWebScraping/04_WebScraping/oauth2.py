import json
import os
import requests
from datetime import datetime, timedelta

# followed this post as a guide to build this class
# https://www.reddit.com/r/redditdev/comments/2yekdx/how_do_i_get_an_oauth2_refresh_token_for_a_python/

class authentication():
	
	def __init__(self):
		self.client_settings_file = os.path.join(os.getcwd(), 'client_settings_json.txt')
		if os.path.isfile(self.client_settings_file):
			with open(self.client_settings_file) as json_data:
				auth = json.load(json_data)
				self.client_settings = auth['client_settings']
		else:
			print('Client settings file not found, cannot initialize object\n{}'.format(self.client_settings_file))
	
	def token_expired(self):
		# If token is still valid 
		# Returns the number of minutes that it will continue to be valid
		# Otherwise it will return True
		
		token_expires = datetime.strptime(self.client_settings['token_expires'], '%Y-%m-%d %H:%M:%S.%f')
		current_time = datetime.now()
		
		if token_expires > current_time:
			time_difference = token_expires - current_time
			return time_difference.total_seconds() / 60
		else:
			return True
	
	def verify_refresh_token(self):
		# Checks to see if token is valid
		# If status_code is 401 then gets a new token and returns True
		# If status_code is 200 then it prints the number of minutes it will continue to be valid and returns True
		# Otherwise it prints the response code and returns False
		
		headers = {"Authorization": self.client_settings['access_token'], "User-Agent": self.client_settings['user_agent']}
		response = requests.get("https://oauth.reddit.com", headers=headers)
		status = response.status_code
		
		if status == 200:
			print('Minutes until token expires:', self.token_expired())
		elif status == 401:
			self.get_new_token()
			print('Token not valid, new token created')
			print('Minutes until new token expires:', self.token_expired())
		else:
			print('Response Status Code:', status)
			return False
		
		print('\n')
		return True
	
	def get_new_token(self):
		client_auth = requests.auth.HTTPBasicAuth(self.client_settings['client_id'], self.client_settings['client_secret'] )
		headers = {'user-agent': self.client_settings['user_agent']}
		post_data = {"grant_type": "password", "username": self.client_settings[ "username" ], "password": self.client_settings[ "password" ]}
		response = requests.post( "https://www.reddit.com/api/v1/access_token", auth=client_auth, data=post_data, headers=headers)
		self.token_data = response.json()
		self.client_settings['access_token'] = self.token_data['token_type'] + " " + self.token_data['access_token']
		self.client_settings['token_expires'] = str(datetime.now() + timedelta(seconds=self.token_data['expires_in']))
		
		self.write_client_settings_tofile()
		
	def write_client_settings_tofile(self):
		if os.path.isfile(self.client_settings_file):
			os.remove(self.client_settings_file)
		
		auth = {'client_settings': self.client_settings, 'token_data': self.token_data}
			
		with open(self.client_settings_file, 'w') as outfile:
			json.dump(auth, outfile)
			outfile.close()