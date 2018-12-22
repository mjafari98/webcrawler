from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .puller import pull_out
import json

@api_view(['POST'])
def link_list(request):
    text = json.loads(request.body)
    return Response(pull_out(text['uri'], text['depth']))
