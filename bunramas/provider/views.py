from django.shortcuts import render
from provider.forms import OfferInsertForm

'''
View for adding an offer
'''
def add_offer(request):
    if request.method == "POST":
        form = OfferInsertForm(request.POST)
        if form.is_valid():
            offer = form.save()
    else:
        form = OfferInsertForm()

    '''
    Path to html file
    '''
    template_name = "provider/add_offer.html"

    return render(request, template_name, {'form':form})
