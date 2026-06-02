from django.urls import path
from . import views
app_name='equipments'
urlpatterns=[
    path('',views.equipment_list,name='equipment_list'),
    path('<int:pk>/',views.equipment_detail,name='equipment_detail'),
    path('new/',views.equipment_create,name='equipment_create'),
    path('<int:pk>/edit/',views.equipment_edit,name='equipment_edit'),
    path('<int:pk>/failure/',views.report_failure,name='report_failure'),
]
