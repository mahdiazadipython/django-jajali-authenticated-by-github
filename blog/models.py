from django.db import models


from ckeditor.fields import RichTextField
from django_jalali.db import models as jmodels # تاریخ شمسی

from django.contrib.auth import get_user_model



class Post(models.Model):
    title    = models.CharField(max_length=200)
    author   = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    body     = RichTextField()
    publish  = jmodels.jDateField(auto_now_add=True) # تاریخ شمسی
    views_count = models.PositiveIntegerField(default=0)
    update = jmodels.jDateField(auto_now=True)

    class Meta:
        ordering = ("-publish",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment_by = models.CharField(max_length=200)
    comment_body = RichTextField()
    comment_created_on = jmodels.jDateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

      

    def __str__(self):
        return self.title
