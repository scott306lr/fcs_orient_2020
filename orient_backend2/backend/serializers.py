from rest_framework import serializers
from rest_framework.mixins import UpdateModelMixin

from .models import Groups
from .models import Groupsinfo
from .models import Hints
from .models import Hint
from .models import Others, Logging

class HintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hint
        fields = ('id', 'hint_type', 'hint_choices', 'difficulty', 'name', 'text', 'answer', 'basic_score', 'bonus_score', 'penalty', 'where')

class HintsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hints
        fields = "__all__"
        
    def update(self, instance, validated_data):
        instance.done = validated_data.get('done', instance.done)
        instance.avail = validated_data.get('avail', instance.avail)
        instance.done_by = validated_data.get('done_by', instance.done_by)
        instance.save()
        return instance

class GroupsinfoSerializer(serializers.ModelSerializer):
    hints = HintsSerializer(read_only=False, many=True)
    class Meta:
        model = Groupsinfo
        fields = ['id', 'hints']

    def create(self, validated_data):
        hints_data = validated_data.pop('hints')
        groupsinfo = Groupsinfo.objects.create(**validated_data)
        for hint_data in hints_data:
            Hints.objects.create(groupsinfo=groupsinfo, **hint_data)
        return groupsinfo
    
class GroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groups
        fields = ['id', 'score', 'name']
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.score = validated_data.get('score', instance.score)
        instance.save()
        return instance

    # def create(self, validated_data):
    #     groups_data = validated_data.pop('name')
    #     groups = Groups.objects.create(**validated_data)
    #     for group_data in groups_data:
    #         Groups.objects.create(groups=groups, **group_data)
    #     return groups

    # def post(self, request, *args, **kwargs):
    #     group_data = request.data
    #     new_group = Groups.objects.create(id=group_data["id"], score=group_data["score"], name=group_data["name"])
    #     new_group.save()
    #     serializer = GroupsSerializer(new_group)
    #     return Response(serializer.data)

class OthersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Others
        fields = "__all__"
    
class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Logging
        fields = "__all__"
    def update(self, instance, validated_data):
        instance.group_id = validated_data.get('group_id', instance.group_id)
        instance.reason = validated_data.get('reason', instance.reason)
        instance.fin_time = validated_data.get('fin_time', instance.fin_time)
        instance.cur_score = validated_data.get('cur_score', instance.cur_score)
        instance.get_score = validated_data.get('get_score', instance.get_score)
        instance.save()
        return instance



