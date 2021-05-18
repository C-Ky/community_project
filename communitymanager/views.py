from django.shortcuts import render


def homepage(request):
    """ Displays the homepage with list of all communities """
    return render(request, 'homepage.html', locals())