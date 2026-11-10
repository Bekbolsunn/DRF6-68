from time import sleep

from celery import shared_task


@shared_task(
    bind=True,
    autoretry_for=(Exception,),
)
def download_excel():
    print("Downloading...")
    # raise ValueError()
    sleep(20)
    print("Dlownloaded!")
    return "Good"
