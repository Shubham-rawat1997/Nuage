from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DepartmentViewSet, UserViewSet, StudentViewSet, CourseViewSet, AttendanceLogViewSet

from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token 

router = DefaultRouter()
router.register(r'departments', DepartmentViewSet)
router.register(r'users', UserViewSet)
router.register(r'students', StudentViewSet)
router.register(r'courses', CourseViewSet)
router.register(r'attendance_logs', AttendanceLogViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('token/',obtain_auth_token), # It will generate the token for user providing username and password
    
]