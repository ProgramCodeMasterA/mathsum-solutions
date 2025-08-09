from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(author=1)
    template_name = "forum/index.html"
    paginate_by = 6

def post_detail(request, problem):
    """
    Display an individual :model:`forum.Post`.

    **Context**

    ``post``
        An instance of :model:`forum.Post`.

    **Template:**

    :template:`forum/post_detail.html`
    """

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, problem=problem)

    return render(
        request,
        "forum/post_detail.html",
        {"post": post},
    )