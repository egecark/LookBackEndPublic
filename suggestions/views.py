import io
import os
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.http import HttpResponse, JsonResponse
from suggestions.models import Validation, EventType, Suggestion, SuggestionOption, SuggestionImages
from suggestions.serializer import ValidationSerializer, EventTypeSerializer, ValidationResultSerializer, SuggestionSerializer, SuggestionOptionSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import mixins
from rest_framework import generics
from google.cloud import vision
from google.cloud.vision import types
from django.views import generic
from suggestions.scripts import random_forest


dinner_date = ['dress', 'black', 'dark', 'formal']
returned_tags = ['dress', 'clothing', 'dark', 'cocktail dress', 'little black dress', 'bridal party dress', 'gown']
ege_ans = ['black', 'formal']


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

    i = 0
    #print('Labels:')
    for label in labels:
        if i == 5:
            break
        else:
            result.append(label.description)
            i = i+1
        #print(label.description)

        # Performs label detection on the image file
    webResponse = client.web_detection(image=image)
    webLabels = webResponse.web_detection


    #print('\nWeb Labels:')
    #for webLabel in webLabels.web_entities:
    #    print(webLabel.description)
    return result


def validate():
    validation_number = 0
    answer = False

    validation = Validation.objects.last()
    outfit_path = validation.image_path()
    # get the latest entry in validation
    event = validation.event_type.name
    result = random_forest(getVision(outfit_path), 1.0, 5).pop().pop()[0]
    if (result == "[u'"+event+"']"):
        answer = True

    return answer


class ValidationList(generics.ListCreateAPIView):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer
    
    def perform_create(self, serializer):
        validation = serializer.save()
        some_result = validate()
        serializer._data = {
            "image_path": validation.image_path(),
            "message": some_result
        }
class ValidateView(APIView):
    def get(self, request):
        response = validate()
        return Response({'result': response})

class ValidationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Validation.objects.all()
    serializer_class = ValidationSerializer


class EventList(generics.ListCreateAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class EventListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer

#class SuggestionList(generics.ListCreateAPIView):
#    queryset = Suggestion.objects.get(option_1__event_type__name="Wedding")[:5]
#    serializer_class = SuggestionSerializer

class SuggestionOptionList(generics.ListCreateAPIView):
    queryset = SuggestionOption.objects.filter(event_type__name="Wedding")[:5]
    serializer_class = SuggestionOptionSerializer


from rest_framework import serializers
class SuggestionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SuggestionOption
        fields = "answer_image",

# 2 ye gel
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

from random import sample 
class SuggestionImagesListAPIView(APIView):
    serializer_class = SuggestionImageSerializer
    pagination_class = None

    def head(self, request):
        return Response(list(EventType.objects.values_list('code_name')))


    def get(self, request):# biraz baydim hizlandiriyorum
        event_type = self.request.query_params.get("event_type", "")
        count = int(self.request.query_params.get("count", "5"))
        
        try:
            event_type_object = get_object_or_404(EventType, code_name=event_type)
        except Exception as e:
            a =  list(EventType.objects.values_list('code_name'))
            return Response({"expected": a, "got": event_type, "error": str(e)})


        qs = event_type_object.suggestionoption_set.all()
        

        images = sample(list(qs), count)
        def serialize(si):
            return {
                    "id": si.id,
                    "url": "https://looktheapp.com" + si.answer_image.url,
                    "tags" : list(si.image_tags.values_list("tag", flat=True))

                    }
        return Response([serialize(si) for si in images])
