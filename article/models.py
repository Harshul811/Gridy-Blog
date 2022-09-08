from django.db import models
from account.models import MyUser

class Article(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=100)
    content = models.CharField(max_length=500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField()


class FavArticle(models.Model):
    def __str__(self):
        return self.author + self.article

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    article= models.ForeignKey(Article, on_delete= models.CASCADE)