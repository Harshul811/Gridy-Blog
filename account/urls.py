
from django.conf.urls import include, url

urlpatterns = [
    url(r'^home/$','account.views.home',name='home'),
    url(r'^article/$','article.views.articles',name='articles'),
    url(r'^article/addArticle/$','article.views.addArticle',name='addArticle'),
    
    url(r'^friends/$','account.views.friends',name='friends'),
    url(r'^logout/$','account.views.logoutview', name='logout'),
]
