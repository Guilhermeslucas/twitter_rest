from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse
from rest_framework import status
from . import twitter_methods
from rest_framework.response import Response

class Tweets(APIView):
    def get(self, request, *args, **kwargs):
        search_arg = kwargs['search_pattern']
        result = twitter_methods.get_search(search_arg, 200)
        response = Response({'data':result})
        return response