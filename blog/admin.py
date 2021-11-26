from django.contrib import admin


from . models import Article,Category, thumbnail_tag , IpAdderss

# Register your models here.

def make_published(modeladmin,request,queryset):
    rows_updated=queryset.update(status='p')
    if rows_updated == 1:
        masage_bit='منتشر شد'
    else:
        masage_bit='منتشر شدند'
    modeladmin.message_user(request,'{} مقاله {}'.format(rows_updated,masage_bit))
make_published.short_description='انتشار مقالات انتخاب شده'

def make_draft(modeladmin,request,queryset):
    rows_updated=queryset.update(status='d')
    if rows_updated == 1:
        masage_bit='پیش نویس شد'
    else:
        masage_bit='پیش نویس شدند'
    modeladmin.message_user(request,'{} مقاله {}'.format(rows_updated,masage_bit))
make_draft.short_description='پیش نویس مقالات انتخاب شده'

class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','status','category_to_str',thumbnail_tag , 'author')
    list_filter=('publish','status')
    search_fields=('title','description')
    ordering=['status','-publish']
    def category_to_str(self,obj):
        return ','.join([category.title for category in obj.category.all()])
    category_to_str.short_description='دسته بندی'
    actions=[make_published,make_draft]

admin.site.register(Article,ArticleAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display=('position','slug','title')
    list_filter=('status',)
    search_fields=('title','slug')

admin.site.register(Category,CategoryAdmin)




admin.site.register(IpAdderss)