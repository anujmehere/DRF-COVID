from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings
from django.utils.translation import gettext_lazy as _ 

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset() .filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    image = models.ImageField(_("Image"), upload_to=upload_to, default='posts/default.JPG')
    
    excerpt = models.TextField(null=True)
    content = models.TextField()
    #DOC_DETAILS
    doc = models.CharField(max_length=50,default="Dr")
    qual = models.CharField(max_length=12,default="M.B.B.S.")
    doc_add = models.CharField(max_length=50,default="Clinic Centre")
    doc_phone = models.CharField(max_length=15, default="")
    # remdisvir
    # oxygen
    # tot oxygen bed
    #tot icu
    #aval oxy bed
    # aval icu
    rem = models.IntegerField(default="0")
    oxy = models.CharField(max_length=10,default="0")
    t_oxy_bed = models.IntegerField(default="0")
    a_oxy_bed = models.IntegerField(default="0")
    t_icu_bed = models.IntegerField(default="0")
    a_icu_bed = models.IntegerField(default="0")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=15, default="")
    update_time = models.DateTimeField(auto_now_add=True,null=True)
    ###########################
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager()  # default manager
    postobjects = PostObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
