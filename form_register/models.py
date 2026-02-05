from django.db import models


# =====================
# STUDENT MODEL
# =====================
class Student(models.Model):

    CLASS_CHOICES = [
        ('S1', 'Senior 1'),
        ('S2', 'Senior 2'),
        ('S3', 'Senior 3'),
        ('S4', 'Senior 4'),
        ('S5', 'Senior 5'),
        ('S6', 'Senior 6'),
    ]

    # Student Information
    student_firstname = models.CharField(max_length=100)
    student_lastname = models.CharField(max_length=100)

    student_class = models.CharField(
        max_length=2,
        choices=CLASS_CHOICES,
        default='S1'
    )

    student_dob = models.DateField()
    student_email = models.EmailField(blank=True, null=True)
    student_national_id = models.BigIntegerField(unique=True)
    student_phone = models.BigIntegerField()
    student_address = models.CharField(max_length=255)

    primary_school = models.CharField(max_length=150, blank=True, null=True)
    secondary_school = models.CharField(max_length=150, blank=True, null=True)

    # Father Information
    father_firstname = models.CharField(max_length=100)
    father_lastname = models.CharField(max_length=100)
    father_phone = models.BigIntegerField()
    father_email = models.EmailField(blank=True, null=True)
    father_national_id = models.BigIntegerField(blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)

    # Mother Information
    mother_firstname = models.CharField(max_length=100)
    mother_lastname = models.CharField(max_length=100)
    mother_phone = models.BigIntegerField()
    mother_email = models.EmailField(blank=True, null=True)
    mother_national_id = models.BigIntegerField(blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student_firstname} {self.student_lastname} ({self.student_class})"


# =====================
# TEACHER MODEL
# =====================
class Teacher(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    email = models.EmailField(blank=True, null=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


# =====================
# MARKS MODEL
# =====================
class Mark(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)
    subject = models.CharField(max_length=100)
    marks = models.IntegerField()
    term = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
