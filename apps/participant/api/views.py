import random
from rest_framework import status
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.response import Response
from apps.participant.models import Participant
from apps.participant.api.serializers import ParticipantSerializer


class ParticipantApiViewset(ModelViewSet):
    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
    http_methos_names = ['get', 'post']

    def list(self, request):
        winners = Participant.objects.filter(winner=True)
        winnersSerializer = self.serializer_class(data=winners, many=True)

        winnersSerializer.is_valid()

        return Response(status=status.HTTP_200_OK, data=winnersSerializer.data)

class TotalParticipantView(ViewSet):
    def list(self, request):
        total = Participant.objects.all().count()
        return Response(status=status.HTTP_200_OK, data=total) 

class ExecuteLotteryView(ViewSet):
    def create(self, request):
        participants = Participant.objects.all()
        total_winners = int(request.data['total_winner'])
        winners = random.sample(list(participants), total_winners)



        for winner in winners:
            participant = winner
            participant.winner = True
            participant.save()

        return Response(status=status.HTTP_200_OK, data={'result': '!Ganadores Generados'})    

