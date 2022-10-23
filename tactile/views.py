from django.shortcuts import render
from django.views.generic import FormView
from .forms import *
from django.http import JsonResponse
from .models import textTo
from .serializers import TactileSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
class HomeView(FormView):
    form_class = UploadForm
    template_name = 'index.html'
    success_url = '/'

    def form_valid(self, form):
        upload = self.request.FILES['file']
        return super().form_valid(form)

def input_list(request):
    if request.method == 'GET':
        inputs = textTo.objects.all()
        serializer = TactileSerializer(inputs, many = True)
        return JsonResponse({"inputs": serializer.data})
    
    if request.method == 'POST':
        serializer = TactileSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)