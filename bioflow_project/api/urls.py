from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name='api'
router=DefaultRouter()
router.register('reagents',views.ReagentViewSet)
router.register('equipments',views.EquipmentViewSet)
router.register('experiments',views.ExperimentViewSet)
router.register('schedules',views.ScheduleViewSet)
router.register('samples',views.SampleViewSet)
router.register('analysis',views.AnalysisViewSet)
urlpatterns=[
    path('',views.api_overview,name='api_overview'),
    path('',include(router.urls)),
]
