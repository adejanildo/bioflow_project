from rest_framework import viewsets, filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from reagents.models import Reagent
from equipments.models import Equipment
from experiments.models import Experiment
from schedules.models import Schedule
from samples.models import Sample
from analysis.models import Analysis
from .serializers import *

class ReagentViewSet(viewsets.ModelViewSet):
    queryset=Reagent.objects.all()
    serializer_class=ReagentSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['name','lot','supplier']

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset=Equipment.objects.all()
    serializer_class=EquipmentSerializer
    filter_backends=[filters.SearchFilter]
    search_fields=['name','model','serial_number']

class ExperimentViewSet(viewsets.ModelViewSet):
    queryset=Experiment.objects.all()
    serializer_class=ExperimentSerializer

class ScheduleViewSet(viewsets.ModelViewSet):
    queryset=Schedule.objects.all()
    serializer_class=ScheduleSerializer

class SampleViewSet(viewsets.ModelViewSet):
    queryset=Sample.objects.all()
    serializer_class=SampleSerializer

class AnalysisViewSet(viewsets.ModelViewSet):
    queryset=Analysis.objects.all()
    serializer_class=AnalysisSerializer

@api_view(['GET'])
def api_overview(request):
    return Response({
        'BioFlow API': 'v1.0',
        'endpoints': {
            'reagents': '/api/reagents/',
            'equipments': '/api/equipments/',
            'experiments': '/api/experiments/',
            'schedules': '/api/schedules/',
            'samples': '/api/samples/',
            'analysis': '/api/analysis/',
        }
    })
