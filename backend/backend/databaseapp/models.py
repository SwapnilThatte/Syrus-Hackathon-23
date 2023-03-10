from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Job(models.Model):

    Job_id = models.AutoField(primary_key=True)
    Job_location = models.CharField(max_length=100)
    Language_preferences = models.CharField(max_length=20, choices=(()))
    Wages_per_hour = models.IntegerField(MinValueValidator(2000))
    Contract_tenure = models.DurationField()
    required_skills = models.TextField()
    Job_status = models.BooleanField(default=False)
    Employer_contact_number = models.CharField(max_length=20, blank=False)
    Number_of_vacancies = models.PositiveIntegerField(MinValueValidator(0))


class Complaint(models.Model):

    ComplaintID = models.AutoField(primary_key=True)
    Complaint_by = models.CharField(max_length=50)
    Complaint_of = models.CharField(max_length=50, blank=False)
    Complaint_description = models.CharField(max_length=300)
    Complaint_resolution_status = models.BooleanField(default=False)


# Create your models here.
class EmployerModel(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.IntegerField(max_length=8)
    pfp = models.ImageField(null=False, blank=False)
    aadharcard = models.ImageField(null=False, blank=False)

    def _str_(self):
        return self.emp_id + "" + str(self.name)


work_type = (('plumber', 'PLUMBER'),
             ('carpenter', 'CARPENTER'),
             ('labour', 'LABOUR'),
             )
loc = (
    ('mumbai', 'MUMBAI'),
    ('thane', 'THANE'),
    ('pune', 'PUNE'),
)

lang = (
    ('english', 'ENGLISH'),
    ('hindi', 'HINDI'),
    ('marathi', 'MARATHI'),
)


class Workers(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(null=False, blank=False)
    phone = models.CharField(max_length=10)
    Address = models.TextField()
    Adhaarcard = models.ImageField(null=False, blank=False)
    cityoforigin = models.CharField(max_length=20)
    medicalhistory = models.TextField()
    skills = models.CharField(max_length=100, choices=work_type, default=None)
    prefferedworklocation = models.CharField(
        max_length=100, choices=loc, default=None)
    languages = models.CharField(max_length=100, choices=lang, default=None)
