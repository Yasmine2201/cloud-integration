from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
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