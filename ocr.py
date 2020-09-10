from google.cloud import vision

def get_text(url):
    client = vision.ImageAnnotatorClient.from_service_account_json('/home/meenalgoswami115/credentials.json')
    image = vision.types.Image()
    image.source.image_uri = url

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

if __name__ == "__main__":
	get_text("gs://images-hackathon-288506/images/billing-invoice-with-payment-plan.png")
