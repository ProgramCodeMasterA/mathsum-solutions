from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))
DIFFICULTY_CHOICES = (('low','Low'),
    ('moderate', 'Moderate'),
    ('high', 'High'),
    ('master', 'Master'))
MATH_CHOICES = (('arithmetic', 'Arithmetic'),
    ('algebra', 'Algebra'),
    ('analysis', 'Analysis'),
    ('calculus', 'Calculus'),
    ('combinatorics', 'Combinatorics'),
    ('geometry', 'Geomoetry'),
    ('probability', 'Probability'),
    ('topology', 'Topology'))

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="forum_posts"
    )
    content = models.CharField(max_length=100, unique=True) # Type in the mathematical content of your math problem
    context = models.TextField(max_length=200) # Type in what answer you expect to get when this mathematical problem is solved
    area = models.CharField(max_length=15, choices=MATH_CHOICES, default='arithmetic')  # Choose which category of Maths the problem is
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='low')  # Choose perceived difficulty of problem
    resolution = models.BooleanField(default=False)    # True/False if math problem is solved
    created_on = models.DateTimeField(auto_now_add=True)    # Add DateTime field for when post is created
    updated_on = models.DateTimeField(auto_now_add=True)    # Add DateTime field for when post is updated
    status = models.IntegerField(choices=STATUS, default=0) # Define if object is a draft or is published post
