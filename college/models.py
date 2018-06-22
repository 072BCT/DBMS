import datetime

from django.db import models

# pw - dbms1234


Degree_Choices = {('PhD', 'PhD'), ('MSc', 'MSc'), ('Bachelors', 'Bachelors'), ('Diploma', 'Diploma')}
Affiliation_Choices = {('Permanent', 'Permanent'), ('Contract', 'Contract'), ('Visiting', 'Visiting')}
Position_Choices = {('Prof Dr.', 'Prof Dr'), ('Dr.', 'Dr')}


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
    first_name = models.CharField(max_length=40, )
    middle_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40, )
    salutation = models.CharField(max_length=40, choices=Position_Choices, blank=True)
    mobile_phone = models.CharField(max_length=20, blank=True)
    home_phone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    upper_degree = models.CharField(max_length=30, choices=Degree_Choices, default='MSc')

    class Meta:
        abstract = True

    def full_name(self):
        return str(self.salutation + ' ' + self.first_name + ' ' + self.middle_name + ' ' + self.last_name)

    def __str__(self):
        return self.full_name()


class AffiliatedInstitute(models.Model):
    institute_name = models.CharField(max_length=20, blank=True)
    code = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.institute_name


class Teacher(HumanResource):
    teacher_id = models.CharField(max_length=20, blank=True, null=False)
    known_subjects = models.ManyToManyField('Subject', blank=True)
    aff_type = models.CharField(max_length=30, choices=Affiliation_Choices, default='Permanent')
    affiliated_institute = models.ForeignKey('AffiliatedInstitute', on_delete=models.DO_NOTHING)
    started_teaching = models.CharField(max_length=4, default=datetime.date.today().strftime("%Y"), blank=True)

    def get_teacher_id(self):
        return str(self.teacher_id)

    def get_teacher_experience_years(self):
        if self.started_teaching:
            return int(datetime.date.today().strftime("%Y")) - int(self.started_teaching)
        else:
            return ""


class Subject(models.Model):
    name = models.CharField(max_length=40, blank=True, null=True)
    elective = models.BooleanField(default=0)
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
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Expert(HumanResource):
    organization = models.ForeignKey('AffiliatedInstitute', on_delete=models.DO_NOTHING)
    topic = models.ManyToManyField(Topic)
