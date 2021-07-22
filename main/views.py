from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.urls import reverse_lazy

from main.models import List
from main.form import ListForm


def successPage():
    return reverse_lazy('main:home_view')


@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    template_name = 'main/index.html'

    def get(self, request):
        all_items = List.objects.all().order_by('-pk')
        context = {
            'all_items': all_items,
        }

        return render(request, self.template_name, context)

    def post(self, request):
        form = ListForm(request.POST or None)

        if not form.is_valid():
            context = {
                'form': form,
            }

            return render(request, self.template_name, context)

        form.save()
        messages.success(request, ('Item Has Been Added To List!!!'))

        return redirect(successPage())


class DeleteView(View):
    def get(self, request, pk):
        item = get_object_or_404(List, pk=pk)
        item.delete()
        messages.success(request, ('Item Has Been Deleted!!!'))

        return redirect(successPage())


class CrossOffView(View):
    def get(self, request, pk):
        item = get_object_or_404(List, pk=pk)
        item.completed = True
        item.save()

        return redirect(successPage())


class UncrossView(View):
    def get(self, request, pk):
        item = get_object_or_404(List, pk=pk)
        item.completed = False
        item.save()

        return redirect(successPage())


@method_decorator(csrf_exempt, name='dispatch')
class UpdateView(View):
    template_name = 'main/update_view.html'

    def get(self, request, pk):
        item = get_object_or_404(List, pk=pk)
        context = {
            'item': item,
        }

        return render(request, self.template_name, context)

    def post(self, request, pk):
        item = get_object_or_404(List, pk=pk)
        form = ListForm(request.POST, instance=item)

        if not form.is_valid():
            context = {
                'form': form,
            }

            return render(request, self.template_name, context)

        form.save()
        messages.success(request, ('Item Has Been Edited!!!'))

        return redirect(successPage())
