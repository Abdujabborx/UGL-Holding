
from django.urls import path
from app.views import index, about, home_view, contact_view, course_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('courses/', home_view, name='courses'),
    path('contact/', contact_view, name='contact'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
