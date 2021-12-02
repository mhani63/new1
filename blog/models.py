
from django.db import models
from django.db.models.fields import BooleanField
from django.utils import timezone
from django.utils.html import format_html
from account.models import User
from django.contrib.contenttypes.fields import GenericRelation
from comment.models import Comment
# Create your models here.




class IpAdderss(models.Model):
	ip_address = models.GenericIPAddressField(verbose_name="آدرس آی‌پی")


def thumbnail_tag(self):
    return format_html("<img width=60px src= '{}' >".format(self.thumbnail.url))
thumbnail_tag.short_description='تصویر'



class ArticleManager(models.Manager):
    def published(self):
        return self.filter(status='p')

class CategoryManager(models.Manager):
    def active(self):
        return self.filter(status=True)



class Category(models.Model):
    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='لینک')
    status=models.BooleanField(default=True,verbose_name='وضعیت')
    position=models.IntegerField(verbose_name='پوزیشن')

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'
        ordering=['position']

    def __str__(self):
        return self.title

    def category_published(self):
        return self.category.filter(status=True)

    objects=CategoryManager()










class Article(models.Model):
    STATUS_CHOICES=(
        ('d','Draft'),
        ('p','Publish'),
    )
    title=models.CharField(max_length=200,verbose_name='عنوان')
    slug=models.SlugField(max_length=100,unique=True,verbose_name='لینک')
    description=models.TextField(verbose_name='کپشن')
    thumbnail=models.ImageField(upload_to='images',verbose_name='تصویر')
    publish=models.DateTimeField(default=timezone.now,verbose_name='زمان انتشار')
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=1,choices=STATUS_CHOICES,verbose_name='وضعیت')
    rate=models.CharField(max_length=3,default=0,verbose_name='نمره')
    director=models.CharField(default='',max_length=20,verbose_name='کارگردان')
    stars=models.CharField(default='',max_length=100,verbose_name='ستارگان')
    release=models.CharField(default='',max_length=20,verbose_name='زمان انتشار فیلم')
    time=models.CharField(default='',max_length=10,verbose_name='زمان فیلم')
    age=models.CharField(default='PG-13',max_length=10,verbose_name='درجه سنی')
    star=models.BooleanField(default=False,verbose_name='برگزیده')
    category=models.ManyToManyField(Category,verbose_name='دسته بندی',related_name='articles')
    author=models.ForeignKey(User,null=True,on_delete=models.SET_NULL,related_name='articles',verbose_name='نویسنده')
    hits=models.ManyToManyField(IpAdderss,blank=True,related_name='hits',verbose_name='بازدیدها')
    comments = GenericRelation(Comment)
    def __str__(self):
        return self.title

    class Meta:
        verbose_name='مقاله'
        verbose_name_plural='مقالات'

    objects=ArticleManager()



