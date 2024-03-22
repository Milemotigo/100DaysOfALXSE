from django.shortcuts import render
from .forms import StudentForms
from .models import Student
from django.shortcuts import redirect
#from django.httpResponse import jsonResponse

def home(request):
    form = StudentForms(request.POST)
    students = Student.objects.all()

    context = {'students':students}
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

        return render(request, 'add.html', {'form':form})

def update_view(request):

    sudent = ''
    if request.method=='POST':
        id = request.POST.get('id')
        print(id)
        student = Student.objects.get(pk=id)
        form = StudentForms(request.POST, instance=student)
        student.name = request.POST.get('name')
        student.email = request.POST.get('email')
        student.course = request.POST.get('course')
        if form.is_valid():
            student.save()
        return redirect('home')
    else:
        id = request.POST.get('id')
        student = Student.objects.get(pk=id)
        form = StudentForms(instance=student)

    context = {'form':form}
    return render(request, 'core/update.html', context)

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
