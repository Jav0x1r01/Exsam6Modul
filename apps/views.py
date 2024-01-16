from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, FormView

from apps.forms import ProductForm
from apps.models import UserModel, Position


class UserModelView(ListView):
    template_name = 'apps/index.html'
    queryset = UserModel.objects.all()
    context_object_name = 'users'


def delete_product(request, pk):
    UserModel.objects.filter(id=pk).delete()
    return redirect('index')


# class AddProductView(View):
#     def get(self, request):
#         context = {
#             'positions': Position.objects.all()
#         }
#         return render(request, 'apps/forms.html', context)
#
#     def post(self, request):
#         # Post so'rovi bo'yicha kerakli logika
#         return redirect('index')


class AddProductView(FormView):
    template_name = 'apps/forms.html'

    # context_object_name='positions'
    form_class = ProductForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['positions'] = Position.objects.all()
        return context

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
