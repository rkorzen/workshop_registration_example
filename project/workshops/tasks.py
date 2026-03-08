from celery import shared_task
from django.utils.translation import gettext_lazy as _
from django.core.mail import send_mail
from .models import Registration
from django.conf import settings

@shared_task
def send_registration_confirmation(registration_id):
    registration = Registration.objects.select_related("workshop").get(id=registration_id)

    subject = _("Registration Confirmation")
    message = _(
        "Dear {name},\n\n"
        "Thank you for registering for the workshop: {workshop}.\n\n"
        "Best regards,\n"
        "The Workshop Team"
    ).format(name=registration.name, workshop=registration.workshop)

    send_mail(
        subject=subject,
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[registration.email],
        fail_silently=False,
    )