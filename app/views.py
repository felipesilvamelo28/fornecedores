from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from .models import Fornecedor

# Create your views here.

class fornecedorForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['nome', 'cnpj', 'forma_med_part', 'mass_esp_apar', 'poros_apar', 'resist_int', 'resist_comp',
                  'resist_choq', 'teor_frag', 'mat_pulv', 'torr_arg', 'limit_m_u', 'resist_desg', 'dist_635',
                  'dist_500', 'dist_380', 'dist_250', 'dist_190', 'dist_127']


def cadastrar_fornecedor(request, template_name='fornecedor_form.html'):
    form = fornecedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('fornecedor_list')
    return render(request, template_name, {'form': form})


def fornecedor_list(request, template_name='fornecedor_list.html'):
    query = request.GET.get("busca")
    if query:
        fornecedor = Fornecedor.objects.filter(nome__icontains = query)
    else:
        fornecedor = Fornecedor.objects.all()
    fornecedores = {'lista': fornecedor}
    return render(request, template_name, fornecedores)


def editar_fornecedor(request, pk, template_name='fornecedor_form.html'):
    fornecedor = get_object_or_404(Fornecedor, pk=pk)
    if request.method == "POST":
        form = fornecedorForm(request.POST, instance=fornecedor)
        if form.is_valid():
            form.save()
            return redirect('fornecedor_list')
    else:
        form = fornecedorForm(instance=fornecedor)
    return render(request, template_name, {'form': form})


def remover_fornecedor(request, pk, template_name = 'fornecedor_delete.html'):
    fornecedor = Fornecedor.objects.get(pk=pk)
    if request.method == 'POST':
        fornecedor.delete()
        return redirect('fornecedor_list')
    return render(request, template_name, {'fornecedor': fornecedor})