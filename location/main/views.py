from django.shortcuts import render, redirect
from main.forms import DataForm, LoginForm, RegForm, AntennasForm
from main.models import RequestTable, AntennasTable
from django.contrib.auth import authenticate, login as person_login, logout
from django.contrib.auth.models import User
from django.db import IntegrityError


def base(request):
    if not request.user.is_authenticated:
        type = LoginForm()

        return render(request, "login.html", context={"type": type})
    else:
        if request.method == "GET":
            type = DataForm()
            base = RequestTable.objects.filter(user=request.user)

            return render(request, "home.html", context={"type": type, "people": base, "user": request.user})


def login(request):
    if request.method == "POST":
        type = LoginForm(request.POST)

        if type.is_valid():
            email = type.cleaned_data["email"]
            password = type.cleaned_data["password"]

            person = authenticate(request, email=email, password=password)

            if person is not None:
                person_login(request, person)

        return redirect("/")


def registration(request):
    if request.method == "GET":
        type = RegForm()
        return render(request, "registration.html", context={"type": type})

    if request.method == "POST":
        type = RegForm(request.POST)

        if type.is_valid():
            email = type.cleaned_data["email"]
            password = type.cleaned_data["password"]

            try:
                person = User.objects.create_user(username=email, email=email, password=password)
                person_login(request, person)

            except IntegrityError:
                return render(request, "registration.html", context={"type": type, "message": "Email is exist"})

        return redirect("/")


def logout_view(request):
    logout(request)
    return redirect("/")


def submit(request):
    if request.method == "POST":
        type = DataForm(request.POST, request.FILES)

        if type.is_valid():
            file = type.cleaned_data["file"]
            antenna = type.cleaned_data["antenna"]

            RequestTable.objects.create(user=request.user, file=file, antenna=antenna.name).save()

        return redirect("/")


def antennas_download(request):
    if request.method == "POST":
        type = AntennasForm(request.POST, request.FILES)

        if type.is_valid():
            antennas = type.cleaned_data["antennas"]

            for line in antennas:
                AntennasTable.objects.create(name=line.decode("utf-8").strip()).save()

        return redirect("/")

    if request.method == "GET":
        if request.user.is_superuser:
            type = AntennasForm()
            return render(request, "dl_antennas.html", context={"type": type})

        return redirect("/")



