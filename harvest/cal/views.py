from django.shortcuts import render_to_response, get_object_or_404, HttpResponse, redirect

import gflags
import httplib2
import json

from apiclient.discovery import build
from oauth2client.file import Storage
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.tools import run

FLAGS = gflags.FLAGS

# Set up a Flow object to be used if we need to authenticate. This
# sample uses OAuth 2.0, and we set up the OAuth2WebServerFlow with
# the information it needs to authenticate. Note that it is called
# the Web Server Flow, but it can also handle the flow for native
# applications
# The client_id and client_secret are copied from the API Access tab on
# the Google APIs Console
def cal(request):
    print "start"
    FLOW = OAuth2WebServerFlow(
        client_id='291668763217-4em7iq2trgp3it8it22i5cspaumg7bna.apps.googleusercontent.com',
        client_secret='5VO3Nf2wSdzEeceneHMWvCWg',
        scope='https://www.googleapis.com/auth/calendar',
        redirect_uri = 'http://localhost:8000/oauth2callback',
        user_agent='cal/1')
    print FLOW
# To disable the local server feature, uncomment the following line:
# FLAGS.auth_local_webserver = False

# If the Credentials don't exist or are invalid, run through the native client
# flow. The Storage object will ensure that if successful the good
# Credentials will get written back to a file.
    print "about to store"
    storage = Storage('calendar.dat')
    credentials = storage.get()
    print "credentials"
    if credentials is None or credentials.invalid == True:
        credentials = run(FLOW, storage)
        print "in cred if"
# Create an httplib2.Http object to handle our HTTP requests and authorize it
# with our good Credentials.
        http = httplib2.Http()
        http = credentials.authorize(http)

# Build a service object for interacting with the API. Visit
# the Google APIs Console
# to get a developerKey for your own application.
        service = build(serviceName='calendar', version='v3', http=http,
                        developerKey='AIzaSyCxf_ljx73homsazrdtygO9LF2Vpa9GVWE')
        print "service built"
        event = {
            'summary': 'Appointment',
            'location': 'Somewhere',
            'start': {
                'dateTime': '2012-03-29T10:00:00.000-07:00'
                },
            'end': {
                'dateTime': '2011-03-29T10:25:00.000-07:00'
                },
            'attendees': [
                {
                    'email': 'jsmoxon@gmail.com',
                    # Other attendee's data...
                    },
                # ...
                ],
            }
        print event
        created_event = service.events().insert(calendarId='9lt2oheg4tke9tmps856c97kj0@group.calendar.google.com', body=event).execute()
        print created_event['id']
        return redirect('/')
    return redirect('/')
def auth_return(request):
    return render_to_response("oauth.html")
