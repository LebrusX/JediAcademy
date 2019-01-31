from django.conf.urls import url

from . import views

app_name = 'jedi'                     # пространство имен для определения url в html -> {% url 'jedi:list'...
urlpatterns = (
    url(r'^$', views.main, name='main'),
    url(r'^jedi/$', views.JediView.as_view(), name='jedi'),
    url(r'^jedi/(?P<pk>\d+)$', views.ListOfCandsView.as_view(), name='list'),
    url(r'^candidate-form/$', views.ResumeView.as_view(), name='resume'),

    # url(r'^candidate-form/test', views.test, name='test'),
    # url(r'^candidate-form/(?P<pk>\d+)', views.CandidateView.as_view(), name='test'),

    url(r'^candidate-form/test/(?P<pk>\d+)', views.TestView.as_view(), name='test'),
    url(r'^candidate-form/test/(?P<pk>\d+)/thanks$', views.thanks, name='thanks'),

)
