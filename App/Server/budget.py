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
	new_data = json.loads(new_data)
	for key in new_data["spent"]:
		my_key = key['room']
		print(type(key))
		data['budget']['spent'][my_key] = str(int(data['budget']['spent'][my_key]) + int(key['budget']))

	
	print("Data Updated")
	print(data)

def update_budget(new_data):
	new_data = json.loads(new_data)
	for key in new_data["spent"]:
		my_key = key['room']
		print(type(key))
		data['budget']['threshold'][my_key] = int(key['budget'])

	
	print("Data Updated")
	print(data)