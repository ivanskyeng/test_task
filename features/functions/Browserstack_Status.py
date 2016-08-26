import requests, json
from requests.auth import HTTPBasicAuth

class Changestatus:

	def error(self, context):
		url = 'https://www.browserstack.com/automate/sessions/'+context.browser.session_id+'.json'
		payload = {'status': 'Error', 'reason': 'Test Failed'}
		headers = {"content-type": "application/json"}
		r = requests.put(url, headers=headers, params=payload, auth=HTTPBasicAuth('user', 'password'))