from django.shortcuts import render, get_list_or_404


def login(request):
    context = {}
    return render(request, 'users/login.html', context)


def registration(request):
    context = {}
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {}
    return render(request, 'users/profile.html', context)


def logout(request):
    context = {}
    return render(request, 'users/logout.html', context)
