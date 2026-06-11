from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Equipment, EquipmentFailure
from .forms import EquipmentForm, FailureForm

@login_required
def equipment_list(request):
    q = request.GET.get('q','')
    status = request.GET.get('status','')
    qs = Equipment.objects.all()
    if q: qs = qs.filter(name__icontains=q)
    if status: qs = qs.filter(status=status)
    return render(request,'equipments/equipment_list.html',{'equipments':qs,'q':q,'status':status,'status_choices':Equipment.STATUS_CHOICES})

@login_required
def equipment_detail(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    schedules = eq.schedules.order_by('-start_datetime')[:5]
    failures = eq.failures.all()[:5]
    return render(request,'equipments/equipment_detail.html',{'equipment':eq,'schedules':schedules,'failures':failures})

@login_required
def equipment_create(request):
    form = EquipmentForm(request.POST or None, request.FILES or None)
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Equipamento cadastrado!')
        return redirect('equipments:equipment_list')
    return render(request,'equipments/equipment_form.html',{'form':form,'title':'Novo Equipamento'})

@login_required
def equipment_edit(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    form = EquipmentForm(request.POST or None, request.FILES or None, instance=eq)
    if request.method=='POST' and form.is_valid():
        form.save()
        messages.success(request,'Equipamento atualizado!')
        return redirect('equipments:equipment_detail',pk=pk)
    return render(request,'equipments/equipment_form.html',{'form':form,'title':'Editar Equipamento','equipment':eq})

@login_required
def report_failure(request, pk):
    eq = get_object_or_404(Equipment, pk=pk)
    form = FailureForm(request.POST or None)
    if request.method=='POST' and form.is_valid():
        f=form.save(commit=False)
        f.equipment=eq; f.reported_by=request.user
        f.save()
        eq.status='broken'; eq.save()
        messages.warning(request,'Falha registrada e equipamento marcado como com defeito.')
        return redirect('equipments:equipment_detail',pk=pk)
    return render(request,'equipments/failure_form.html',{'form':form,'equipment':eq})
