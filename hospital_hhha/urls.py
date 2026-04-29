from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from pacientes import views

# Importaciones necesarias para ver los archivos
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('paciente/<int:id>/', views.detalle_paciente, name='detalle_paciente'),
    path('examen/pdf/<int:examen_id>/', views.ver_pdf, name='ver_pdf'),
    path('examen/imagen/<int:examen_id>/', views.ver_imagen, name='ver_imagen'),
]

# Agregar esto al final para servir archivos multimedia localmente
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)