import io
import os
from google.cloud import vision
from google.cloud.vision import types
from os import walk
from os.path import splitext
from os.path import join


        #print (os.path.abspath(p))

def getVision(filepath):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "look_django/Vision-3be131c0d9f3.json"

    # Instantiates a client
    client = vision.ImageAnnotatorClient()

    # The name of the image file to annotate
    file_name = os.path.join(
        os.path.dirname(__file__),
        filepath)

    # Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    # Performs label detection on the image file
    response = client.label_detection(image=image)
    labels = response.label_annotations

    result = []

    print('Labels:')
    for label in labels:
        result.append(label.description)
        print(label.description)

        # Performs label detection on the image file
    webResponse = client.web_detection(image=image)
    webLabels = webResponse.web_detection


    print('\nWeb Labels:')
    for webLabel in webLabels.web_entities:
        print(webLabel.description)
    return result


for root, dirs, files in os.walk('C:/Users/Lenovo/Downloads/first date clothes'):
    for file in files:
        p=os.path.join(root,file)
        getVision(p)