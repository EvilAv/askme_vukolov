from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
QUESTIONS = [
    {
        "title": f"Title #{i}",
        "text": f"this is text for question #{i}",
        "number": i,
    } for i in range(10)
]

ANSWERS = [
    {
        "title": f"Answer #{i}",
        "text": f"this is text for answer #{i}",
        "number": i,
    } for i in range(3)
]

def index(request):
    return render(request, "index.html", {"questions": QUESTIONS})

def settings(request):
    return render(request, "settings.html")

def tag(request, i: int):
    return render(request, "tag.html", {"questions": QUESTIONS})

def register(request):
    return render(request, "registration.html")

def login(request):
    return render(request, "login.html")

def ask(request):
    return render(request, "ask.html")

def question(request, i: int):
    return render(request, "question_page.html", {"question": QUESTIONS[i], "answers": ANSWERS})