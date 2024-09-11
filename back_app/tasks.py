from celery.schedules import crontab

from back_app.app import app

from rest_1c.api import status_api

from service.push import pusher
from service.settings.params import ServiceSettings


@app.tasks
async def get_status() -> None:
    orders = await status_api.orders()
    for order in orders:
        await pusher.push(data=order)


app.conf.beat_schedule = {
    'get_status': {
        'task': 'get_status',
        'schedule': crontab(minute=f'*/{ServiceSettings.timeout_minutes}')
    }
}