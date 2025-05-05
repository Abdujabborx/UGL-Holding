from django.db import models
from django.utils.timezone import now

class Course(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='courses/')
    uploaded_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title


class CourseSection(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='sections')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.course.title} - {self.title}"


class CourseContentBlock(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="content_blocks")
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(upload_to="course_blocks/", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title
