#!/usr/bin/env python

import webbrowser
import os
import time

import dropbox

app_key = os.environ.get("DROPBOX_APP_KEY")
app_secret = os.environ.get("DROPBOX_APP_SECRET")

if not app_key and not app_secret:
    print """
You need an dropbox app key. You can create one at
http://dropbox.com/developers
"""

if not app_key:
    app_key = raw_input("Enter the dropbox app key: ").strip()

if not app_secret:
    app_secret = raw_input("Enter the dropbox app secret: ").strip()

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

authorize_url = flow.start()

print 'Retreiving OAuth token.'
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'

time.sleep(5)
webbrowser.open(authorize_url)

code = raw_input("Enter the authorization code here: ").strip()

try:
    access_token, user_id = flow.finish(code)
    # v gbhnm,

print("The user_id is: " + user_id)
print "And the access token is: " + access_token
