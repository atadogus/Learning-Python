from django.shortcuts import render

posts = [
    {
        "author": "Popper",
        "title": "Logic of Research",
        "content": "Logic",
        "date_posted": "22nd June 1964"
    },
    {
        "author": "Foucault",
        "title": "History of Sexuality",
        "content": "Sex",
        "date posted": "4th May 1968"
    }
]


def home(request):
    """home page"""

    context = {
        "posts": posts
    }

    return render(request, 'blog/home.html', context)


def about(request):
    """info about the blog website"""

    return render(request, 'blog/about.html')
