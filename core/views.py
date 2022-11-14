from django.shortcuts import render


def home(request):

    return render(request, 'home.html', {})


def team(request):

    return render(request, 'team.html', {})
    

def contact(request):

    return render(request, 'contact.html', {})
    

def about(request):

    return render(request, 'about.html', {})
    

def works(request):

    return render(request, 'works.html', {})
    

def profile(request):

    return render(request, 'profile.html', {})
    