from rest_framework import serializers
from courses.models import Course, Teacher, Student, CourseStudent


class CourseStudentShortSerializer(serializers.ModelSerializer):
    course_name = serializers.SerializerMethodField()

    class Meta:
        model = CourseStudent
        fields = ['course_name', ]


    def get_course_name(self, instance):
        return instance.course.name


class CourseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name']


class TeacherSerializer(serializers.ModelSerializer):
    courses = CourseShortSerializer(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ['id', 'name', 'courses']


class TeacherShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['name']


class StudentSerializer(serializers.ModelSerializer):
    courses = serializers.SerializerMethodField()

    class Meta:
        model = Student
        fields = ['id', 'name', 'courses']

    def get_courses(self, instance):
        courses = CourseStudent.objects.filter(
            student=instance
        )

        return CourseStudentShortSerializer(courses, many=True).data


class StudentShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Student
        fields = ['name']


class CourseSerializer(serializers.ModelSerializer):
    teacher = TeacherShortSerializer()
    students = StudentShortSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'name', 'teacher', 'students']
