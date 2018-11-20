from django.conf.urls import url
from calvin import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^cv/', views.cv, name='cv'),

    url(r'category/(?P<category_name_slug>[\w\-]+)/$',
        views.show_category, name='show_category'),

]
