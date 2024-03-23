# from django.shortcuts import render

# def Welcome(request):
#         return render(request, 'index.html')

# def User(request):
#         username = request.GET['username']
#         print(username)
#         return render(request, 'user.html', {'name':username}) 
# from django.shortcuts import render

# def Welcome(request):
#         return render(request, 'index.html')

# def User(request):
#     if 'username' in request.GET:
#         username = request.GET['username']
#         return render(request, 'user.html', {'name': username})
#     else:
#         return render(request, 'user.html', {'name': 'Default Name'})

# from django.shortcuts import render

# def Welcome(request):
#     return render(request, 'index.html')

# def User(request):
#     if 'username' in request.GET:
#         username = request.GET['username']
#         print(username)
#         return render(request, 'user.html', {'name': username})
#     else:
#         return render(request, 'index.html')  # Redirect to index if username not provided

from django.shortcuts import render
from .phishing_detector import predict_phishing  # Import your function for phishing detection

def welcome(request):
    return render(request, 'index.html')

def user(request):
    if 'url' in request.GET:
        url = request.GET['url']
        is_phishing = predict_phishing(url)
        return render(request, 'user.html', {'url': url, 'is_phishing': is_phishing})
    else:
        return render(request, 'index.html')  # Redirect to index if URL not provided

