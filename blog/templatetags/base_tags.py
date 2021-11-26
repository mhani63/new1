from django import template
from .. models import Category
from django.shortcuts import render

register=template.Library()
@register.simple_tag
def title():
    return 'لاست مووی'



@register.inclusion_tag('blog/partials/cat.nav.html')
def category_navbar():
    return {
        'category':Category.objects.filter(status=True)
    }



@register.inclusion_tag('blog/partials/cat.movie.html')
def category_movie():
    return {
        'category':Category.objects.filter(slug='movie')
    }


@register.inclusion_tag('blog/partials/cat.series.html')
def category_series():
    return {
        'category':Category.objects.filter(slug='srl')
    }