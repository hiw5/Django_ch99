from django.shortcuts import render
from practice.models import PracticeModels
from django.views.generic import TemplateView, ListView
from django.views.generic.list import MultipleObjectMixin

#Create your views here.

class PracticeViews(TemplateView):
    template_name='practice/practice.html'
    model = PracticeModels
    context_object_name='practice_context_object_name' # context에 담아서 활용

    def get(self, request, *args, **kwargs):    # get 함수가 오버라이드 되며, render를 호출하기에 get_context_data는 실행되지않음

        queryset = PracticeModels.objects.all().order_by("-practice_dt")
        context = dict()
        context['practice'] = queryset

        print(queryset.query)
        return render(request, self.template_name, context)
    
    def get_context_data(self, *args, **kwargs):

        context = super().get_context_data(**kwargs)
        
        context[self.context_object_name] = self.model.objects.all().order_by("-practice_dt")

        
        print(type(context))
        

        return context


    # def get(self, request, *args, **kwargs):
    #     practice_char = request.GET.get("practice_char", "").strip()
    #     practice_int = request.GET.get("practice_int", "").strip()
    #     return render(self.request, self.template_name)

class PracticePaginationViews(TemplateView, MultipleObjectMixin):
    template_name='practice/practice_pagination.html'
    model=PracticeModels
    context_object_name='practice_context_object_name' # context에 담아서 활용
    paginate_by = 10

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)

        return self.render_to_response(context)
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-practice_dt')
    
    def get_paginate_by(self, queryset):
        return int(self.request.GET.get('per_page',self.paginate_by))
    