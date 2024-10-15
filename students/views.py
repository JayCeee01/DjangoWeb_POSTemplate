from django.shortcuts import render

def home(request):
    return render(request, 'students/home.html')

def viewItem(request):
    txt1 = request.POST.get('txt1')
    txt2 = request.POST.get('txt2')
    return render(request, 'students/viewItem.html', {'txt1' : txt1, 'txt2' : txt2,})
