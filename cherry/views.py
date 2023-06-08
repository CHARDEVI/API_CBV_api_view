from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from cherry.models import *
from cherry.serializers import *
from rest_framework.response import Response



class ProductCRUD(APIView):
    def get(self,request):
        PQS=Product.objects.all()
        PJD=ProductSerializer(PQS,many=True)
        return Response(PJD.data)


































