from django.db.models import Sum
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import Product, ProductSerializer
import pandas as pd

class ProductImportView(APIView):
    def post(self, request):
        file = request.FILES['file']
        df = pd.read_excel(file)

        df = df.dropna()
        df['mf_date'] = pd.to_datetime(df['mf_date']).dt.date
        df['exp_date'] = pd.to_datetime(df['exp_date']).dt.date
        print(df.to_dict('records'))

        serializer = ProductSerializer(data=df.to_dict('records'), many=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data imported successfully"})

        else:
            return Response(serializer.errors, status=400)




class Total_Calculate(APIView):
    def get(self, request):
        obj = Product.objects.aggregate(total_sum= Sum('price'))
        return Response(data=obj, status=200)


class ProductUpdateView(APIView):
    def put(self, request, pk):
        obj = Product.objects.get(id=pk)
        serializers = ProductSerializer(data=request.data, instance=obj, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response(data=serializers.data, status=200)
        return Response(data=serializers.errors, status=404)



