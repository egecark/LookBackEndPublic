from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer
from .models import Option



class OptionSerializer(serializers.ModelSerializer):
        "user = serializers.RelatedField(User, read_only=True)"
        id = serializers.ReadOnlyField()

        class Meta:
            model = Option
            fields = ('id','option_description', 'answer_image', 'answer_tags')


class QuestionSerializer(serializers.ModelSerializer):
    "user = serializers.RelatedField(User, read_only=True)"
    id = serializers.ReadOnlyField()
    class Meta:
        model = Question
        fields = ('id','text', 'option_1', 'option_2', 'option_3', 'option_4')

    option_1 = OptionSerializer()
    option_2 = OptionSerializer()
    option_3 = OptionSerializer()
    option_4 = OptionSerializer()


class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('question', 'user', 'chosen_option')

