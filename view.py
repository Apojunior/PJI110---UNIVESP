from django.shortcuts import render
from .forms import ClienteForm

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ClienteForm()
    return render(request, 'meu-template.html', {'form': form})

