from django.shortcuts import render, redirect

def index(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(request, 'index.html')

def demo_request(request):
    return render(request, 'demo_request.html')

def influencers(request):
    return render(request, 'influencers.html')

def consumers(request):
    return render (request, 'consumers.html')

def newsletter(request):
    return render(request, 'newsletter.html')

def about(request):
    return render(request, 'about.html')

def legal_notice(request):
    return render(request, 'legal-notice.html')

def terms(request):
    return render(request, 'terms.html')