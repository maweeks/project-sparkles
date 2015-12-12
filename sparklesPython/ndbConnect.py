#!/usr/bin/env python
#
# Copyright 2015 Matt Weeks
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

from google.appengine.ext import ndb

class Account(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    spotify = ndb.StringProperty(indexed=False)
    autoHide = ndb.BooleanProperty(indexed=False)

class Profile(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    type = ndb.StringProperty(indexed=False)
    sites = ndb.StringProperty(indexed=False)
    playlist = ndb.StringProperty(indexed=False)
    default = ndb.BooleanProperty(indexed=True)


def createAccountData(email):
    account = Account()
    account.spotify = ""
    account.email = email
    account.autoHide = False
    account.put()

def checkForAccount(email):
    account_query = Account.query(Account.email == email)
    account = account_query.fetch(1)
    return account[0]

def forceAccount(email):
    if not checkForAccount(email):
        createAccountData(email)
    return checkForAccount(email)

def printAccountForm(account):
    checked = ""
    if account.autoHide:
        checked = " checked"

    contents = """<div class="col-md-12">
                <h6>Account details:</h6>
                <em><b>Email: </b></em>""" + account.email + """<br/>
                <em><b>Spotify details: </b></em>""" + account.spotify

    contents += """<form class='form' action="/settings/generalSend" method="post">
                    <h6>Settings: </h6>
                    <label class="checkbox" for="autohide">
                    <input type="checkbox" data-toggle="checkbox" value="True" id="autohide" name="autohide" class="custom-checkbox" """ + checked + """><span class="icons"><span class="icon-unchecked"></span><span class="icon-checked"></span></span>
                    <em><b>Close autorun tab after completion</b></em>
                    </label>
                    <div><br/>
                    <input class='btn btn-primary' type="submit" value="Save Changes">
                    <button type="button" class="btn btn-default" onclick="location.reload();">Cancel Changes</button>
                    </div>
                    </form>
                    </div>"""

    return contents

def updateAccount(email, autohide, spotify):
    account = checkForAccount(email)
    changed = False
    if (account.autoHide != autohide):
        account.autoHide = autohide
        changed = True
    if (account.spotify != spotify):
        account.spotify = spotify
        changed = True
    if changed:
        account.put()


def createProfileData(email, name, type, sites, playlist, default):
    profile = Profile()
    profile.email = email
    profile.name = name
    profile.type = type
    profile.sites = sites
    profile.playlist = playlist
    profile.default = default
    profile.put()

def checkForProfile(email, name):
    profile_query = Profile.query(Profile.email == email).query(Profile.name == name)
    profile = account_query.fetch(1)
    return profile[0]

def printProfileForm(profile):
    contents = "Name: " + profile.name
    contents += "<br/>Type: " + profile.type
    contents += "<br/>Sites: " + profile.sites
    contents += "</br>Playlist: " + profile.playlist
    contents += "</br>Default: " + str(profile.default)
    return contents

def printProfileList(profile):
    contents = "Name: " + profile.name
    contents += "<br/>Type: " + profile.type
    contents += "<br/>Sites: " + profile.sites
    contents += "</br>Playlist: " + profile.playlist
    contents += "</br>Default: " + str(profile.default)
    return contents

def updateProfile(email, name, newName, type, sites, playlist, default):
    profile = checkForProfile(email, name)
    changed = False
    if (profile.name != newName):
        profile.name = newName
        changed = True
    if (profile.type != type):
        profile.type = type
        changed = True
    if (profile.sites != sites):
        profile.sites = sites
        changed = True
    if (profile.playlist != playlist):
        profile.playlist = playlist
        changed = True
    if (profile.default != default):
        profile.default = default
        changed = True
    if changed:
        profile.put()