import json

class Action(object):

	def __init__(self):
		pass

	def read(self, json_file):
		with open(json_file, 'r+') as f:
			text = f.read()
		data = ''
		try:
			data = json.loads(text)
		except Exception as e:
			print("Error when loading the JSON file")
			print(e)
		finally:
			return data

	def import_data(self,data):
		pass
