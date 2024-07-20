from django.urls import path,include
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('addemp',views.addemp,name='addemp'),
    path('delemp',views.delemp,name='delemp'),
    path('delemp/<int:emp_id>',views.delemp,name='delemp'),
    path('editemp',views.editemp,name='editemp'),
    path('viewemp',views.viewemp,name='viewemp'),   
]
