from django.db import models
import random
import string

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
    student_class = models.CharField(max_length=10, choices=CLASS_CHOICES, default='S1')
    student_dob = models.DateField()
    student_email = models.EmailField(blank=True, null=True)
    student_national_id = models.BigIntegerField(unique=True)
    student_phone = models.BigIntegerField()
    student_address = models.CharField(max_length=255)

    primary_school = models.CharField(max_length=150, blank=True, null=True)
    secondary_school = models.CharField(max_length=150, blank=True, null=True)

    # Parent Information
    father_firstname = models.CharField(max_length=100)
    father_lastname = models.CharField(max_length=100)
    father_phone = models.BigIntegerField()
    father_email = models.EmailField(blank=True, null=True)
    father_national_id = models.BigIntegerField(blank=True, null=True)
    father_occupation = models.CharField(max_length=100, blank=True, null=True)

    mother_firstname = models.CharField(max_length=100)
    mother_lastname = models.CharField(max_length=100)
    mother_phone = models.BigIntegerField()
    mother_email = models.EmailField(blank=True, null=True)
    mother_national_id = models.BigIntegerField(blank=True, null=True)
    mother_occupation = models.CharField(max_length=100, blank=True, null=True)

    # Unique student code: 6 numbers + 4 letters
    student_code = models.CharField(max_length=10, unique=True, editable=False)
    
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.student_code:
            self.student_code = self.generate_unique_code()
        super().save(*args, **kwargs)

    def generate_unique_code(self):
        """
        Generate a unique code in the format: 6 digits + 4 uppercase letters
        """
        while True:
            numbers = ''.join(random.choices(string.digits, k=6))
            letters = ''.join(random.choices(string.ascii_uppercase, k=4))
            code = numbers + letters
            if not Student.objects.filter(student_code=code).exists():
                return code

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
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    term = models.CharField(max_length=50)
    marks = models.FloatField()
    total_marks = models.FloatField()
    mark_type = models.CharField(
        max_length=10,
        choices=[('Quiz','Quiz'),('Exam','Exam')],
        default='Exam'
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.subject}"
