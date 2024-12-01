from rest_framework.serializers import ModelSerializer
from apps.participant.models import Participant

class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant 
        fields = ['id', 'nick', 'email']
        reald_only_fields = ['winner']