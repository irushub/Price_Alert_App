from django_cron import CronJobBase, Schedule
import requests
from django.core.mail import send_mail
from django.conf import settings
from alerts.models import Alert
import logging

logger = logging.getLogger(__name__)

class CheckBTCPriceCronJob(CronJobBase):
    RUN_EVERY_MINS = 1

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'alerts.check_btc_price'

    def do(self):
        logger.info("Running check_btc_price cron job")
        try:
            response = requests.get('https://hermes.pyth.network/v2/updates/price/latest?ids[]=e62df6c8b4a85fe1a67db44dc12de5db330f7ac66b72dc658afedf0f4a415b43')
            response.raise_for_status()
            data = response.json()
            logger.info("Received data: %s", data)
            if 'parsed' in data and len(data['parsed']) > 0:
                current_price_str = data['parsed'][0]['price']['price']
                current_price = int(current_price_str) / 1e8
                logger.info("Current BTC price: %s", current_price)
                alerts = Alert.objects.filter(price=current_price)
                for alert in alerts:
                    send_mail(
                        subject='Alert Triggered',
                        message=f'BTC price has reached {current_price}, which matches your alert price of {alert.price}.',
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[alert.email],
                        fail_silently=False,
                    )
                    alert.delete()
        except Exception as e:
            logger.error(f"Error in check_btc_price cron job: {e}")
