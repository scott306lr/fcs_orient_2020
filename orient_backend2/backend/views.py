from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import GroupsinfoSerializer, HintsSerializer, HintSerializer, GroupsSerializer, OthersSerializer, LoggingSerializer
from .models import Groupsinfo, Hints, Hint, Groups, Others, Logging


class GroupsinfoViewSet(viewsets.ModelViewSet):
    model = Groupsinfo
    queryset = Groupsinfo.objects.all().order_by('id')
    serializer_class = GroupsinfoSerializer

    # def post(self, request, *args, **kwargs):
    #      pass


class HintsViewSet(viewsets.ModelViewSet):
    queryset = Hints.objects.all()
    serializer_class = HintsSerializer

class HintViewSet(viewsets.ModelViewSet):
    queryset = Hint.objects.all().order_by('id')
    serializer_class = HintSerializer

class GroupsViewSet(viewsets.ModelViewSet):
    queryset = Groups.objects.all().order_by('id')
    serializer_class = GroupsSerializer

    # def post(self, request, *args, **kwargs):
    #     group_data = request.data
    #     new_group = Groups.objects.create(id=group_data["id"], score=group_data["score"], name=group_data["name"])
    #     new_group.save()
    #     serializer = GroupsSerializer(new_group)
    #     return Response(serializer.data)
    #     testmodel = self.get_object(pk) 
    #     serializer = GroupsSerializer(testmodel, data=request.data, partial=True) # set partial=True to update a data partially 
    #     if serializer.is_valid(): 
    #         serializer.save() 
    #     return JsonReponse(code=201, data=serializer.data) 
    #     return JsonResponse(code=400, data="wrong parameters") 
    
class OthersViewSet(viewsets.ModelViewSet):
    queryset = Others.objects.all()
    serializer_class = OthersSerializer

class LoggingViewSet(viewsets.ModelViewSet):
    queryset = Logging.objects.all()
    serializer_class = LoggingSerializer

