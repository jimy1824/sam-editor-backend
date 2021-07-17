from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import ProductDesign, Category
from django.views import View
from .product_fields import products_dict, all_feilds


# Create your views here.

class EditorView(View):
    # template_name = 'editor.html'
    template_name = 'editor_layers.html'

    def get(self, request, *args, **kwargs):
        product = ProductDesign.objects.filter(id=3).first()
        return render(request, self.template_name, {'product': product})


class ModelFieldsView(TemplateView):

    def post(self, request, *args, **kwargs):
        category = Category.objects.filter(id=request.POST.get('model_id')).first()
        fields = products_dict[0].get(category.key)
        display_false_list = []
        display_true_list = []
        for key in fields.keys():
            if fields.get(key) == 'false':
                display_false_list.append('#id_' + str(key))
            else:
                display_true_list.append('#id_' + str(key))

        dic = {}
        dic['display_false_list'] = display_false_list
        dic['display_true_list'] = display_true_list

        return JsonResponse(dic)


class AllModelFieldsView(TemplateView):

    def post(self, request, *args, **kwargs):
        fields = all_feilds
        all_fielss = []
        for key in fields[0].keys():
            all_fielss.append('#id_' + str(key))
        dic = {}
        dic['all_list'] = all_fielss

        return JsonResponse(dic)
