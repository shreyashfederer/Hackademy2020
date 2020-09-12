import json

with open('resources/user.json', 'rb') as f:
	data = json.load(f)

def get_spends():
	return data['budget']['spent']

def get_budget():
	return data['budget']['threshold']

def update_spends(new_data):

	"""
	new_data = {
		"name" : "user",
		"spent" : {"electronics":"80000","apparels":"1200","furniture":"7000"},
		"total" : 9000
	}
	"""
	
	for key in new_data["spent"].keys():
		data['budget']['spent'][key] = int(data['budget']['spent'][key]) + int(new_data["spent"][key])

	
	print("Data Updated")
	print(data)
