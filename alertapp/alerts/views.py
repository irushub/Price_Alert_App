from django.shortcuts import get_object_or_404, redirect, render
from .models import Alert
from .forms import AlertForm
from django.core.mail import send_mail
from django.conf import settings
import requests

from django.shortcuts import render

def index(request):
    return render(request, 'alerts/index.html')

def send_alert_email(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,  
        recipient_list,  
        fail_silently=False,
    )

def create_alert(request):
    if request.method == 'POST':
        form = AlertForm(request.POST)
        if form.is_valid():
           
            alert = form.save(commit=False)
            alert.title = 'Bitcoin Alert' 
            alert.save()
            
         
            send_alert_email(
                subject='New Bitcoin Alert Created',
                message=f'Bitcoin alert created.\nPrice: {alert.price}',
                recipient_list=[alert.email]  
            )
            
            return render(request, 'alerts/success.html')
    else:
        form = AlertForm()
    return render(request, 'alerts/create_alert.html', {'form': form})


def fetch_alerts(request):
    alerts = Alert.objects.all()
    return render(request, 'alerts/fetch_alerts.html', {'alerts': alerts})

def delete_alert(request, alert_id):
    alert = get_object_or_404(Alert, id=alert_id)
    if request.method == 'POST':
        alert.delete()
        return redirect('fetch_alerts')
    return render(request, 'alerts/delete_alert.html', {'alert': alert})
