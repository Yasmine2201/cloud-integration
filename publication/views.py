from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from publication.models import Like
from publication.services import PublicationService

@login_required
def like_publication(request, publication_id):
    publication = PublicationService.get_publication_by_id(publication_id)
    PublicationService.like_publication(publication, request.user)
    return render(request, 'publication/home.html', {"publication": publication, "user": request.user})

@login_required
def dislike_publication(request, publication_id):
    publication = PublicationService.get_publication_by_id(publication_id)
    PublicationService.dislike_publication(publication, request.user)
    return render(request, 'publication/home.html', {"publication": publication, "user": request.user})

@login_required
def home_page(request):
    user = request.user
    publications = PublicationService.get_all_publications(user)
    for publication in publications:
        publication.number_likes = PublicationService.get_likes(publication)
        publication.has_user_liked = PublicationService.has_user_liked(publication, user)

    print("publications :", publications)
    return render(request, 'publication/home.html', {"all_publications": publications, "user": user})