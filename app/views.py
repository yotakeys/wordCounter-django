from django.shortcuts import render

# Create your views here.
def wordCounter(request):
    __text = ""
    __characters = 0
    __words = 0
    __sentences = 0
    __paragraphs = 0
    __readingTime = 0
        
    if request.method == 'POST':
        __text = request.POST.get('textInput')

    return render(request,'app/index.html')