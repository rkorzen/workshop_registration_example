from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils.translation import gettext_lazy as _

from workshops.forms import RegistrationForm
from workshops.models import Workshop
from .tasks import send_registration_confirmation

# Create your views here.
def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, "workshops/workshop_list.html", {"workshops": workshops})


def workshop_detail(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)
    return render(request, "workshops/workshop_detail.html", {"workshop": workshop})

def workshop_register(request, pk):
    workshop = get_object_or_404(Workshop, pk=pk)

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            registration = form.save(commit=False)
            registration.workshop = workshop
            registration.save()

            try:
                send_registration_confirmation.delay(registration.id)
            except Exception as e:
                messages.warning(
                    request,
                    _("Registration confirmation email could not be sent.")
                )

    else:
        form = RegistrationForm()

    context = {"workshop": workshop, "form": form}
    return render(request, "workshops/register.html", context)

def registration_success(request):
    ...