from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, Quang. You're at the polls index.")