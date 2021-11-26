from django.urls import path
from . views import article_list,ArticleDetail,CategoryList,SearchList



app_name='blog'
urlpatterns = [
    path('', article_list.as_view(),name='home'),
    path('article/<slug:slug>',ArticleDetail.as_view(),name='detail'),
    path('category/<slug:slug>',CategoryList.as_view(),name='category'),
    path('category/<slug:slug>/Page/<int:Page>',CategoryList.as_view(),name='category'),
    path('search/',SearchList.as_view(), name='search'),
    path('search/page/<int:page>',SearchList.as_view(), name='search')

]
