from django.db.models import Q
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView, TemplateView

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

    def get_queryset(self):
        object_list = Entry.objects.filter(publish=True).order_by('-created')
        query = self.request.GET.get('q', None)

        if query:
            object_list = object_list.filter(Q(title__icontains=query) | Q(text__icontains=query))

        return object_list


class EntryView(DetailView):
    model = Entry
    template_name = "apps/blog/entry.html"


class AboutView(TemplateView):
    template_name = "apps/blog/about.html"