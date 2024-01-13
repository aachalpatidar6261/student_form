# marksheet_app/tables.py
import django_tables2 as tables
from .models import Student

class StudentTable(tables.Table):
    class Meta:
        model = Student
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ('name', 'roll_no', 'subject1', 'subject2', 'subject3', 'subject4', 'subject5', 'score1', 'score2', 'score3', 'score4', 'score5', 'student_class')
