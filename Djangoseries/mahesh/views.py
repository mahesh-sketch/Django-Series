from django.shortcuts import render
from .models import ComputerVarity, Store
from django.shortcuts import get_object_or_404
from .forms import ComputerVarityForm

# Create your views here.
def allComputerItem(request):
    computer = ComputerVarity.objects.all()
    return render(request,'mahesh/index.html',{'computers': computer})

def computer_detail(request,comp_id):
    computer = get_object_or_404(ComputerVarity, pk = comp_id)
    return render(request, 'mahesh/mahesh_detail.html',{'computer':computer})

def computer_store_view(request):
    stores = None
    if request.method == 'POST':
        form = ComputerVarityForm(request.POST)
        if form.is_valid():
            compter_variety = form.cleaned_data['computer_variety']
            stores = Store.objects.filter(computer_varieties=compter_variety)
    else:
        form = ComputerVarityForm()
                        
    return render(request,'mahesh/computer_stores.html', {'form':form, 'stores':stores})