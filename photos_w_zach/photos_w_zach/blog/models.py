from django.db import models
from django.contrib.auth.models import User

# Models describe a table that we will store in our database
class Category(models.Model):
    name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class Post(models.Model):
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=100)
    slug = models.SlugField(max_length=250, unique=True)     # Usable URL addressable string -- No special chars
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="post_author"
    )
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, editable=False)
    last_modified = models.DateTimeField(auto_now=True, editable=False)
    status = models.CharField(max_length=10, choices=options, default='draft')
    categories = models.ManyToManyField("Category", related_name="posts")
    # image = models.ImageField()

    class Meta:
        ordering = ('-created_on', )

    def __str__(self):
        return self.title
