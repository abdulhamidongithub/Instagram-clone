from django.conf import settings
from django.contrib.auth.models import User
from django.db import models

class Account(models.Model):
    full_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    bio = models.CharField(max_length=150, blank=True)
    profile_pic = models.FileField(upload_to="profile_pics", blank=True)
    private = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="user_following", null=True)
    followers = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="user_followers", null=True)
    def __str__(self):
        return self.full_name
    def followerlar_soni(self):
        return self.followers.count()
    def following_soni(self):
        return self.following.count()


