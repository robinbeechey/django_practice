from rest_framework import serializers
from django.contrib.auth.models import User
from polls.models import Question, Choice

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','question_set', 'password')

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id','choice_text', 'votes', 'question')

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'user', 'choice_set')
        read_only_fields = ('choice_set',)


