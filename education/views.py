from django.shortcuts import render, get_object_or_404 , redirect
from .models import Subscribers, Enrolling_to_course, Teachers, Our_courses, Contact_us, Descriptions_about_us

def index(request):

    name = request.POST.get('name')
    subject = request.POST.get('subject')
    surname = request.POST.get('surname')
    number = request.POST.get('phone')
    
    if request.method == "POST":
        Enrolling_to_course.objects.create(name=name , surname=surname , phone_number=number , selected_courses = subject, is_active = False)
    
    
    
    descriptions_about_us = Descriptions_about_us.objects.all()[:5]    
    our_courses = Our_courses.objects.all()[:4]
    teachers = Teachers.objects.all()[:4]
    
    ctx = {
        'our_courses ':our_courses ,
        'teachers ':teachers ,
        'descriptions_about_us':descriptions_about_us
    }
    
    return render(request, 'index.html' , ctx)


def about(request):
    descriptions_about_us = Descriptions_about_us.objects.all()[:5]    
    
    ctx = {
        'descriptions_about_us':descriptions_about_us
    }
    
    return render(request, 'about.html' , ctx)

def courses(request):
    our_courses = Our_courses.objects.all()
    
    ctx = {
        'our_courses ':our_courses[8:] ,

    }
    
    return render(request, 'courses.html' , ctx)

def teachers(request):
    teachers = Teachers.objects.all()
    
    ctx = {
        'teachers':teachers
    }

    return render(request, 'teacher.html', ctx)
def contact(request):
    
    name = request.POST.get('name')
    phone_number = request.POST.get('phone_number')
    message = request.POST.get('message')
    
    if request.method == "POST":
        Contact_us.objects.create(name=name ,phone_number=phone_number , message=message, is_active = False)
        
    return render(request, 'contact.html')
