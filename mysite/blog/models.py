from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)

class Post(models.Model):
    
    class Status(models.TextChoices):
        '''We have defined the enumeration class Status by subclassing models.TextChoices . The available
        choices for the post status are DRAFT and PUBLISHED . Their respective values are DF and PB , and their
        labels or readable names are Draft and Published.
        Django provides enumeration types that you can subclass to define choices simply. These are based on
        the enum object of Python’s standard library. You can read more about enum at https://docs.python.
        org/3/library/enum.html .
        Django enumeration types present some modifications over enum . You can learn about those differences
        at https://docs.djangoproject.com/en/4.1/ref/models/fields/#enumeration-types .
        We can access Post.Status.choices to obtain the available choices, Post.Status.labels to obtain
        the human-readable names, and Post.Status.values to obtain the actual values of the choices.
        We have also added a new status field to the model that is an instance of CharField . It includes a
        choices parameter to limit the value of the field to the choices in Status.choices . We have also set a
        default value for the field using the default parameter. We use DRAFT as the default choice for this field.
        
        It’s a good practice to define choices inside the model class and use the enumeration types.
        This will allow you to easily reference choice labels, values, or names from anywhere in
        your code. You can import the Post model and use Post.Status.DRAFT as a reference
        for the Draft status anywhere in your code.
        '''
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    '''We have imported the User model from the django.contrib.auth.models module and we have added
        an author field to the Post model. This field defines a many-to-one relationship, meaning that each
        post is written by a user, and a user can write any number of posts. For this field, Django will create
        a foreign key in the database using the primary key of the related model.
        The on_delete parameter specifies the behavior to adopt when the referenced object is deleted. This
        is not specific to Django; it is an SQL standard. Using CASCADE , you specify that when the referenced
        user is deleted, the database will also delete all related blog posts. You can take a look at all the possi-
        ble options at https://docs.djangoproject.com/en/4.1/ref/models/fields/#django.db.models.
        ForeignKey.on_delete .
        We use related_name to specify the name of the reverse relationship, from User to Post . This will
        allow us to access related objects easily from a user object by using the user.blog_posts notation.
    '''
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True) #saved automatically when creating an object.
    updated = models.DateTimeField(auto_now=True) #updated automatically when saving an object
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)
    '''The first manager declared in a model becomes the default manager. You can use the Meta attribute
        default_manager_name to specify a different default manager. If no manager is defined in the model,
        Django automatically creates the objects default manager for it. If you declare any managers for
        your model, but you want to keep the objects manager as well, you have to add it explicitly to your
        model. In the preceding code, we have added the default objects manager and the published custom
        manager to the Post model.
        The get_queryset() method of a manager returns the QuerySet that will be executed. We have over-
        ridden this method to build a custom QuerySet that filters posts by their status and returns a successive
        QuerySet that only includes posts with the PUBLISHED status.
    '''
    objects = models.Manager()  ## the default manager
    published = PublishedManager()  ## our custom manager

    
    class Meta:
        '''This class defines metadata for the model. 
            We use the ordering attribute to tell Django that it should sort results by the publish field. This ordering will
            apply by default for database queries when no specific order is provided in the query. We indicate
            descending order by using a hyphen before the field name, -publish . Posts will be returned in reverse
            chronological order by default.
            --------------------------------
            We have added the indexes option to the model’s Meta class. This option allows you to define database
            indexes for your model, which could comprise one or multiple fields, in ascending or descending
            order, or functional expressions and database functions. We have added an index for the publish
            field. We use a hyphen before the field name to define the index in descending order. The creation of
            this index will be included in the database migrations that we will generate later for our blog models.
        '''
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]
        
    def __str__(self) -> str:
        return self.title



############################################################################################
''' 
We just applied migrations for the applications listed in INSTALLED_APPS , including the blog application.
After applying the migrations, the database reflects the current status of the models.
If you edit the models.py file in order to add, remove, or change the fields of existing models, or if you
add new models, you will have to create a new migration using the makemigrations command. Each
migration allows Django to keep track of model changes. Then, you will have to apply the migration
using the migrate command to keep the database in sync with your models.

python manage.py makemigrations blog
python manage.py sqlmigrate blog 0001
python manage.py migrate
'''

'''Creating an administration site for models
Now that the Post model is in sync with the database, we can create a simple administration site to
manage blog posts.
Django comes with a built-in administration interface that is very useful for editing content. The Django
site is built dynamically by reading the model metadata and providing a production-ready interface for
editing content. 
You can use it out of the box, configuring how you want your models to be displayed in it.
The django.contrib.admin application is already included in the INSTALLED_APPS setting, so you don’t need to add it.

python manage.py createsuperuser
'''
############################################################################################