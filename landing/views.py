from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm

def landing_page(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('landing_page')
    else:
        form = ClienteForm()

    return render(request, 'landing/landing_page.html', {'form': form})
