from django.contrib import admin
from django.contrib.auth.models import User
from .models import Course, CourseContentBlock

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'date_joined', 'is_active')
    search_fields = ('username', 'email')

class CourseContentBlockInline(admin.TabularInline):
    model = CourseContentBlock
    extra = 1

class CourseAdmin(admin.ModelAdmin):
    inlines = [CourseContentBlockInline]

admin.site.register(Course, CourseAdmin)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

