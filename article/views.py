from django.shortcuts import render,redirect
from article.forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
@login_required
@require_http_methods(['GET','POST'])
def artciles(request):
  if request.method=='GET':
    return render(request,'article/allArticles.html');


@require_http_methods(['GET','POST'])
@login_required
def addArticle(request):
  if(request.method=='GET'):
    f=ArticleForm()
    return render(request,'article/addArticle.html',{'nForm':f});
  else:
    f=ArticleForm(request.POST,request.FILES)
    if f.is_valid(): 
      article=f.save(commit=False)
      article.author=request.user
      article.save()
      return redirect('articles')
    else:
      return render(request,'article/addArticle.html',{'nForm':f});  



