from django.db import models

class Subscribers(models.Model):
    email = models.EmailField(max_length=254)
    
    def __str__(self):
        return self.email

class We_have_courses(models.Model):
    course_name = models.CharField(max_length=225)
    
    def __str__(self):
        return self.course_name
    
    
class Enrolling_to_course(models.Model):
    name = models.CharField(max_length=225)
    surname = models.CharField(max_length=225)
    selected_courses = models.ManyToManyField(We_have_courses)
    phone_number = models.IntegerField()
    is_active = models.BooleanField(default=False)
    

    def __str__(self):
        return self.name
    

class Teachers(models.Model):
    name = models.CharField(max_length=225)
    teacher_photo = models.ImageField(upload_to='edu_images/')
    which_subjects = models.CharField(max_length=225)
    description = models.TextField()
    experience = models.IntegerField()
    
    def __str__(self):
        return self.name
    
    
class Our_courses(models.Model):
    teacher_name = models.ForeignKey(Teachers, on_delete=models.CASCADE)
    number_students = models.IntegerField()
    course_photo = models.ImageField(upload_to='edu_images/')
    course_name = models.ForeignKey(We_have_courses , on_delete=models.CASCADE)
    about_course = models.TextField()   
    
    def __str__(self):
        return self.course_name
    
    
class Contact_us(models.Model):
    name = models.CharField(max_length=225)
    phone_number = models.IntegerField()
    message = models.TextField()
    is_active = models.BooleanField(default=False)    
    
    def __str__(self):
        return self.name
    
     
class Descriptions_about_us(models.Model):
    WHO = (
        ('Father', 'Father'),
        ('Mother', 'Mother'),
        ('Sister' , 'Sister'),
        ('Brother', 'Brother'),
        ('Student', 'Student'),
    )

    name = models.CharField(max_length=50)
    who = models.CharField(choices=WHO, max_length=250, default='Student')
    descriptions = models.TextField()
    photo = models.ImageField(upload_to='edu_images/')
    
    def __str__(self):
        return self.name

    
    