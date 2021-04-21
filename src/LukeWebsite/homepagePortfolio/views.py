from django.shortcuts import render


# Create your views here.
def index(request):
    context = {}
    return render(request, 'homepagePortfolio/index.html', context)


def about(request):
    return render(request, 'homepagePortfolio/about.html', {})
