from django.urls import path
from student_app import views

urlpatterns = [
    path('info',views.info),
    path('dashboard',views.dashboard),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete)
]