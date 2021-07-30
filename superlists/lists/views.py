from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import Item
# Create your views here.
def home_page(request):
  if request.method == "POST":
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/')

  return render(request, "home.html", {
    "items": Item.objects.all()
  })