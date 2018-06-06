from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Validation
from .models import Suggestion
from .models import EventType
from .models import SuggestionOption


class EventTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventType
        fields = ('name', 'tags')


class ValidationSerializer(serializers.ModelSerializer):
    "user = serializers.RelatedField(User, read_only=True)"

    class Meta:
        model = Validation
        fields = ('feedback', 'event_date', 'event_type', 'user', 'outfit_image', 'event_type_details')
    def get_event_type_details(self, validation):
        return {
            "name": validation.event_type.name,
            "tags": [tag.tag_name for tag in validation.event_type.tags.all()]		
        }
    event_type_details = serializers.SerializerMethodField()


class ValidationResultSerializer(serializers.ModelSerializer):
    "user = serializers.RelatedField(User, read_only=True)"

    class Meta:
        model = Validation
        fields = ('feedback', 'event_date', 'event_type', 'user', 'outfit_image')



class SuggestionSerializer(serializers.ModelSerializer):
    "user = serializers.RelatedField(User, read_only=True)"

    class Meta:
        model = Suggestion
        fields = ('user', 'event_date', 'option_1', 'option_2', 'option_3', 'option_4', 'option_5', 'feedback')

class SuggestionOptionSerializer(serializers.ModelSerializer):
    "user = serializers.RelatedField(User, read_only=True)"

    class Meta:
        model = SuggestionOption
        fields = ('answer_image', 'event_type', 'image_tags')
