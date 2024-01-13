# marksheet_app/views.py
from django.shortcuts import render, redirect
from django_tables2 import RequestConfig
from .forms import StudentForm
from .models import Student
from .tables import StudentTable

# marksheet_app/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .serializers import StudentSerializer

class GetStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Student.objects.all()

        # Apply class filter if provided
        student_class = self.request.query_params.get('class', None)
        if student_class is not None:
            queryset = queryset.filter(student_class=student_class)

        return queryset




def student_list(request):
    table = StudentTable(Student.objects.all())
    RequestConfig(request, paginate={'per_page': 10}).configure(table)

    return render(request, 'student_list.html', {'table': table})

def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            msg="Data Sumbited!"
            return render(request, 'add_student.html', {'msg': msg})
  # Create a success page or redirect as needed
    else:
        form = StudentForm()

    return render(request, 'add_student.html', {'form': form})
