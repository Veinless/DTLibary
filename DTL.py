import requests
import json


class user:
	def __init__(self, token):
		self.token = token
		self.header = {
			"authorization": token
		}
	def send(self, message, channel):
		payload = {
			"content": message
		}
		r = requests.post("https://discord.com/api/v8/channels/" + channel + "/messages", data=payload, headers=self.header)
	def scrape(self, channel):
		r = requests.get("https://discord.com/api/v8/channels/" + channel + "/messages", headers=self.header)
		scraped = json.loads(r.text)
		return scraped
	def seperate(self, cjson):
		ret = []
		for value in cjson:
			ret.append(value)
		return ret
	def extract(self, value):
		return value["content"]
	def last_message(self, channel):
		h = self.scrape(channel)
		g = self.seperate(h)
		return g[0]["content"]
	def join(self, invite):
		requests.post("https://discord.com/api/v8/invites/" + invite, headers=self.header)
		
