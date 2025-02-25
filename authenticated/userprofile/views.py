import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

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
        request.user.username = json.loads(request.body).get('username')
        request.user.save()
    return redirect('profile')