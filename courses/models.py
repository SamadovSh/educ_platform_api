from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(
        'Teacher',
        related_name='courses', on_delete=models.CASCADE
    )
    students = models.ManyToManyField('Student', through='CourseStudent')

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class CourseStudent(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)


class Teacher(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

