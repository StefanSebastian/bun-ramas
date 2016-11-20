from django.shortcuts import render
from provider.forms import OfferInsertForm
from django.views.generic.edit import FormView
from django.views import View
from django.http import HttpResponseRedirect

'''
View for adding an offer
'''
class AddOfferView(FormView):
    form_class = OfferInsertForm
    template_name = "provider/add_offer.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form':form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            #saves the values entered in form
            form.save()
            #redirects to success_add page
            return HttpResponseRedirect("success_add/");
        #form is not valid
        return render(request, self.template_name, {'form':form})

'''
Success view after adding an offer
'''
class SuccessOfferAdditionView(View):
    template_name = "provider/success_add.html"

    def get(self, request):
        return render(request, self.template_name)
