from django.shortcuts import get_object_or_404, render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from django.conf import settings

from .models import HomePage, Team, About, Work
from .forms import ContactForm


def home(request):
    home = HomePage.objects.first()
    about = About.objects.first()
    return render(request, 'home.html', {'home': home, 'about': about})


def team(request):
    teams = Team.objects.all()
    return render(request, 'team.html', {'teams': teams})
    

def contact(request):
    from_email = settings.DEFAULT_FROM_EMAIL
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            body = form.cleaned_data['body']
            to_email = form.cleaned_data['email']

            mail = EmailMessage(subject, body, from_email, [to_email])
            mail.send()
            messages.success(request, 'Your email has been sent successfully.')
            return redirect('home')
    else:
        form = ContactForm()

    template_name = 'contact.html'
    context = {'contact': contact, 'form': form}

    return render(request, template_name, context)


def about(request):
    about = About.objects.first()
    return render(request, 'about.html', {'about': about})
    

def works(request):
    works = Work.objects.all()
    return render(request, 'works.html', {'works': works})
    

def profile(request, slug):
    profile = get_object_or_404(Team, slug=slug)

    return render(request, 'profile.html', {'profile': profile})
    