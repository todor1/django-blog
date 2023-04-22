from django.urls import path
from . import views

### adding namespace
app_name = 'blog'

urlpatterns = [
    #post views
    path("", views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),
]

'''URL patterns allow you to map URLs to views. A URL pattern is composed of a string pattern, a view,
and, optionally, a name that allows you to name the URL project-wide. Django runs through each URL
pattern and stops at the first one that matches the requested URL. Then, Django imports the view
of the matching URL pattern and executes it, passing an instance of the HttpRequest class and the
keyword or positional arguments.

In the preceding code, you define an application namespace with the app_name variable. This allows
you to organize URLs by application and use the name when referring to them. You define two different
patterns using the path() function. The first URL pattern doesn’t take any arguments and is mapped
to the post_list view. The second pattern is mapped to the post_detail view and takes only one
argument id , which matches an integer, set by the path converter int .

You use angle brackets to capture the values from the URL. Any value specified in the URL pattern
as <parameter> is captured as a string. You use path converters, such as <int:year> , to specifically
match and return an integer. For example <slug:post> would specifically match a slug (a string that
can only contain letters, numbers, underscores, or hyphens). You can see all path converters provid-
ed by Django at https://docs.djangoproject.com/en/4.1/topics/http/urls/#path-converters .

If using path() and converters isn’t sufficient for you, you can use re_path() instead to define complex
URL patterns with Python regular expressions. You can learn more about defining URL patterns with
regular expressions at https://docs.djangoproject.com/en/4.1/ref/urls/#django.urls.re_path .
If you haven’t worked with regular expressions before, you might want to take a look at the Regular
Expression HOWTO located at https://docs.python.org/3/howto/regex.html first.

Creating a urls.py file for each application is the best way to make your applications
reusable by other projects.
'''