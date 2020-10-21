from django.shortcuts import render
from django.views.generic import View
from .models import IndexDesign


class IndexView(View):
    def get(self, *args, **kwargs):
        index_design = IndexDesign.objects.filter(
            status=1).order_by('timestamp')
        context = {'index_design': index_design}
        return render(self.request, 'main/category-page.html', context)
