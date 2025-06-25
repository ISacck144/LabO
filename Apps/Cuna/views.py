import json
from datetime import datetime
from django.shortcuts import render
from .models.Student import Student
from Apps.Cuna.models.Student import Student
from .models.Course import Course
from .models.Teacher import Teacher
from .models.Proxy import Proxy
from .models.Workload import Workload
from .models.YearCourse import YearCourse
from .models.Inscription import Inscription
from .models.Announcement import Announcement  # Asegúrate de importar Announcement
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models.Student import Student
from rest_framework.generics import ListCreateAPIView
from .models import Student
from .serializers import StudentSerializer
from .serializers import CourseSerializer, TeacherSerializer, WorkloadSerializer, ProxySerializer, YearCourseSerializer, AnnouncementSerializer, InscriptionSerializer  
from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer
from .models.Grade import Grade
from .serializers import GradeSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from .serializers import UserRegistrationSerializer, LoginSerializer
from django.http import HttpResponseBadRequest, JsonResponse
from .serializers import (
    CourseSerializer, ProxySerializer, WorkloadSerializer,
    TeacherSerializer, StudentSerializer, YearCourseSerializer,
    AnnouncementSerializer, InscriptionSerializer, GradeSerializer,
    UserRegistrationSerializer, LoginSerializer, UserListSerializer, UserDetailSerializer
)


class StudentsByWorkloadView(ListAPIView):
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        workload_id = self.kwargs['workload_id']
        return Student.objects.filter(inscription__workload_id=workload_id)
    
    def list(self, request, *args, **kwargs):
        workload_id = self.kwargs['workload_id']
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'👥 Estudiantes en la carga académica ID: {workload_id}',
            'workload_id': workload_id,
            'total_students': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })

class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'📋 Se encontraron {len(serializer.data)} estudiantes registrados',
            'total_count': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            student = serializer.save()
            return Response({
                'success': True,
                'message': f'✅ Estudiante {student.names} registrado exitosamente',
                'data': serializer.data,
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': '❌ Error al registrar estudiante',
            'errors': serializer.errors,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_400_BAD_REQUEST)

class TeacherListCreateView(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'👨‍🏫 Se encontraron {len(serializer.data)} docentes registrados',
            'total_count': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            teacher = serializer.save()
            return Response({
                'success': True,
                'message': f'✅ Docente {teacher.names} {teacher.father_surname} registrado exitosamente',
                'data': serializer.data,
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': '❌ Error al registrar docente',
            'errors': serializer.errors,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_400_BAD_REQUEST)
class ProxyListCreateView(generics.ListCreateAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer

class WorkloadListCreateView(generics.ListCreateAPIView):
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer
    permission_classes = [AllowAny]

class YearCourseListCreateView(generics.ListCreateAPIView):
    queryset = YearCourse.objects.all()
    serializer_class = YearCourseSerializer

class AnnouncementListCreateView(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer   

class InscriptionListCreateView(generics.ListCreateAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer
    permission_classes = [AllowAny]    

class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]    

class ProxyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Proxy.objects.all()
    serializer_class = ProxySerializer  

class WorkloadDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer
    permission_classes = [AllowAny]   

class YearCourseDetailView(generics.RetrieveUpdateDestroyAPIView):  
    queryset = YearCourse.objects.all()
    serializer_class = YearCourseSerializer 

class StudentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]
    
    def retrieve(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance)
            return Response({
                'success': True,
                'message': f'👤 Información del estudiante {instance.names}',
                'data': serializer.data,
                'timestamp': datetime.now().isoformat()
            })
        except Student.DoesNotExist:
            return Response({
                'success': False,
                'message': '❌ Estudiante no encontrado',
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_404_NOT_FOUND)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        
        if serializer.is_valid():
            serializer.save()
            action = '🔄 actualizado parcialmente' if partial else '✏️ actualizado completamente'
            return Response({
                'success': True,
                'message': f'Estudiante {instance.names} {action} exitosamente',
                'data': serializer.data,
                'timestamp': datetime.now().isoformat()
            })
        
        return Response({
            'success': False,
            'message': '❌ Error al actualizar estudiante',
            'errors': serializer.errors,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        student_name = f"{instance.names}"
        instance.delete()
        
        return Response({
            'success': True,
            'message': f'🗑️ Estudiante {student_name} eliminado exitosamente',
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_204_NO_CONTENT)



class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.select_related('proxy').all()
    serializer_class = StudentSerializer

class AnnouncementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer   

class InscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer
    permission_classes = [AllowAny]    

class CourseStatisticsView(APIView):
    """
    Vista para obtener estadísticas de cursos.
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        total_courses = Course.objects.count()
        active_courses = Course.objects.filter(status=True).count()
        inactive_courses = Course.objects.filter(status=False).count()
        
        statistics = {
            "total_courses": total_courses,
            "active_courses": active_courses,
            "inactive_courses": inactive_courses,
            "activity_percentage": round((active_courses / total_courses * 100), 2) if total_courses > 0 else 0
        }
        
        return Response({
            'success': True,
            'message': '📊 Estadísticas de cursos generadas',
            'data': statistics,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_200_OK)



class CourseListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos los cursos
    POST: Crea un nuevo curso
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'📖 Se encontraron {len(serializer.data)} cursos disponibles',
            'total_count': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene un curso específico con detalles
    PUT: Actualiza un curso completamente
    PATCH: Actualiza un curso parcialmente
    DELETE: Elimina un curso
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

class GradeListCreateView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]
    
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'📊 Se encontraron {len(serializer.data)} notas registradas',
            'total_count': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })

class GradeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]

class StudentGradesView(ListAPIView):
    """Obtener todas las notas de un estudiante específico"""
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        student_id = self.kwargs['student_id']
        return Grade.objects.filter(inscription__student_id=student_id)
    
    def list(self, request, *args, **kwargs):
        student_id = self.kwargs['student_id']
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        try:
            student = Student.objects.get(id=student_id)
            student_name = f"{student.names}"
        except Student.DoesNotExist:
            student_name = f"ID: {student_id}"
        
        return Response({
            'success': True,
            'message': f'🎓 Notas del estudiante {student_name}',
            'student_id': student_id,
            'total_grades': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })
class WorkloadGradesView(ListAPIView):
    """Obtener todas las notas de una carga académica específica"""
    serializer_class = GradeSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        workload_id = self.kwargs['workload_id']
        return Grade.objects.filter(inscription__workload_id=workload_id)
    
    def list(self, request, *args, **kwargs):
        workload_id = self.kwargs['workload_id']
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'📊 Notas de la carga académica ID: {workload_id}',
            'workload_id': workload_id,
            'total_grades': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })
    
def student_dashboard(request, student_id):
    if request.method == 'GET':
        data = {
            "student_id": student_id,
            "curriculum": 2023,
            "year": 3,
            "semester": 5,
            "code": "CODE-123",
            "name": "Django",
            "acronym": "django",
            "credits": 4.0,
            "theory_hours": 2.0,
            "practice_hours": 2.0,
            "laboratory_hours": 2.0,
            "laboratory": True
        }
        return JsonResponse(data)

    elif request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            data['student_id'] = student_id  # Agregamos el student_id de la URL
            # Aquí podrías validar o procesar data antes de devolverla
            return JsonResponse({
                "message": "Datos recibidos correctamente",
                "received": data
            })
        except json.JSONDecodeError:
            return HttpResponseBadRequest("JSON inválido")

    else:
        return HttpResponseBadRequest("Solo métodos GET y POST permitidos")


class RegisterView(generics.CreateAPIView):
    """Registro de nuevos usuarios"""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        
        return Response({
                'success': True,
                'message': f'✅ Usuario {user.username} registrado exitosamente',
                'data': {
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    },
                    'token': token.key,
                },
                'timestamp': datetime.now().isoformat()
            }, status=status.HTTP_201_CREATED)
        
        return Response({
            'success': False,
            'message': '❌ Error en el registro de usuario',
            'errors': serializer.errors,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(generics.GenericAPIView):
    """Login de usuarios con interfaz browsable"""
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            login(request, user)
            
            return Response({
                'success': True,
                'message': f'🔐 Bienvenido {user.username}, inicio de sesión exitoso',
                'data': {
                    'user': {
                        'id': user.id,
                        'username': user.username,
                        'email': user.email,
                        'first_name': user.first_name,
                        'last_name': user.last_name,
                    },
                    'token': token.key,
                    'last_login': user.last_login.isoformat() if user.last_login else None
                },
                'timestamp': datetime.now().isoformat()
            })
        
        return Response({
            'success': False,
            'message': '❌ Credenciales inválidas - Verifica tu usuario y contraseña',
            'errors': serializer.errors,
            'timestamp': datetime.now().isoformat()
        }, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()  # si estás usando TokenAuthentication
        return Response({
            'success': True,
            'message': '👋 Has cerrado sesión correctamente',
        }, status=status.HTTP_200_OK)
class ProfileView(generics.RetrieveUpdateAPIView):
    """Ver y actualizar perfil del usuario autenticado"""
    serializer_class = UserRegistrationSerializer
    
    def get_object(self):
        return self.request.user
    

class UserListView(generics.ListAPIView):
    """Ver todos los usuarios registrados"""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden ver la lista

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar o eliminar un usuario específico por ID"""
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]

class ProfileView(generics.RetrieveUpdateAPIView):
    """Ver y actualizar perfil del usuario autenticado actual"""
    serializer_class = UserRegistrationSerializer
    permission_classes = [IsAuthenticated]
    
    def get_object(self):
        return self.request.user
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': f'🏠 Perfil personal de {instance.username}',
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })


class AllProfilesView(generics.ListAPIView):
    """Ver todos los perfiles con información básica"""
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        users = User.objects.all()
        data = []
        for user in users:
            data.append({
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_active': user.is_active,
                'date_joined': user.date_joined,
                'last_login': user.last_login,
            })
        return Response(data)
    
class UserListView(generics.ListAPIView):
    """Ver todos los usuarios registrados"""
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    permission_classes = [IsAuthenticated]
    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        
        return Response({
            'success': True,
            'message': f'👥 Se encontraron {len(serializer.data)} usuarios registrados',
            'total_count': len(serializer.data),
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Ver, actualizar o eliminar un usuario específico por ID"""
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response({
            'success': True,
            'message': f'👤 Información del usuario {instance.username}',
            'data': serializer.data,
            'timestamp': datetime.now().isoformat()
        })

class AuthStatusView(APIView):
    """
    ℹ️ ESTADO DE AUTENTICACIÓN
    
    GET: Verifica si el usuario está autenticado y retorna su información
    """
    permission_classes = [AllowAny]
    
    def get(self, request):
        if request.user.is_authenticated:
            return Response({
                'success': True,
                'authenticated': True,
                'message': f'✅ Usuario {request.user.username} está autenticado',
                'data': {
                    'user': {
                        'id': request.user.id,
                        'username': request.user.username,
                        'email': request.user.email,
                        'first_name': request.user.first_name,
                        'last_name': request.user.last_name,
                        'is_staff': request.user.is_staff,
                        'date_joined': request.user.date_joined.isoformat(),
                        'last_login': request.user.last_login.isoformat() if request.user.last_login else None
                    }
                },
                'timestamp': datetime.now().isoformat()
            })
        else:
            return Response({
                'success': True,
                'authenticated': False,
                'message': '❌ Usuario no autenticado',
                'timestamp': datetime.now().isoformat()
            })