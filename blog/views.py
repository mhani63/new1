
from django.shortcuts import render
from . models import Article,Category
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView , ListView
from django.db.models import Q
# Create your views here.

class article_list(ListView):
    queryset=Article.objects.filter(status='p')



class ArticleDetail(DetailView):
    def get_object (self):
        slug=self.kwargs.get('slug')
        article= get_object_or_404(Article,slug=slug,status='p')
        ip_address = self.request.user.ip_address
        if ip_address not in article.hits.all():
            article.hits.add(ip_address)

        return article



class CategoryList(ListView):
    paginate_by=3
    template_name='blog/category_list.html'

    def get_queryset(self):
        global category
        slug=self.kwargs.get('slug')
        category=get_object_or_404(Category.objects.active(),slug=slug)
        return category.articles.published()

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['category']=category
        return context
    

class SearchList(ListView):
    paginate_by=3
    template_name='blog/search_list.html'

    def get_queryset(self):
        search=self.request.GET.get('q')
        return Article.objects.filter(Q(description__icontains=search)| Q(title__icontains=search))

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['search']=self.request.GET.get('q')
        return context