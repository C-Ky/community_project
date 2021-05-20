from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Communaute
from .forms import SubscriptionForm
from django.contrib.auth.models import User


def homepage(request):
    """ Displays the homepage of the site (intended for when user not logged in) """
    return render(request, 'homepage.html', locals())


@login_required()
def communautes(request):
    """ Displays the homepage (first page to appear after logging in) of a user with the list of communities """

    # Allowing subscription actions
    form = SubscriptionForm(request.POST)
    if form.is_valid():
        community_name = form.cleaned_data['community']
        action = form.cleaned_data['action']
        community = Communaute.objects.get(nom=community_name)
        if action == "subscribe":
            community.abonnes.add(request.user)
        else:
            community.abonnes.remove(request.user)
        community.save()

    # Getting all communities
    com = Communaute.objects.all()
    # Adding subscription status of the user for each community
    com = [(c, c.abonnes.filter(username=request.user.username).exists()) for c in com]

    return render(request, 'communautes.html', locals())