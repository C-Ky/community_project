from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Communaute, Priorite, Post, Commentaire
from .forms import SubscriptionForm, CommentaireForm, PostForm
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


@login_required()
def communaute(request, id):
    """ Displays the posts of the specified community """
    # Getting all posts of the specified community
    community = get_object_or_404(Communaute, id=id)
    posts = Post.objects.filter(communaute=community)
    return render(request, 'communaute.html', locals())


@login_required()
def post(request, id):
    """ Displays the specified post with its comments and allows creation of comments """

    # Creating comment
    form = CommentaireForm(request.POST)
    if form.is_valid():
        form.save()

    # Getting post details and comments
    post = get_object_or_404(Post, id=id)
    comments = Commentaire.objects.filter(post=post)
    nb_comments = comments.count()
    rowspan = 2+post.evenementiel

    return render(request, 'post.html', locals())


@login_required()
def nouveau_post(request):
    """ Page to create a new post """
    communities = Communaute.objects.all()
    priorities = Priorite.objects.all()
    post_id = Post.objects.count()+1
    form_post = PostForm(request.POST)
    if form_post.is_valid():
        form_post.save()
        return redirect('post/{0}'.format(post_id))
    return render(request, 'nouveau_post.html', locals())