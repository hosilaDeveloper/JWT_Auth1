from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status, generics
from .models import Task
from .serializers import TaskSerializers
from rest_framework.permissions import IsAuthenticated


# Create your views here.


class TaskList(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        data = self.request.data
        data['author'] = self.request.user.id
        serializer = TaskSerializers(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializers
    permission_classes = (IsAuthenticated,)
