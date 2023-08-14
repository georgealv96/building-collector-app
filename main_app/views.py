from django.shortcuts import render

# Create your views here.

finches = [
    {'type': "Cassin's Finch", 'color': 'red'},
    {'type': 'Common Redpoll', 'color': 'red'},
    {'type': 'Goldfinches', 'color': 'yellow'},
    {'type': 'Greenfinches', 'color': 'green'},
    {'type': 'Blue Grosbeak', 'color': 'blue'},
    {'type': 'White Winged Snow Finch', 'color': 'white'}
]

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches
    })