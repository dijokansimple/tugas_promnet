from django.shortcuts import render

def halaman_utama(request):
    return render(request, 'cv_promnet/templates/cv/index.html')
