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
        
    def post(self,request):
        PMSD=ProductSerializer(data=request.data)
        if PMSD.is_valid():
            SPO=PMSD.save()
            
            return Response({'message':'Product is Created'})
        else:
            return Response({'Failed':'Product Creation is Failed'})
        



    def put(self,request):
        id=request.data['id']
        PO=Product.objects.get(id=id)
        UPO=ProductSerializer(PO,data=request.data)
        if UPO.is_valid():
            UPO.save()
            return Response({'message':'Product is Updated'})
        else:
            return Response({'Failed':'Product is not Updated'})


































