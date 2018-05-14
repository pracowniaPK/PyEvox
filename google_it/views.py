from django.shortcuts import redirect


def index(request):
    return redirect("http://google.com/search?q={}".format(request.GET.get('co')))
