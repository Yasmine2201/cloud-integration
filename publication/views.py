import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render

from publication.services import PublicationService

@login_required
def create_publication(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = request.user

        PublicationService.create_publication(user, body.get("title"), body.get("body"))
        return JsonResponse({"message": "Publication created successfully"})

@login_required
def like_publication(request, publication_id):
    publication = PublicationService.get_publication_by_id(request.user, publication_id)
    PublicationService.like_publication(publication, request.user)
    return JsonResponse({"message": "Publication liked successfully"})

@login_required
def dislike_publication(request, publication_id):
    publication = PublicationService.get_publication_by_id(request.user, publication_id)
    PublicationService.dislike_publication(publication, request.user)
    return JsonResponse({"message": "Publication disliked successfully"})

@login_required
def delete_publication(request, publication_id):
    PublicationService.delete_my_publication(request.user, publication_id)
    return JsonResponse({"message": "Publication deleted successfully"})

@login_required
def edit_publication(request, publication_id):
    if request.method == 'POST':
        body = json.loads(request.body)
        user = request.user

        PublicationService.edit_my_publication(user, publication_id, body.get("title"), body.get("body"))
        return JsonResponse({"message": "Publication edited successfully"})
@login_required
def home_page(request):
    user = request.user
    publications = PublicationService.get_all_publications()
    for publication in publications:
        publication.number_likes = PublicationService.get_likes(publication)
        publication.has_user_liked = PublicationService.has_user_liked(publication, user)

    print("publications :", publications)
    return render(request, 'publication/home.html', {"all_publications": publications, "user": user})