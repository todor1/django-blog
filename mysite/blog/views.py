from django.shortcuts import render, get_object_or_404
# from django.http import Http404

# Create your views here.
from .models import Post

def post_list(request):
    '''This is our very first Django view. The post_list view takes the request object as the only parameter.
        This parameter is required by all views.
        In this view, we retrieve all the posts with the PUBLISHED status using the published manager that we
        created previously.
        Finally, we use the render() shortcut provided by Django to render the list of posts with the given
        template. This function takes the request object, the template path, and the context variables to render
        the given template. It returns an HttpResponse object with the rendered text (normally HTML code).
        The render() shortcut takes the request context into account, so any variable set by the template
        context processors is accessible by the given template. Template context processors are just callables
        that set variables into the context.
    '''
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, id):
    '''This is the post detail view. This view takes the id argument of a post. In the view, we try to retrieve
        the Post object with the given id by calling the get() method on the default objects manager. We
        raise an Http404 exception to return an HTTP 404 error if the model DoesNotExist exception is raised,
        because no result is found.
        Finally, we use the render() shortcut to render the retrieved post using a template.
    '''
    # try:
    #     post = Post.published.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404("No post found.")
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)    
    return render(request, "blog/post/detail.html", {"post": post})

