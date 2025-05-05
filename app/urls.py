
from django.urls import path
from app.views import index, about, login_view, home_view, logout_view, contact_view, course_detail

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('login/', login_view, name='login'),
    path('courses/', home_view, name='courses'),
    path('logout/', logout_view, name='logout'),
    path('contact/', contact_view, name='contact'),
    path('course/<int:course_id>/', course_detail, name='course_detail'),
]
