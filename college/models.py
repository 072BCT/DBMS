import datetime
from django.db import models
from datetime import date

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


class HumanResource(models.Model):
    name = models.CharField(max_length=40, default="", )
    phone = models.CharField(max_length=20, default="")
    email = models.EmailField(max_length=30, default="")
    affiliated_institute = models.CharField(max_length=10, default="PUL")
    started_teaching = models.CharField(max_length=4, default=datetime.date.today().strftime("%Y"))
    upper_degree = models.CharField(max_length=30, choices=Degree_Choices, default='MSc')
    aff_type = models.CharField(max_length=30, choices=Affiliation_Choices, default='Permanent')

    class Meta:
        abstract = True


class Teacher(HumanResource):
    int_marks = models.IntegerField(default="40")

    def __str__(self):
        return self.name


class Subject(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    program_code = models.CharField(max_length=40, blank=True, null=True)
    program = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, null=True, blank=True)
    subject_teacher_teaching_experience_years = models.CharField(max_length=4, blank=True, null=True)
    int_marks = models.IntegerField(default="4")
    int_marks = models.IntegerField(default="40")

    def get_subjet_teacher(self):
        return self.subject_teacher.name

    # total_marks = int_marks + ext_marks

    # def total_marks(self):
    # return self.int_marks + self.ext_marks

    def __str__(self):
        return self.program.name + " - " + self.semester.name + "  :  " + self.name


class Topic(models.Model):
    course = models.ForeignKey(Subject, on_delete=models.PROTECT)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Expert(HumanResource):
    topic = models.ManyToManyField(Topic)

    def __str__(self):
        return self.name
