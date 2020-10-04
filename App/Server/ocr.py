from google.cloud import vision
from google.cloud.vision import types
import json
import io

def get_text_from_url(url):
    client = vision.ImageAnnotatorClient.from_service_account_json('credentials.json')
    image = vision.types.Image()
    image.source.image_uri = url
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts
    

def get_text_from_file(file_path):
    client = vision.ImageAnnotatorClient.from_service_account_json('credentials.json')
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations
    return texts


if __name__ == "__main__":
    get_text_from_url("gs://images-hackathon-288506/images/sampleinvoice.png")
