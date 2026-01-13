from django.shortcuts import render
from .forms import ParticipanteForm
# Create your views here.

def home(request):
    return render(request, 'index.html')

def cadastro(request):
    # Configurar a requisição (POST)
    if request.method ==  'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()
    else: # GET
        form = ParticipanteForm()
    
    return render(request, 'cadastro.html', {'form': form})
           