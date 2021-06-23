from django.shortcuts import render
from .models import ProductDesign
from django.views import View


# Create your views here.

class EditorView(View):
    template_name = 'editor.html'

    def get(self, request, *args, **kwargs):
        product = ProductDesign.objects.filter(id=3).first()
        return render(request, self.template_name, {'product': product})
