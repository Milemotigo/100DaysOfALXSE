from django.shortcuts import render
from .forms import StudentForms
from .models import Student
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponseRedirect

def home(request):
    form = StudentForms(request.POST)
    students = Student.objects.all()

    context = {'students':students,
               'form':form
               }
    return render(request, 'core/add.html', context)

def add_view(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        course = request.POST.get('course')
        newStudent = Student.objects.create(name=name, email=email, course=course)
        newStudent.save()
        return redirect('home')
    else:
        student = StudentForms()

def update_student(request, id):
    student = get_object_or_404(Student, pk=id)
    if request.method == 'POST':
        form = StudentForms(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = StudentForms(instance=student)
    context = {
            'student':student,
            'form':form
            }
    return render(request, 'core/update2.html', context)

def delete_view(request):
    if request.method=='POST':
        id = request.POST.get('id')
        student = Student.objects.get(pk=id)
        if student:
            student.delete()
        return redirect('home')
    else:
        student = StudentForms()

        return student
