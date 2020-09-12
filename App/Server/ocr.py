from google.cloud import vision
from google.cloud.vision import types
import json

def get_text_from_url(url):
    client = vision.ImageAnnotatorClient.from_service_account_json('/home/meenalgoswami115/credentials.json')
    image = vision.types.Image()
    image.source.image_uri = url
    response = client.text_detection(image=image)
    texts = response.text_annotations
    var = json.dumps(texts,indent=4)
    print(var)
    return texts
    # print('Texts:')

    # for text in texts:
    #     print('\n"{}"'.format(text.description))

    #     vertices = (['({},{})'.format(vertex.x, vertex.y)
    #                 for vertex in text.bounding_poly.vertices])

    #     print('bounds: {}'.format(','.join(vertices)))

    # if response.error.message:
    #     raise Exception(
    #         '{}\nFor more info on error messages, check: '
    #         'https://cloud.google.com/apis/design/errors'.format(
    #             response.error.message))

def get_text_from_file(file_path):
    client = vision.ImageAnnotatorClient.from_service_account_json('/home/meenalgoswami115/credentials.json')
    with io.open(file_path, 'rb') as image_file:
        content = image_file.read()
    image = types.Image(content=content)
    response = client.text_detection(image=image)
    with open('sample.json','w') as f:
        f.write(response)
    texts = response.text_annotations
    with open('texts.txt','w') as f:
        f.write(texts)
    return texts

if __name__ == "__main__":
    get_text_from_url("gs://images-hackathon-288506/images/sampleinvoice.png")