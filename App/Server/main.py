import io
import os

from flask import Flask, render_template, request, jsonify, redirect
from flask_cors import CORS

from ocr import *
from parsingtesting import *
from budget import *
from parsing import *

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = "./uploads/"
app.config['RESOURCE_FOLDER'] = "./resources/"


@app.route('/')
def home():
	########## Insert Visualizations according to the JSON ###################

	return {"user" : "George W.", "spends" : get_spends(), 'thresholds' : get_budget()}



@app.route('/ocr',methods=['GET', 'POST'])
def ocr(url = "gs://images-hackathon-288506/images/sampleinvoice.png"):
	if request.method == "POST":
		image = request.files['fileKey']
		if image.filename != None:
			file_path = os.path.join(app.config["UPLOAD_FOLDER"],image.filename)
			image.save(file_path)
			print("File saved successfully : {}".format(file_path))
			texts = get_text_from_file(file_path)
			############# Insert Function Call here to identify products & respective value ################
			parsed_output = get_products(texts)
			######## and then Mapping to categories ###############
			return CategorizeElement(parsed_output)
	else:
		texts = get_text_from_url(url)
		parsed_output = get_products(texts)
		######## and then Mapping to categories ###############
		return CategorizeElement(parsed_output)
	return "File saved successfully"


@app.route('/offers')
def offers():
	return "George, based on your purchases\n We would like to offer you a 9% discount on your next Apparel Shopping!!\n Use BBJJKKK2020 for your purchase!"


@app.route('/budget' ,methods=['GET', 'POST'])
def budget():
	if request.method == "POST":
		new_data = request.data
		print(new_data)
		update_budget(new_data)
		print("Data updated")
		return {"status_code":201}
	############################## Insert Budget App call here #########################
	else:
		print("In else")
		return get_budget()

@app.route('/expenses',methods=['POST'])
def expenses():
	if request.method == "POST":
		new_data = request.data
		print(new_data)
		update_spends(new_data)
		print("Data updated")
		return {"status_code":201}

@app.route('/notifs',methods=['GET'])
def get_notifs():
	return {'data':["You have exceeded your Apparel Budget for September exceeded by 15%","Grocery spends reached 50%", "Electronics spends reached 90%"]}


if __name__ == "__main__":
	app.run(host="0.0.0.0",port=int(8000))
