"""
factory_boy used to generate fake db entries resembling my models
    - find those in <photos_w_zach/tests/factories.py>
the factories were registered using pytest_factoryboy pip package
    - find those in <photos_w_zach/tests/conftest.py>
here the goal is to set a test (class) that will test the model's
ability to return its own name as specified in our __str__ methods
    - lines 11-12 in the Category model for example
    - find that in <photos_w_zach/blog/models.py>
the method in the test class TestCategoryModel will create a test category
and the assertion should be true if out code is functioning
"""
import pytest

pytestmark = pytest.mark.django_db

# Testing lines 11-12 in models.py
class TestCategoryModel:
    def test_str_return(self, category_factory):
        category = category_factory(name='test-category')
        assert category.__str__() == 'test-category'

class TestPostModel:
    def test_str_return(self, post_factory):
        post = post_factory(title='test-post')
        assert post.__str__() == 'test-post'