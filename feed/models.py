from django.conf import settings
from django.db import models

class Media(models.Model):
    media = models.FileField(upload_to="post_uchun")

class Post(models.Model):
    media = models.ManyToManyField(Media)
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="account_posts")
    tag = models.ManyToManyField(settings.ACC, blank=True, related_name="account_tags")
    matn = models.CharField(max_length=300,blank=True)
    joy = models.CharField(max_length=300,blank=True)
    vaqt = models.DateTimeField(auto_now_add=True)

class Like(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Saved(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

class Comment(models.Model):
    matn = models.CharField(max_length=50)
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    vaqt = models.DateTimeField(auto_now_add=True)

class Comment_like(models.Model):
    account = models.ForeignKey(settings.ACC, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)

class Message(models.Model):
    matn = models.CharField(max_length=50, blank=True)
    yuboruvchi = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="message_yuboruvchi")
    qabul = models.ForeignKey(settings.ACC, on_delete=models.CASCADE, related_name="message_qabul")
    vaqt = models.DateTimeField(auto_now_add=True)
    media = models.ForeignKey(Media, on_delete=models.CASCADE, blank=True)


