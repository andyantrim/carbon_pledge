from tasks.models import Tasks
from rest_framework import serializers


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tasks
        fields = ('title', 'description', 'image_link', 'created_by', 'active')