from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'teams.views.hello', name='home'),
#    url(r'^select/', 'teams.views.select', name='select'),
    url(r'^create/', 'teams.views.create', name='create'),
    url(r'harvest_dash/(?P<entry_id>\d+)/', 'teams.views.harvest_detail'),                       
    url(r'harvest_review/(?P<entry_id>\d+)/', 'teams.views.harvest_review'),                       
    url(r'planned_harvests', 'teams.views.planned_harvests'),
    url(r'^signup/(?P<entry_id>\d+)/', 'teams.views.signup'),                        
)
