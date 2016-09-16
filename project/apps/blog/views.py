from django.views.generic import ListView, DetailView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from project.apps.blog.models import Entry


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view, login_url=reverse_lazy("auth"))


class BlogView(ListView):
    model = Entry
    template_name = "apps/blog/blog.html"
    paginate_by = 10


class EntryView(DetailView):
    model = Entry
    template_name = "apps/blog/entry.html"
