from django.db import models

# Create your models here.

class Pets(models.Model):
    gender_option = (('Male','Male'),('Female','Female'))
    type = (('D','Dog'),('C','Cat'))
    animal_type = models.CharField(max_length=30,choices = type,default='NA')
    name = models.CharField(max_length=30)
    species = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    gender = models.CharField(max_length=20,choices=gender_option)
    price = models.FloatField(default=0)
    image = models.ImageField(upload_to="Media")
    description = models.TextField(max_length=1000)




class student(models.Model):
    student_name = models.CharField(max_length=30)
    student_age = models.IntegerField()
    student_email = models.EmailField()
    student_location = models.CharField(max_length=50)
    student_course = models.CharField(max_length=100)
    
    
    
class author(models.Model):
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    title =models.CharField(max_length=100)
    author = models.ForeignKey(author, on_delete=models.CASCADE)

    
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    student = models.ManyToManyField(student)    
    


# username = Anas123
# password = itvedant123