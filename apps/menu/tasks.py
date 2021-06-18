import os
from datetime import date

from celery.decorators import periodic_task
from celery.task.schedules import crontab

import requests

from .models import Menu

# LOAD ENV variables
SERVER_URL = os.getenv("SERVER_URL", default="localhost")
SERVER_PORT = os.getenv("SERVER_PORT", default="8000")
SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")

MENU_URL = f"http://{SERVER_URL}:{SERVER_PORT}/menu"


@periodic_task(run_every=(crontab(hour="10")), name="send_alert")
def send_alert():
    """
    Function that send reminder to slack channel,
    if not exist available menu dont send message.
    """
    menu = Menu.objects.filter(date=date.today()).first()
    if menu:
        message = f"Pst, pst. Tomate unos minutos y revisa el menu de hoy! {MENU_URL}/{menu.uuid}"
        requests.post(SLACK_WEBHOOK, json={"text": message})
