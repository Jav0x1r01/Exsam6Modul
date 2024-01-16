from django.shortcuts import render, redirect
from django.views.generic import ListView,TemplateView

from apps.models import UserModel, Position


class UserModelView(ListView):
    template_name = 'apps/index.html'
    queryset=UserModel.objects.all()
    context_object_name = 'users'


def delete_product(request, pk):
    UserModel.objects.filter(id=pk).delete()
    return redirect('index')


def add_product(request):
    context=None
    if request.method == 'POST':
        context = {
            'positions': Position.objects.all()
        }
        return redirect('products_list')
    return render(request, 'apps/forms.html', context)

