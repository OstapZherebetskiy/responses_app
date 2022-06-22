from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Areas, Places, Comments
from .forms import PlacesForm, CommentsForm
from django.views.generic import DeleteView
# Create your views here.

def index(request):
    area = Areas.objects.all()
    data = {
        'area':area
    }
    return render(request, 'responses_app/index.html', data)

def area(request, id):
    area = Areas.objects.get(id=id)
    place = area.places_set.order_by('-date_added')
    data = {
        'place':place,
        'area':area
    }
    return render(request, 'responses_app/area.html', data)

def new_place(request, area_id):
#  """Добавляет новую запись по конкретной теме."""
    area = Areas.objects.get(id=area_id)
    if request.method != 'POST':
 # Данные не отправлялись; создается пустая форма.
        form = PlacesForm()
    else:
 # Отправлены данные POST; обработать данные.
        form = PlacesForm(request.POST, request.FILES)
        if form.is_valid():
            new_place = form.save(commit=False)
            new_place.area = area
            new_place.save()
            return redirect('area', id = area_id)

 # Вывести пустую или недействительную форму.
    context = {'area': area, 'form': form}
    return render(request, 'responses_app/new_place.html', context)

def comment_update(request, place_id):
#  """Добавляет новую запись по конкретной теме."""
    place = Places.objects.get(id=place_id)
    if request.method != 'POST':
 # Данные не отправлялись; создается пустая форма.
        form = CommentsForm()
    else:
 # Отправлены данные POST; обработать данные.
        form = CommentsForm(request.POST, request.FILES)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.place = place
            new_comment.save()
            return redirect('comments', pk = place_id)

 # Вывести пустую или недействительную форму.
    context = {'place': place, 'form': form}
    return render(request, 'responses_app/new_comment.html', context)

class OrderDeleteView(DeleteView):
    model = Places
    success_url = reverse_lazy('index')
    template_name = 'responses_app/order_delete.html'

def comments(request, pk):
    place = Places.objects.get(id=pk)
    comment = place.comments_set.order_by('-date_added')
    context = {
        'place':place,
        'comment':comment
    }
    return render(request, 'responses_app/comments.html', context)





    
