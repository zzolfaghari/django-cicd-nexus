echo "--> Starting celery process"
celery -A hexa.tasks beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
