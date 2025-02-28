import factory
from django.contrib.auth.models import User
from ..blog.models import Post, Category

class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = 'test'
    username = 'test'
    is_superuser = True
    is_staff = True

class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post

    title = 'x'
    subtitle = 'x'
    slug = 'x'
    author = factory.SubFactory(UserFactory)
    body = 'x'
    status = 'published'

class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'x'