from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from . import twitter_methods
from rest_framework.response import Response

class Tweets(APIView):
    def get(self, request, *args, **kwargs):
        search_arg = kwargs['search_pattern']
        result = twitter_methods.get_search(search_arg, 1)
        results = []
        for r in result:
            new_result = {}
            aux_result = r._json
            new_result['text'] = r.text
            new_result['id'] = r.id
            new_result['created_at'] = r.created_at
            new_result['in_reply_to_status_id'] = r.in_reply_to_status_id
            new_result['in_reply_to_screen_name'] = r.in_reply_to_screen_name
            new_result['retweet_count'] = r.retweet_count
            new_result['favorite_count'] = r.favorite_count
            new_result['coordinates'] = r.coordinates
            new_result['user_name'] = r.user.screen_name
            new_result['user_followers'] = r.user.followers_count
            new_result['user_following'] = r.user.friends_count
            results.append(aux_result)
        return Response({'data': results})
