from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def link_list(request):
    print(request.body)
