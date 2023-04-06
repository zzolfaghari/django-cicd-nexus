echo "--> Starting beats process"
celery -A hexa.tasks worker -l info --without-gossip --without-mingle --without-heartbeat
