from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_no = models.CharField(max_length=20, unique=True)
    subject1 = models.CharField(max_length=50)
    subject2 = models.CharField(max_length=50)
    subject3 = models.CharField(max_length=50)
    subject4 = models.CharField(max_length=50)
    subject5 = models.CharField(max_length=50)
    score1 = models.IntegerField()
    score2 = models.IntegerField()
    score3 = models.IntegerField()
    score4 = models.IntegerField()
    score5 = models.IntegerField()
    image = models.ImageField(upload_to='student_images/')
    student_class = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 13)])

    def __str__(self):
        return self.name + " : " + str(self.score1 + self.score2 + self.score3 + self.score4 + self.score5)
    
    def total_score(self):
        return self.score1 + self.score2 + self.score3 + self.score4 + self.score5
