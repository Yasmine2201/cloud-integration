from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from publication.services import PublicationService


# Create your views here.
# Create your views here.
def welcome_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    last_publication = PublicationService.get_last_publication()

    print("last publication :",last_publication)
    return render(request, 'publication/welcome.html', {"last_publication": last_publication})

@login_required
def home_page(request):
    user = request.user
    # try:
    #     letter = Letter.objects.get(author=user)
    #     html_content = __text_to_html_content(letter.content)
    #     letter = {
    #         'id': letter.id,
    #         'title': letter.title,
    #         'author': letter.author,
    #         'content': html_content
    #     }
    # except Letter.DoesNotExist:
    #     letter = None
    # return render(request, 'love/home.html', {"letter": letter, "user": user})
    return render(request, 'publication/home.html')