from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Student, Teacher, Mark
from django.db.models import Sum

# ===========================
# AUTHENTICATION VIEWS
# ===========================
def home(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return render(request, "login.html")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successfully")
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

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return render(request, "register.html")

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "register.html")

        User.objects.create_user(username=username, email=email, password=password1)
        messages.success(request, "Account created successfully. Please login.")
        return redirect("login")

    return render(request, "register.html")


@login_required
def logout(request):
    return redirect("login")


# ===========================
# DASHBOARD
# ===========================
@login_required
def dashboard(request):
    return render(request, "dashboard.html", {
        "total_students": Student.objects.count(),
        "total_teachers": Teacher.objects.count(),
    })


# ===========================
# STUDENT VIEWS
# ===========================
@login_required
def student_register(request):
    if request.method == "POST":
        Student.objects.create(
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
            father_firstname=request.POST.get("father_firstname"),
            father_lastname=request.POST.get("father_lastname"),
            father_phone=request.POST.get("father_phone"),
            father_email=request.POST.get("father_email"),
            father_national_id=request.POST.get("father_national_id"),
            father_occupation=request.POST.get("father_occupation"),
            mother_firstname=request.POST.get("mother_firstname"),
            mother_lastname=request.POST.get("mother_lastname"),
            mother_phone=request.POST.get("mother_phone"),
            mother_email=request.POST.get("mother_email"),
            mother_national_id=request.POST.get("mother_national_id"),
            mother_occupation=request.POST.get("mother_occupation"),
        )
        return redirect("dashboard")

    return render(request, "registration.html")


@login_required
def student_list(request):
    query = request.GET.get("q")
    if query:
        students = Student.objects.filter(student_firstname__icontains=query)
    else:
        students = Student.objects.all()

    return render(request, "student_list.html", {"students": students})


@login_required
def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, "student_detail.html", {"student": student})


@login_required
def edit_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == "POST":
        student.student_firstname = request.POST.get("student_firstname")
        student.student_lastname = request.POST.get("student_lastname")
        student.student_class = request.POST.get("student_class")
        student.save()
        return redirect("student_list")

    return render(request, "edit_student.html", {"student": student})


@login_required
def delete_student(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    student.delete()
    return redirect("student_list")


# ===========================
# TEACHER VIEWS
# ===========================
@login_required
def teacher_register(request):
    if request.method == "POST":
        Teacher.objects.create(
            firstname=request.POST.get("firstname"),
            lastname=request.POST.get("lastname"),
            phone=request.POST.get("phone"),
            email=request.POST.get("email"),
            subject=request.POST.get("subject")
        )
        return redirect("teacher_list")

    return render(request, "teacher_register.html")


@login_required
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, "teacher_list.html", {"teachers": teachers})


@login_required
def edit_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    if request.method == "POST":
        teacher.firstname = request.POST.get("firstname")
        teacher.lastname = request.POST.get("lastname")
        teacher.phone = request.POST.get("phone")
        teacher.email = request.POST.get("email")
        teacher.subject = request.POST.get("subject")
        teacher.save()
        return redirect("teacher_list")

    return render(request, "edit_teacher.html", {"teacher": teacher})


@login_required
def delete_teacher(request, id):
    teacher = get_object_or_404(Teacher, id=id)
    teacher.delete()
    return redirect("teacher_list")


# ===========================
# MARKS VIEWS
# ===========================
@login_required
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
            total_marks=request.POST.get("total_marks"),
            mark_type=request.POST.get("mark_type")
        )
        return redirect("mark_entry")

    return render(request, "mark_entry.html", {
        "students": students,
        "teachers": teachers
    })


@login_required
def student_report(request, student_id, term='Term 1'):
    student = get_object_or_404(Student, id=student_id)
    marks = Mark.objects.filter(student=student, term=term)

    # Calculate percent
    for m in marks:
        m.percent = round((m.marks / m.total_marks) * 100, 2)

    quiz_marks = marks.filter(mark_type='Quiz')
    exam_marks = marks.filter(mark_type='Exam')

    total_scored = sum(m.marks for m in marks)
    total_possible = sum(m.total_marks for m in marks)
    overall_percent = round((total_scored / total_possible * 100) if total_possible > 0 else 0, 2)

    # Position in class
    class_marks = Mark.objects.filter(student__student_class=student.student_class, term=term)
    student_totals = {}
    for m in class_marks:
        student_totals[m.student.id] = student_totals.get(m.student.id, 0) + m.marks
    sorted_students = sorted(student_totals.items(), key=lambda x: x[1], reverse=True)
    position = next((i+1 for i, s in enumerate(sorted_students) if s[0] == student.id), None)
    class_total = len(student_totals)

    # Promotion check after Term 3
    promotion_status = None
    if term == 'Term 3':
        all_marks = Mark.objects.filter(student=student)
        total_scored_all = sum(m.marks for m in all_marks)
        total_possible_all = sum(m.total_marks for m in all_marks)
        overall_all_percent = (total_scored_all / total_possible_all * 100) if total_possible_all > 0 else 0
        promotion_status = "Promoted to next class" if overall_all_percent >= 50 else "Repeated the same class"

    return render(request, "student_report.html", {
        "student": student,
        "quiz_marks": quiz_marks,
        "exam_marks": exam_marks,
        "overall_percent": overall_percent,
        "term": term,
        "promotion_status": promotion_status,
        "position": position,
        "class_total": class_total
    })


# ===========================
# PARENT PORT
# ===========================
def parent_port(request):
    context = {}
    if request.method == "POST":
        code = request.POST.get('student_code')
        student = Student.objects.filter(student_code=code).first()
        if student:
            return render(request, 'parent_report.html', {'student': student})
        else:
            context['error'] = "Invalid student code."
    return render(request, 'parent.html', context)


def parent_report(request):
    code = request.GET.get('student_code')
    student = get_object_or_404(Student, student_code=code)

    terms = ['Term 1', 'Term 2', 'Term 3']
    term_reports = []

    for term in terms:
        marks = Mark.objects.filter(student=student, term=term)
        for m in marks:
            m.percent = round((m.marks / m.total_marks) * 100, 2)
        quiz_marks = marks.filter(mark_type='Quiz')
        exam_marks = marks.filter(mark_type='Exam')
        total_scored = sum(m.marks for m in marks)
        total_possible = sum(m.total_marks for m in marks)
        overall_percent = round((total_scored / total_possible * 100) if total_possible > 0 else 0, 2)
        term_reports.append({
            "term": term,
            "quiz_marks": quiz_marks,
            "exam_marks": exam_marks,
            "overall_percent": overall_percent
        })

    all_marks = Mark.objects.filter(student=student)
    total_scored_all = sum(m.marks for m in all_marks)
    total_possible_all = sum(m.total_marks for m in all_marks)
    overall_all_percent = (total_scored_all / total_possible_all * 100) if total_possible_all > 0 else 0
    promotion_status = "Promoted to next class" if overall_all_percent >= 50 else "Repeated the same class"

    return render(request, 'parent_report.html', {
        "student": student,
        "term_reports": term_reports,
        "promotion_status": promotion_status
    })
