import datetime
from django.db import models


# pw - dbms1234


Degree_Choices = {('PhD', 'PhD'), ('MSc', 'MSc'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma')}
Affiliation_Choices = {('Permanent', 'Permanent'), ('Contract', 'Contract'), ('Visiting', 'Visiting')}


class Programme(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Batch(models.Model):
    year = models.CharField(max_length=40, default=datetime.date.today().strftime("%Y"))
    programme = models.ForeignKey(Programme, on_delete=models.DO_NOTHING)
    number_of_students = models.IntegerField(default='48')

    def __str__(self):
        return self.programme.name + " : " + self.year


class Semester(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    # programme = models.ForeignKey(Programme, on_delete= models.PROTECT)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    affiliated_institute = models.CharField(max_length=10)
    teaching_experience_years = models.IntegerField(default='1')

    upper_degree = models.CharField(max_length=30, choices=Degree_Choices, default='MSc')
    aff_type = models.CharField(max_length=30, choices=Affiliation_Choices, default='Permanent')


class Subject(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    program = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=True)
    program_code = models.CharField(max_length=40, blank=True, null=True)
    int_marks = models.IntegerField(default="4")
    int_marks = models.IntegerField(default="40")
    ext_marks = models.IntegerField(default="60")

    # total_marks = int_marks + ext_marks

    # def total_marks(self):
    # return self.int_marks + self.ext_marks

    def __str__(self):
        return self.name + "  :  " + self.program.name + " - " + self.semester.name


class Topic(models.Model):
    course = models.ForeignKey(Subject, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)


class Expert(models.Model):
    # programme = models.ForeignKey(Programme, on_delete= models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    aff_campus = models.CharField(max_length=10)
    upper_degree = models.CharField(max_length=30, choices=Degree_Choices, default='MSc')
    aff_type = models.CharField(max_length=30, choices=Affiliation_Choices, default='Permanent')
