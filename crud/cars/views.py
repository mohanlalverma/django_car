from django.shortcuts import render, redirect
from django.views import View
from .form import CarForm
from .models import Car

# Create your views here.


class Car_list(View):
    def get(self, request):
        cars = Car.objects.all()
        return render(request, 'list.html', {'cars': cars})


class Car_form(View):
    def get(self, request, id=0):
        if id == 0:
            form = CarForm()
        else:
            cars = Car.objects.get(pk=id)
            form = CarForm(instance=cars)
        return render(request, 'form.html', {'form': form})

    def post(self, request, id=0):
        if id == 0:
            form = CarForm(request.POST)
        else:
            cars = Car.objects.get(pk=id)
            form = CarForm(request.POST, instance=cars)
        if form.is_valid():
            form.save()
        return redirect('list')


class Car_delete(View):
    def post(self, request, id):
        cars = Car.objects.get(pk=id)
        cars.delete()
        return redirect('list')
