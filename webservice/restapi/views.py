from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import json

@api_view(['POST'])
def link_list(request):
    j = json.loads(request.body)
    return Response(j['uri'])
