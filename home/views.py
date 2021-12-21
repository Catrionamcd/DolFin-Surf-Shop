from django.shortcuts import render

# View to render the index page.


def index(request):
    """A view to return the index page"""
    return render(request, 'home/index.html')
