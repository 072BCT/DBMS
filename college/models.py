from django.db import models

#pw - dbms1234
# Create your models here.

class Programme(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name

class Batch(models.Model):
    programme = models.ForeignKey(Programme, on_delete= models.DO_NOTHING)
    no_stud = models.IntegerField()

class Semester(models.Model):
    batch = models.ForeignKey(Batch, on_delete= models.CASCADE)
    year = models.CharField(max_length=10)
    part = models.CharField(max_length=10)

class Course(models.Model):
    semester = models.ForeignKey(Semester, on_delete= models.CASCADE)
    int_marks = models.IntegerField()
    ext_marks = models.IntegerField()
    total_marks = models.IntegerField()
    # total_marks = int_marks + ext_marks

    # def total_marks(self):
    # return self.int_marks + self.ext_marks

class Teacher(models.Model):
    #programme = models.ForeignKey(Programme, on_delete= models.PROTECT)
    course = models.ForeignKey(Course, on_delete= models.PROTECT)
    name = models.CharField(max_length = 40)
    phone = models.CharField(max_length= 20)
    email = models.CharField(max_length=30)
    aff_campus = models.CharField(max_length=10)
    experience = models.IntegerField()
    exp_on_sub = models.IntegerField()
    upper_deg = models.CharField(max_length=20)
    aff_type = models.CharField(max_length=30)

    #(Permanent, Contract, Visiting)

class Topic(models.Model):
    course = models.ForeignKey(Course, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)

class Expert(models.Model):
    #programme = models.ForeignKey(Programme, on_delete= models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete= models.PROTECT)
    name = models.CharField(max_length = 40)
    phone = models.CharField(max_length= 20)
    email = models.CharField(max_length=30)
    aff_campus = models.CharField(max_length=10)
    upper_deg = models.CharField(max_length=20)
    aff_type = models.CharField(max_length=30)






