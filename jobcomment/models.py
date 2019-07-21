from django.db import models
from django.utils import timezone

Category_select = (
    ('상식', '상식'),
    ('철학', '철학'),
    ('정치', '정치'),
)

class Blog(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null = True)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    body = models.TextField()
    category = models.CharField(max_length=20, choices = Category_select, default = '상식')
    created_date = models.DateTimeField(default=timezone.now)
    pub_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):

        return self.title

class Comment(models.Model):
    post = models.ForeignKey('jobcomment.Blog', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Login(models.Model):
    login_title = models.CharField(max_length=200)