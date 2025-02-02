from pytest_factoryboy import register
from .factories import PostFactory, CategoryFactory

register(PostFactory)
register(CategoryFactory)
