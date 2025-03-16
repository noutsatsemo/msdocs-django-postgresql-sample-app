from django.db.models import Avg, Count
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import cache_page
from rest_framework.parsers import JSONParser

from restaurant_review.models import Restaurant, Review
# Create your views here.


from restaurant_review.models import  Restaurant, Review, SillaUser, SillaProject
from restaurant_review.serializers import SillaUserSerializer, SillaProjectSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from restaurant_review.permissions import IsOwnerOrReadOnly



class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class SillaUserList(generics.ListCreateAPIView):
    queryset = SillaUser.objects.all()
    serializer_class = SillaUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



class SillaUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SillaUser.objects.all()
    serializer_class = SillaUserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]    



class SillaProjectList(generics.ListCreateAPIView):
    queryset = SillaProject.objects.all()
    serializer_class = SillaProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class SillaProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SillaProject.objects.all()
    serializer_class = SillaProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

