from django.conf.urls import url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^profile$', views.profile, name='profile'),
    url(r'^resume$', views.resume, name='resume'),
]
