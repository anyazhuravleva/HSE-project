from django.shortcuts import render
from django.http import HttpResponse
from main.forms import DataForm


def base(request):
    if request.method == "GET":
        type = DataForm()
        return render(request, "home.html", context={"type": type})


def submit(request):
    if request.method == "POST":
        return HttpResponse('Downloading')
