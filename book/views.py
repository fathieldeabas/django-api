
from django.http import response
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from .models import Book
from .serializers import bookserializer
from rest_framework.response import Response
from django.http import HttpResponse

class BookV(APIView):
    def get(self,request):
        books=Book.objects.all()
        ser=bookserializer(books,many=True)
        # why use .data#
        return Response(ser.data)
    def post(self,request):
        Book.objects.create(titile=request.POST['titile'])
        return HttpResponse(status=200)