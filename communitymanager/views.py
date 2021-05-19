from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    """ Displays the homepage of the site (intended for when user not logged in) """
    return render(request, 'homepage.html', locals())


@login_required()
def communautes(request):
    """ Displays the homepage (first page to appear after logging in) of a user with the list of communities """
    return render(request, 'communautes.html', locals())