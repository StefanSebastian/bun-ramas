from django.shortcuts import render
from provider.forms import OfferInsertForm

def add_offer(request):
    if request.method == "POST":
        form = OfferInsertForm(request.POST)
        if form.is_valid():
            offer = form.save()
    else:
        form = OfferInsertForm()

    template_name = "provider/add_offer.html"

    return render(request, template_name, {'form':form})
