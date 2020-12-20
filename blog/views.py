from django.shortcuts import render 

from .models import Post ,Comment


from django.views.generic import (
    ListView
)


class PageContextMixin(object):
    page_title = None

    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        return context


class Home(PageContextMixin , ListView):
    model = Post
    template_name = "blog/list.html"
    context_object_name = 'posts'
    paginate_by = 3
    page_title = 'Home'
