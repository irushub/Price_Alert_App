#   Price alert app
## Introduction
The Price Alert App is a Django application designed to send email alerts when the Bitcoin (BTC) price hits a specified target value. This application uses the Pyth Network API to fetch the latest BTC price and allows users to set their alert preferences via a web interface.

## Features
- Fetches real-time BTC prices from the Pyth Network API.
- Allows users to set target BTC prices and receive email alerts when the target price is reached.
- Web interface for setting up and managing alerts.

## Requirements
Python 
Django 
requests
django-environ
SQLite
django-cron
redis

## Installation
** 1. Clone the repository:**
```git clone https://github.com/irushub/alert_app
cd alert_app
```

** 2. Migrate the database:**
```python manage.py migrate```

** 3. Start the Redis and Django development server:**
Start redis server
```redis-server```

Ping the redis server to check whether its online 
```ping redis-cli```

Start the Django development server
```python manage.py runserver```

** 4. Start the Django CRON Job:**
```python manage.py runcrons```
