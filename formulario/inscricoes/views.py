from django.shortcuts import render
from .forms import ParticipanteForm

def home(request):
    return render(request, 'index.html')
def cadastro(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            form.save()  
            return render(request, 'sucesso.html')
    else:
        form = ParticipanteForm()
    return render(request, 'cadastro.html', {'form': form})


