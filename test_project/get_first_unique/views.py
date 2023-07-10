from django.shortcuts import render
from util import get_fist_unique_for_words


# Create your views here.
def index(request):
    return render(request, "get_first_unique/index.html", {})


def result(request):
    text = request.POST["text"]
    result = get_fist_unique_for_words(text)

    return render(request, "get_first_unique/result.html", {"text": result})
