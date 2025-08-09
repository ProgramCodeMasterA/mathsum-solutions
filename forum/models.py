from django.db import models
from django.contrib.auth.models import User


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
    problem = models.CharField(max_length=100, unique=True) # Type in the mathematical content of your math problem
    context = models.TextField(max_length=200) # Type in what answer you expect to get when this mathematical problem is solved
    area = models.CharField(max_length=15, choices=MATH_CHOICES, default='arithmetic')  # Choose which category of Maths the problem is
    difficulty = models.CharField(max_length=10, choices=DIFFICULTY_CHOICES, default='low')  # Choose perceived difficulty of problem
    solved = models.BooleanField(default=False)    # True/False if math problem is solved or not
    created_on = models.DateTimeField(auto_now_add=True)    # Add DateTime field for when post is created
    updated_on = models.DateTimeField(auto_now_add=True)    # Add DateTime field for when post is updated

    class Meta:
        ordering = ["-created_on"]
    
    def __str__(self):
        return f"{self.problem} | written by {self.author}"


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    response = models.TextField(max_length=200)     # Response to user's post
    resolution = models.BooleanField(default=False)     # True/False if reply gives correct solution for math problem
    created_on = models.DateTimeField(auto_now_add=True)    # Add DateTime field for when comment is created

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.response} by {self.author}"