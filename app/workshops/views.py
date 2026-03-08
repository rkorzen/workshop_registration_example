from django.shortcuts import render

from workshops.models import Workshop


# Create your views here.
def workshop_list(request):
    workshops = Workshop.objects.all()
    return render(request, "workshops/workshop_list.html", {"workshops": workshops})


def workshop_detail(request, pk):
    ...

def workshop_register(request, pk):
    ...

def registration_success(request):
    ...