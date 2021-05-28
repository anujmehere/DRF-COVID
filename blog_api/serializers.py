from rest_framework import serializers
from blog.models import Post
from django.conf import settings

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'slug', 'author','image','excerpt', 'content', 'status','doc','qual','doc_add',
        'doc_phone','rem','oxy','t_oxy_bed','a_oxy_bed','t_icu_bed','a_icu_bed','email','phone','update_time')



class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'user_name', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}