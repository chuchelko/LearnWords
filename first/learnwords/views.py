from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Word, User
from .forms import NewWordForm


def all_words_page(request):
    user = User.objects.get(name='Эмиль')
    words = user.word_set.all()
    form = NewWordForm(request.POST or None)
    if form.is_valid():
        new_word = form.save(False)
        new_word.user = User.objects.get(name='Эмиль')
        new_word.save()
        form = NewWordForm()
    
    context = {
        'words' : words,
        'PAGE_NAME' : 'Your words',
        'SITE_NAME' : 'learnwords',
        'form' : form,
    }
    return render(request, "learnwords/list_of_words.html", 
    context=context)

def index(request):
    return HttpResponse("")