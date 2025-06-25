from django.contrib import admin

from django.contrib import admin

from .models.Course import Course
from .models.Teacher import Teacher
from .models.Workload import Workload
from .models.Student import Student
from .models.Inscription import Inscription
from .models.Proxy import Proxy
from .models.YearCourse import YearCourse
from .models.Announcement import Announcement
from .models.Grade import Grade

admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Workload)
admin.site.register(Inscription)

admin.site.register(YearCourse)
admin.site.register(Announcement)
admin.site.register(Grade)

@admin.register(Proxy)
class ProxyAdmin(admin.ModelAdmin):
    list_display = ['names', 'father_surname', 'mother_surname', 'email', 'phone', 'status']
    search_fields = ['names', 'father_surname', 'mother_surname', 'email']
    list_filter = ['status', 'created']

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['cui', 'names', 'get_proxy_name', 'status']
    search_fields = ['cui', 'names']
    list_filter = ['status', 'created']

    def get_proxy_name(self, obj):
        return str(obj.proxy) if obj.proxy else 'Sin apoderado'
    get_proxy_name.short_description = 'Apoderado'