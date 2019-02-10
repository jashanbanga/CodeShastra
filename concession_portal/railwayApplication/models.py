from django.db import models
from django.utils import timezone
# Create your models here.
class RailwayApplication(models.Model):
    # student info 
    student_photo = models.ImageField(upload_to='railway/students/%m/%d/')
    student_collegeId = models.CharField(max_length=255)
    student_emailId = models.EmailField()
    student_aadharId = models.CharField(max_length=255)
    student_fullname = models.CharField(max_length=1024)
    student_contact= models.CharField(max_length=100)
    student_dob = models.DateField()
    student_address = models.TextField()
    student_bonafide = models.FileField(upload_to='bonafides/%m/%d/')
    student_prevPassId = models.CharField(max_length=255, blank=True)

    # railway info 
    trainClasses = (
        ('First', 'First Class'),
        ('Second', 'Second Class')
    )
    source_station = models.CharField(max_length=255)
    destination_station = models.CharField(max_length=255)
    train_class = models.CharField(choices=trainClasses, max_length=50)

    # application info 
    isApproved_railway = models.BooleanField(default=False)
    application_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.student_aadharId
