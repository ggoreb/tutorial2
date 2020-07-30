from django.shortcuts import render
from .models import Hospital

def hospital(request):
  hospital = Hospital.objects.all()
  print(hospital)
  return render(request, 'hospital.html', {'list':hospital})