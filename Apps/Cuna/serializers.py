from rest_framework import serializers
from .models.Student import Student
from .models.Teacher import Teacher
from .models.Course import Course
from .models.Announcement import Announcement
from .models.Inscription import Inscription
from .models.Proxy import Proxy
from .models.Workload import Workload
from .models.YearCourse import YearCourse
from .models.Grade import Grade
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.proxy:
            representation['proxy_display'] = str(instance.proxy)
        else:
            representation['proxy_display'] = 'Sin apoderado'
        return representation

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified', 'full_name')  # Assuming full_name is a read-only field in the Teacher model
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__' 
        read_only_fields = ('id', 'created', 'modified') 

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')       

class InscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inscription
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')

class ProxySerializer(serializers.ModelSerializer):
    class Meta:
        model = Proxy
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')  

class WorkloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workload
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')  

class YearCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = YearCourse
        fields = '__all__' 
        read_only_fields = ('id', 'created', 'modified')    


from .models.Grade import Grade

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='inscription.student.names', read_only=True)
    course_name = serializers.CharField(source='inscription.workload.year_course.name', read_only=True)
    teacher_name = serializers.CharField(source='inscription.workload.teacher', read_only=True)
    percentage_score = serializers.ReadOnlyField()
    
    class Meta:
        model = Grade
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified', 'percentage_score')

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')
    
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise serializers.ValidationError('Credenciales inválidas')
            if not user.is_active:
                raise serializers.ValidationError('Usuario desactivado')
            attrs['user'] = user
        else:
            raise serializers.ValidationError('Username y password requeridos')
        
        return attrs
    

class UserListSerializer(serializers.ModelSerializer):
    """Serializer para listar usuarios con información básica"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                 'is_active', 'date_joined', 'last_login')
        read_only_fields = ('id', 'date_joined', 'last_login')

class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer para ver detalles completos de un usuario"""
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 
                 'is_active', 'is_staff', 'date_joined', 'last_login')
        read_only_fields = ('id', 'date_joined', 'last_login', 'is_staff')