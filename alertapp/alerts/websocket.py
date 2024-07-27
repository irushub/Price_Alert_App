import requests
import time
from django.core.mail import send_mail
from django.conf import settings
from alerts.models import Alert

def fetch_btc_price():
    url = "https://api.coingecko.com/api/v3/coins/bitcoin"
    response = requests.get(url)
    data = response.json()
    return data['market_data']['current_price']['usd']

def check_alerts(price):
    alerts = Alert.objects.filter(symbol='btc', status='created')
    for alert in alerts:
        if price >= alert.trigger_price:
            notify_user(alert)
            alert.status = 'triggered'
            alert.save()

def notify_user(alert):
    subject = 'Alert Triggered!'
    message = f"Your alert for Bitcoin has been triggered at ${alert.trigger_price}."
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [alert.user.email]

    send_mail(subject, message, from_email, recipient_list)

if __name__ == "__main__":
    while True:
        btc_price = fetch_btc_price()
        check_alerts(btc_price)
        time.sleep(60) 
