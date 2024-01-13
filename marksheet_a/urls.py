from django.urls import path
from . import views
from .views import GetStudentsView


urlpatterns = [
    path('',views.add_student,name='add_student'),
    path('list/',views.student_list, name='student_list'),
    path('getstudents/', GetStudentsView.as_view(), name='get_students'),
]
