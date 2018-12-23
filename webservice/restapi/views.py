from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, status
from .puller import pull_out
from .models import Answer
from .serializers import AnswerSerializer
import json

@api_view(['POST', 'GET'])
def link_list(request):
    if request.method == 'POST':
        # print(request.body)
        # return Response('200')
        text = json.loads(request.body)
        print(text['uri'], text['depth'])
        return Response(pull_out(text['uri'], text['depth']))

    if request.method == 'GET':
        return Response('GET request 200 OK', status=status.HTTP_200_OK)

# class AnswerView(generics.ListCreateAPIView):
#     queryset = Answer.objects.all()
#     serializer_class = AnswerSerializer
#     name = 'answer-view'
