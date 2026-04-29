from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from .models import Paciente, Examen

@login_required(login_url='login')
def dashboard(request):
    # Contamos solo los exámenes que tienen al menos un archivo (PDF o Imagen)
    pacientes = Paciente.objects.annotate(
        num_examenes=Count(
            'examen',
            filter=Q(examen__reporte_pdf__gt='') | Q(examen__imagen_medica__gt='')
        )
    )
    return render(request, 'dashboard.html', {'pacientes': pacientes})

@login_required(login_url='login')
def detalle_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    examenes = Examen.objects.filter(paciente=paciente)
    return render(request, 'pacientes/detalle_paciente.html', {'paciente': paciente, 'examenes': examenes})

@login_required(login_url='login')
def ver_pdf(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    return render(request, 'pacientes/visor_archivo.html', {
        'examen': examen,
        'tipo': 'pdf',
        'url': examen.reporte_pdf.url
    })

@login_required(login_url='login')
def ver_imagen(request, examen_id):
    examen = get_object_or_404(Examen, id=examen_id)
    return render(request, 'pacientes/visor_archivo.html', {
        'examen': examen,
        'tipo': 'imagen',
        'url': examen.imagen_medica.url
    })