from django.shortcuts import render
from .models import ComputerVarity
from django.shortcuts import get_object_or_404

# Create your views here.
def allComputerItem(request):
    computer = ComputerVarity.objects.all()
    return render(request,'mahesh/index.html',{'computers': computer})

def computer_detail(request,comp_id):
    computer = get_object_or_404(ComputerVarity, pk = comp_id)
    return render(request, 'mahesh/mahesh_detail.html',{'computer':computer})