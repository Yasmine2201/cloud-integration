import json

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect

from authentication.models import CustomUser
from publication.services import PublicationService

@login_required
def profile_page(request):
    publications = PublicationService.get_my_publications(request.user)
    for publication in publications:
        publication.number_likes = PublicationService.get_likes(publication)
        publication.has_user_liked = PublicationService.has_user_liked(publication, request.user)

    return render(request, 'userprofile/profile.html', {"all_publications": publications, "user": request.user})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        new_username = json.loads(request.body).get('username')
        if request.user.username != new_username and CustomUser.objects.filter(username=new_username).exists():
            return JsonResponse({"errors": "Username already taken"}, status=400)
        else:
            request.user.username = new_username
            request.user.save()
            return JsonResponse({"message": "Username updated successfully"}, status=200)

    return JsonResponse({"errors": "invalid method"}, status=400)