import json

with open ('resources/user.json', 'rb') as f:
	data = json.load(f)

def get_spends():
	return data['budget']['spent']

def get_budget():
	return data['budget']['threshold']