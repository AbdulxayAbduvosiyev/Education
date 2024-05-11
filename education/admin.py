from django.contrib import admin
from .models import Subscribers, We_have_courses, Enrolling_to_course, Teachers, Our_courses, Contact_us, Descriptions_about_us

@admin.register(Subscribers)
class SubscribersAdmin(admin.ModelAdmin):
    search_fields = ('id',  'email' )
    list_display = ('id', 'email')
    list_display_links = ('id', 'email')
    
@admin.register(We_have_courses)
class We_have_coursesdAdmin(admin.ModelAdmin):
    search_fields = ('id', 'course_name')
    list_display = ('id', 'course_name')
    list_display_links = ('id', 'course_name')

@admin.register(Enrolling_to_course)
class Enrolling_to_coursedAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'surname', 'selected_courses', 'is_active', 'phone_number' )
    list_display = ('id', 'name', 'phone_number')
    list_display_links = ('id', 'name', 'phone_number')

@admin.register(Teachers)
class TeachersAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'which_subjects', 'experience')
    list_display = ('id', 'name', 'which_subjects', 'experience')
    list_display_links = ('id', 'name', 'which_subjects', 'experience')
    
@admin.register(Our_courses)
class Our_coursesdAdmin(admin.ModelAdmin):
    search_fields = ('id', 'teacher_name')  
    list_display = ('id', 'course_name', 'teacher_name', 'number_students')
    list_display_links = ('id', 'teacher_name', 'number_students')
    
@admin.register(Contact_us)
class Contact_usdAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'phone_number', 'is_active')
    list_display = ('id', 'name', 'phone_number', 'is_active')
    list_display_links = ('id', 'name', 'phone_number', 'is_active')
    
@admin.register(Descriptions_about_us)
class We_have_coursesdAdmin(admin.ModelAdmin):
    search_fields = ('id', 'name', 'who')
    list_display = ('id', 'name', 'who')
    list_display_links = ('id', 'name', 'who')