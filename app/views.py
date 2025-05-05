from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from app.forms import RegistrationForm
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from .models import Course

def index(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # reload after successful registration
    else:
        form = RegistrationForm()

    # Get latest 3 courses
    courses = Course.objects.order_by('-id')[:3]  # or '-created_at' if you added that field

    return render(request, 'index.html', {'form': form, 'courses': courses})




def about(request):
    return render(request, 'about.html')




def home_view(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})





def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            
            full_message = f"Message from {name} <{email}>:\n\n{message}"
            send_mail(subject, full_message, email, ['your@email.com'])
            messages.success(request, 'Your message has been sent. Thank you!')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})



def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    content_blocks = course.content_blocks.filter(is_active=True) 
    sections = course.sections.all()  

    return render(request, 'course-details.html', {
        'course': course,
        'sections': sections,
        'content_blocks': content_blocks,
    })
