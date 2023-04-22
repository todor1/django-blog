from django.contrib import admin

# Register your models here.
from .models import Post

# admin.site.register(Post)

# Customizing how models are displayed
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''We are telling the Django administration site that the model is registered in the site using a custom
    class that inherits from ModelAdmin . In this class, we can include information about how to display
    the model on the site and how to interact with it.
    The list_display attribute allows you to set the fields of your model that you want to display on the
    administration object list page. The @admin.register() decorator performs the same function as the
    admin.site.register() function that you replaced, registering the ModelAdmin class that it decorates.
    '''
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
'''You can see that the fields displayed on the post list page are the ones we specified in the list_display
    attribute. The list page now includes a right sidebar that allows you to filter the results by the fields
    included in the list_filter attribute.
    A search bar has appeared on the page. This is because we have defined a list of searchable fields using
    the search_fields attribute. Just below the search bar, there are navigation links to navigate through
    a date hierarchy; this has been defined by the date_hierarchy attribute. You can also see that the
    posts are ordered by STATUS and PUBLISH columns by default. We have specified the default sorting
    criteria using the ordering attribute.
    Chapter 1/p29
    Next, click on the ADD POST link. You will also note some changes here. As you type the title of a new
    post, the slug field is filled in automatically. You have told Django to prepopulate the slug field with
    the input of the title field using the prepopulated_fields attribute:
'''