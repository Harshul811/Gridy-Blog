from django import forms
from article.models import Article

#Create you forms here
class ArticleForm(forms.ModelForm):
  class Meta:
    model=Article
    exclude=['likes']
