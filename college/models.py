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

    def getyearpart(self):
        if self.name == "First":
            return "I/I"
        if self.name == "Second":
            return "I/II"
        if self.name == "Third":
            return "II/I"
        if self.name == "Fourth":
            return "II/II"

    def __str__(self):
        return self.name


class HumanResource(models.Model):
    name = models.CharField(max_length=40, default="", )
    phone = models.CharField(max_length=20, default="", blank=True)
    email = models.EmailField(max_length=30, default="", blank=True)
    affiliated_institute = models.CharField(max_length=10, default="PUL")
    started_teaching = models.CharField(max_length=4, default=datetime.date.today().strftime("%Y"), blank=True)
    upper_degree = models.CharField(max_length=30, choices=Degree_Choices, default='MSc')
    aff_type = models.CharField(max_length=30, choices=Affiliation_Choices, default='Permanent')

    class Meta:
        abstract = True


class Teacher(HumanResource):
    teacher_id = models.CharField(max_length=20, default=" ", blank=True, null=False)
    known_subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return self.name

    def get_name(self):
        return str(self.name)

    def get_teacher_id(self):
        return str(self.teacher_id)

    def get_teacher_experience_years(self):
        if self.started_teaching:
            return int(datetime.date.today().strftime("%Y")) - int(self.started_teaching)
        else:
            return ""


class Subject(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    program_code = models.CharField(max_length=40, blank=True, default=" ")
    program = models.ForeignKey(Programme, on_delete=models.CASCADE, null=True)
    semester = models.ForeignKey(Semester, on_delete=models.CASCADE)
    subject_teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject_teacher_teaching_experience_years = models.CharField(max_length=4, blank=True)
    int_marks = models.IntegerField(default="4")
    int_marks = models.IntegerField(default="40")

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