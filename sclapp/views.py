from django.db.models.query import InstanceCheckMeta
from django.shortcuts import get_object_or_404, redirect, render
from .models import Orgao
from .forms import CadOrgaoForm

# Create your views here.
#from django.http import HttpResponse


def index(request):
    return render(request, "base.html")
    #return HttpResponse("Hello, world. You're at the polls index.")

def cad_orgao(request):
    if request.method == "POST":
        form = CadOrgaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cadastro')
    else:
        form = CadOrgaoForm
    return render(request, "cad_orgao.html", {'form': form})


def list_orgao(request):
    form = Orgao.objects.all()
    
    busca = request.GET.get('search')
    if busca:
        form = Orgao.objects.filter(nome__icontains = busca)
        
    if request.method == "POST":
        form = CadOrgaoForm(request.POST)
           
    return render(request, 'listar_empresa.html', {'form': form}) 

def alt_orgao(request, id):
    empresa = Orgao.objects.get(pk=id)
    form = CadOrgaoForm(request.POST or None, instance=empresa)

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('listar_empresa')
    context = {
        'form':form
    }
    return render(request, 'cad_orgao.html', context)

    
