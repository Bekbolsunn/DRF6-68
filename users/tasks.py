from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail


@shared_task
def send_otp_mail(code, email, user_id):
    print("Sending...")
    send_mail(
        "Регистраця в SHOP api",
        f"ваш одноразовый код для регистрации: {code} \n и id:{user_id}",
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )
    print("Sent")
    return "Done"


@shared_task
def delete_unactive_users():
    from users.models import CustomUser

    deleted = CustomUser.objects.filter(is_active=False).delete()
    return f"Deleted: {deleted}"
