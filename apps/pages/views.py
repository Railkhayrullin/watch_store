from django.views.generic import ListView, DetailView

from apps.pages.models import News


class BlogListView(ListView):
    paginate_by = 3
    model = News
    template_name = 'watch/blog.html'


class BlogDetailView(DetailView):
    model = News
    template_name = 'watch/blog_detail.html'
