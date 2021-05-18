from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def homepage(request):
    """ Displays the homepage of the site (intended for when user not logged in) """
    return render(request, 'homepage.html', locals())


@login_required()
def homepage_user(request):
    """ Displays the homepage of a user """
    return render(request, 'homepage_user.html', locals())