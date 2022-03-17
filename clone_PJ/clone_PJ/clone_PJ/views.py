from django.shortcuts import render
from rest_framework.views import APIView

# Create your views here.

class Sub(APIView):
    def get(self, request):
        print("GET !!!")
        return render(request,"main.html")

    def post(self, request):
        print("POST !!!")
        return render(request,"main.html")