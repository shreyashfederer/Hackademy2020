import io
import os

from flask import Flask, render_template, request, jsonify, redirect
from ocr import get_text_from_url, get_text_from_file

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = "./uploads/"


@app.route('/')
def home():
	########## Insert Visualizations according to the JSON ###################

	return "Hello George!"



@app.route('/ocr')
def ocr(url = "gs://images-hackathon-288506/images/billing-invoice-with-payment-plan.png"):
	image = request.files['file']
	if image.filename != None:
		file_path = os.path.join(app.config["UPLOAD_FOLDER"],image.filename)
		image.save(file_path)
		print("File saved successfully : {}".format(file_path))
		texts = get_text_from_url(url)
		############# Insert Function Call here to identify products & respective value ################

		######## and then Mapping to categories ###############
	return "File saved successfully"


@app.route('/offers')
def offers():
	return "George, based on your purchases\n We would like to offer you a 9% discount on your next Apparel Shopping!!\n Use BBJJKKK2020 for your purchase!"


@app.route('/budget')
def budget():
	############################## Insert Budget App call here #########################
	return "Budget app"


@app.route('/notifs')
def get_notifs():
	return {'data':["You have exceeded your Apparel Budget for September exceeded by 15%","Grocery spends reached 50%", "Electronics spends reached 90%"]}


if __name__ == "__main__":
	app.run(port=int(443))