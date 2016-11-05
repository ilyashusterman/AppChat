from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


def home(request):
    return render(request, 'index.html', {'users': users})


class User:
    def __init__(self, name, value):
        self.name = name
        self.value = value


users = {
    User('Ilya shusterman', 20000),
    User('Ilya radu', 2000)
}
