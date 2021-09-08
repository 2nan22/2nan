from django.shortcuts import redirect, render


def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )

def about_me(request):
    return render(
        request,
        'single_pages/about_me.html',
    )

def work_1(request):
    return render(
        request,
        'single_pages/work_1.html',
    )