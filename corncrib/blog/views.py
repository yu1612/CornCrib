from django.shortcuts import render

posts = [
    {
        'author': "michelle",
        'title': 'clara dickson hall',
        'content': 'north campus',
        'date_posted': 'october 25th, 2023'
    },
    {
        'author': "michelle",
        'title': 'mary donlon hall',
        'content': 'north campus party dorm',
        'date_posted': 'october 25th, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'home/index.html', context)

def login(request):
    return render(request, 'home/login.html', {'title': 'hi'})
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

