from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.participant.api.views import ParticipantApiViewset, TotalParticipantView, ExecuteLotteryView

router_participant = DefaultRouter()

router_participant.register(prefix='lottery/apps/participant', basename='lottery/apps/participant', viewset=ParticipantApiViewset)
router_participant.register(prefix='lottery/apps/total_participants', basename='lottery/apps/total_participants', viewset=TotalParticipantView)
router_participant.register(prefix='lottery/apps/execute', basename='lottery/apps/execute', viewset=ExecuteLotteryView)
