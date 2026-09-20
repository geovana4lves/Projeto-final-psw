from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def home(request):
    return render(
        request,
        'home.html'
    )


@login_required
def painel(request):

    return render(
        request,
        'painel.html'
    )


def erro_403(request, exception=None):

    return render(
        request,
        '403.html',
        status=403
    )