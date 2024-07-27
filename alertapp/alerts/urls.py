

from django.urls import path
from .views import index, create_alert, fetch_alerts, delete_alert

urlpatterns = [
    path('', index, name='index'),
    path('create/', create_alert, name='create_alert'),
    path('fetch/', fetch_alerts, name='fetch_alerts'),
    path('delete/<int:alert_id>/', delete_alert, name='delete_alert'),
]
