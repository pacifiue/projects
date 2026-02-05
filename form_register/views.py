from django.shortcuts import render, redirect ,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse
from .models import Student, Teacher, Mark
def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 1. Check if user exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return render(request, "login.html")

        # 2. Authenticate (check password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,"login sucessfully")
            return redirect("dashboard")
        else:
            messages.error(request, "Incorrect password")

    return render(request, "login.html")



def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # 1. Passwords must match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        # 2. Username must be unique
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")

        # 3. Email must be unique
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "register.html")

        # 4. Create user (stored in DB)
        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")
def dashboard(request):
    return render(request,"dashboard.html")

def logout(request):
   return redirect('login')
def student_register(request):
    if request.method == "POST":
        Student.objects.create(
            # Student
            student_firstname=request.POST.get("student_firstname"),
            student_lastname=request.POST.get("student_lastname"),
            student_dob=request.POST.get("student_dob"),
            student_email=request.POST.get("student_email"),
            student_national_id=request.POST.get("student_national_id"),
            student_phone=request.POST.get("student_phone"),
            student_address=request.POST.get("student_address"),
            primary_school=request.POST.get("primary_school"),
            secondary_school=request.POST.get("secondary_school"),
            student_class=request.POST.get("student_class"),

            # Father
            father_firstname=request.POST.get("father_firstname"),
            father_lastname=request.POST.get("father_lastname"),
            father_phone=request.POST.get("father_phone"),
            father_email=request.POST.get("father_email"),
            father_national_id=request.POST.get("father_national_id"),
            father_occupation=request.POST.get("father_occupation"),

            # Mother
            mother_firstname=request.POST.get("mother_firstname"),
            mother_lastname=request.POST.get("mother_lastname"),
            mother_phone=request.POST.get("mother_phone"),
            mother_email=request.POST.get("mother_email"),
            mother_national_id=request.POST.get("mother_national_id"),
            mother_occupation=request.POST.get("mother_occupation"),
        )

        return redirect("dashboard")  # change if needed

    return render(request, "registration.html")

def dashboard(request):
    return render(request, "dashboard.html", {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
    })

def student_list(request):
    query = request.GET.get("q")
    if query:
        students = Student.objects.filter(
            student_firstname__icontains=query
        )
    else:
        students = Student.objects.all()

    return render(request, "student_list.html", {"students": students})


def delete_student(request, id):
    student = get_object_or_404(Student, id=id)
    student.delete()
    return redirect("student_list")


def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == "POST":
        student.student_firstname = request.POST["student_firstname"]
        student.student_lastname = request.POST["student_lastname"]
        student.student_class = request.POST["student_class"]
        student.save()
        return redirect("student_list")

    return render(request, "edit_student.html", {"student": student})


def teacher_register(request):
    if request.method == "POST":
        Teacher.objects.create(
            firstname=request.POST["firstname"],
            lastname=request.POST["lastname"],
            phone=request.POST["phone"],
            email=request.POST["email"],
            subject=request.POST["subject"]
        )
        return redirect("teacher_list")

    return render(request, "teacher_register.html")

def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)  # Get the teacher by ID

    if request.method == "POST":
        # Update the teacher's fields from the form
        teacher.firstname = request.POST.get("firstname")
        teacher.lastname = request.POST.get("lastname")
        teacher.phone = request.POST.get("phone")
        teacher.email = request.POST.get("email")
        teacher.subject = request.POST.get("subject")
        teacher.save()  # Save changes to the database
        return redirect("teacher_list")  # Redirect to the teacher list page

    # If GET request, render the edit form
    return render(request, "edit_teacher.html", {"teacher": teacher})

def delete_teacher(request, id):
    # Get the teacher by ID, or return 404 if not found
    teacher = get_object_or_404(Teacher, id=id)

    # Delete the teacher
    teacher.delete()

    # Redirect back to the teacher list
    return redirect("teacher_list")

def student_detail(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, "student_detail.html", {"student": student})

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})

def student_report(request, id):
    student = get_object_or_404(Student, id=id)
    marks = Mark.objects.filter(student=student)

    return render(request, "student_report.html", {
        "student": student,
        "marks": marks
    })

def mark_entry(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    if request.method == "POST":
        Mark.objects.create(
            student_id=request.POST.get("student"),
            teacher_id=request.POST.get("teacher"),
            subject=request.POST.get("subject"),
            term=request.POST.get("term"),
            marks=request.POST.get("marks"),
        )
        return redirect("mark_entry")

    return render(request, "mark_entry.html", {
        "students": students,
        "teachers": teachers
    })

