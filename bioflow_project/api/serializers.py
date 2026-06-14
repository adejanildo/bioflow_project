from rest_framework import serializers
from reagents.models import Reagent
from equipments.models import Equipment
from experiments.models import Experiment
from schedules.models import Schedule
from samples.models import Sample
from analysis.models import Analysis

class ReagentSerializer(serializers.ModelSerializer):
    is_expired = serializers.SerializerMethodField()
    is_low_stock = serializers.SerializerMethodField()
    class Meta:
        model=Reagent
        fields='__all__'
    def get_is_expired(self,obj): return obj.is_expired()
    def get_is_low_stock(self,obj): return obj.is_low_stock()

class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Equipment
        fields='__all__'

class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Experiment
        fields='__all__'

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Schedule
        fields='__all__'

class SampleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Sample
        fields='__all__'

class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model=Analysis
        fields='__all__'
