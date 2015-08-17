from django.shortcuts import render, render_to_response
from rest_framework import viewsets
from django.template import RequestContext
from polls.models import Question, Choice
from rest_framework.decorators import list_route, detail_route
from django.contrib.auth.models import User
from api.serializers import QuestionSerializer, ChoiceSerializer, UserSerializer
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @list_route(methods=['get'])
    def current_user(self, request):
        user = self.request.user
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)

    @list_route(methods=['get'])
    def user_name(self, request):

        user = self.request.user
        serializer = self.get_serializer(user, many=False)
        return Response(serializer.data)

class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(user=user)

class ChoiceViewSet(viewsets.ModelViewSet):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer

