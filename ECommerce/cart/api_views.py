from urllib import request
from django.shortcuts import render
from rest_framework import APIView
from rest_framework import Response
from rest_framework.permissions import IsAuthenticated

class CartView(APIView):
    def get(self, request):
        pass

    def post(self, request):
        pass
