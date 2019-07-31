from rest_framework import serializers, viewsets, permissions
from .models import TeamData

class TeamDataSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = TeamData
        fields = ('map', 'team_score', 'team_position')
    
    def create(self, validated_data):
        team_data = TeamData.objects.create(**validated_data)
        return team_data

    def post(self):
        return "hello"

class TeamDataViewSet(viewsets.ModelViewSet):
    serializer_class = TeamDataSerializer
    queryset = TeamData.objects.all()
    permission_classes = [
    permissions.AllowAny
]
