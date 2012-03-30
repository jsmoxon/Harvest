from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'teams.views.hello', name='home'),
#    url(r'^select/', 'teams.views.select', name='select'),
    url(r'^create/', 'teams.views.create', name='create'),
#    url(r'harvest/(?P<entry_id>\d+)/', 'teams.views.harvest_detail'),                       
    url(r'^signup/(?P<entry_id>\d+)/', 'teams.views.signup'),                        
)
