from django.conf.urls.defaults import patterns, include, url
from django.views.generic.create_update import create_object
from forms import *
from models import Tree

urlpatterns = patterns('',
    url(r'^$', 'trees.views.home', name='home'),                                                                                
    url(r'volunteer_registration/', 'trees.views.volunteer_registration'),
    url(r'tree_registration/', 'trees.views.tree_by_owner'),
#create_object, {'form_class': TreeByOwnerForm, 'template_name': 'tree_by_owner.html', 'post_save_redirect': '/'}),
    url(r'spotted_tree/', create_object, {'form_class': SpottedTreeForm, 'template_name': 'spotted_tree.html', 'post_save_redirect': '/'}),
    url(r'create_harvest/', create_object, {'form_class': CreateHarvestForm, 'template_name': 'create_harvest.html', 'post_save_redirect': '/'}),
    url(r'tree_view/', 'trees.views.tree_view'),
    url(r'tree_review/(?P<entry_id>\d+)/', 'trees.views.review'),

)
