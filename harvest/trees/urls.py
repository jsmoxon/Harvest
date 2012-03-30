from django.conf.urls.defaults import patterns, include, url
from django.views.generic.create_update import create_object
from forms import *
from models import Tree

urlpatterns = patterns('',
    url(r'^$', 'trees.views.home', name='home'),                                                                                
    url(r'volunteer_registration/', 'trees.views.volunteer_registration'),
    url(r'tree_registration/', 'trees.views.tree_by_owner'),
    url(r'add_house/', 'trees.views.house'),
#create_object, {'form_class': TreeByOwnerForm, 'template_name': 'tree_by_owner.html', 'post_save_redirect': '/'}),
    url(r'spotted_tree/', create_object, {'form_class': SpottedTreeForm, 'template_name': 'spotted_tree.html', 'post_save_redirect': '/spotted_list/'}),
    url(r'create_harvest/', create_object, {'form_class': CreateHarvestForm, 'template_name': 'create_harvest.html', 'post_save_redirect': '/'}),
    url(r'harvest_dash/(?P<entry_id>\d+)/', 'trees.views.harvest_detail'),                       
    url(r'planned_harvests', 'trees.views.planned_harvests'),
    url(r'tree_list/', 'trees.views.tree_list'),
    url(r'spotted_list/', 'trees.views.spotted_tree_list'),
    url(r'tree_review/(?P<entry_id>\d+)/', 'trees.views.review'),

)
