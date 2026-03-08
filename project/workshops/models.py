from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Workshop(models.Model):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    start_date = models.DateTimeField(verbose_name=_("Start Date"))
    location = models.CharField(max_length=255, verbose_name=_("Location"))
    image = models.ImageField(
        upload_to="workshops/", blank=True, null=True, verbose_name=_("Image")
    )

    class Meta:
        ordering = ["start_date"]
        verbose_name = _("Workshop")
        verbose_name_plural = _("Workshops")

    def __str__(self):
        return self.title


class Registration(models.Model):
    workshop = models.ForeignKey(
        Workshop,
        on_delete=models.CASCADE,
        related_name="registrations",
        verbose_name=_("Workshop"),
    )
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    email = models.EmailField(verbose_name=_("Email"))
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"))

    class Meta:
        ordering = ["-created_at"]
        verbose_name = _("Registration")
        verbose_name_plural = _("Registrations")

    def __str__(self):
        return f"{self.name} -> {self.workshop.title}"
