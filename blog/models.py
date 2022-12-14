from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from users.models import Profile, Interests
from django import forms


GEEKS_CHOICES =(
    ("Feedback", "Feedback"),
    ("Request", "Request"),
)
  

class Post(models.Model):
    name = models.TextField(max_length=512, default="")
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now())
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    interest = models.OneToOneField(Interests, on_delete=models.CASCADE, null=True, blank=True)
    participants = models.ManyToManyField(Profile, blank=True)
    score = models.IntegerField(null=False, blank=False, default=10)

    class Meta:
        verbose_name_plural = "Posts"

    def __str__(self):
        return self.name

    @property
    def number_of_comments(self):
        return Comment.objects.filter(post_connected=self).count()


class Feedback(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=1000)
    date_posted = models.DateTimeField(default=timezone.now())
    option = models.CharField(max_length=15, choices = GEEKS_CHOICES, default="Feedback")

    class Meta:
        verbose_name_plural = "Posts"
        ordering = ['-date_posted']

    def __str__(self):
        return str(self.author) + ' ' + str(self.option)

class Comment(models.Model):
    content = models.TextField(max_length=150)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_connected = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.author) + " " + str(self.content)

