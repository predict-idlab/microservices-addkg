import os


class BaseConfig:

    TARGET_PROMETHEUS_URL = os.environ.get("TARGET_PROMETHEUS_URL", default="http://localhost:9090")
    TARGET_K8S_NAMESPACE = os.environ.get("TARGET_K8S_NAMESPACE", default="onlineboutique")

    COLLECTOR_OUTPUT = os.environ.get("COLLECTOR_OUTPUT", default="/data")
    COLLECTOR_START_TIME = os.environ.get("COLLECTOR_START_TIME", default=None)
    COLLECTOR_END_TIME = os.environ.get("COLLECTOR_END_TIME", default=None)
    COLLECTOR_INTERVAL = os.environ.get("COLLECTOR_INTERVAL", default="15s")

    CELERY_BROKER_USER = os.environ.get("CELERY_BROKER_USER", default="")
    CELERY_BROKER_PASSWORD = os.environ.get("CELERY_BROKER_PASSWORD", default="")
    CELERY_BROKER_HOST = os.environ.get("CELERY_BROKER_HOST", default="localhost")
    CELERY_BROKER_PORT = os.environ.get("CELERY_BROKER_PORT", default="6379")
    CELERY_BROKER_VHOST = os.environ.get("CELERY_BROKER_VHOST", default="0")

    CELERY_BROKER_URL = f"redis://{CELERY_BROKER_USER}:{CELERY_BROKER_PASSWORD}@{CELERY_BROKER_HOST}:{CELERY_BROKER_PORT}/{CELERY_BROKER_VHOST}"
    CELERY_RESULT_BACKEND = f"redis://{CELERY_BROKER_USER}:{CELERY_BROKER_PASSWORD}@{CELERY_BROKER_HOST}:{CELERY_BROKER_PORT}/{CELERY_BROKER_VHOST}"
