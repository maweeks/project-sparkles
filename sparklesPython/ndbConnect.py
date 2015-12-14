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
import runScripts as rs
import time

class Account(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    spotify = ndb.StringProperty(indexed=False)
    autoHide = ndb.BooleanProperty(indexed=False)

class ProfileSite(ndb.Model):
    """A main model for representing an individual Profile entry."""
    site = ndb.StringProperty(indexed=True)

class Profile(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    type = ndb.StringProperty(indexed=False)
    sites = ndb.StructuredProperty(ProfileSite, repeated=True)
    playlist = ndb.StringProperty(indexed=False)
    default = ndb.BooleanProperty(indexed=True)

class Location(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    name = ndb.StringProperty(indexed=True)
    type = ndb.StringProperty(indexed=False)
    gpsLat = ndb.FloatProperty(indexed=True)
    gpsLong = ndb.FloatProperty(indexed=True)
    gpsRange = ndb.IntegerProperty(indexed=True)
    profileName = ndb.StringProperty(indexed=True)

# Account methods

def checkForAccount(email):
    account_query = Account.query(Account.email == email)
    account = account_query.fetch(1)
    if account:
        return account[0]
    else:
        return False

def createAccountData(email):
    account = Account()
    account.spotify = ""
    account.email = email
    account.autoHide = False
    account.put()

def forceAccount(email):
    if not checkForAccount(email):
        createAccountData(email)
    time.sleep(0.1)
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

# Profile methods

def checkForProfile(email, name):
    profile_query = Profile.query(Profile.email == email, Profile.name == name)
    profile = profile_query.fetch(1)
    if profile:
        return profile[0]
    else:
        return False

def createProfileData(email, name, type, sites, playlist, default):
    profile = Profile()
    profile.email = email
    profile.name = name
    profile.type = type
    profile.sites = []
    for site in sites:
        siteX = ProfileSite()
        siteX.site = site
        profile.sites.append(siteX)
    profile.playlist = playlist
    profile.default = default
    if default:
        removeDefaultProfile(email)
    profile.put()

def deleteProfile(name, email):
    profile = checkForProfile(email, name)
    if profile:
        profile.put().delete()

def getAllProfiles(email):
    profile_query = Profile.query(Profile.email == email).order(-Profile.default,Profile.name)
    profiles = profile_query.fetch(20)
    return profiles

def getDefaultProfile(email):
    profile_query = Profile.query(Profile.default == True, Profile.email == email)
    profile = profile_query.fetch(1)
    if profile:
        return profile[0]
    else:
        return False

def noProfiles():
    content = "<div class='col-md-12 text-center'><h6>No profiles found, please add some by following <a href='/settings/profiles.html'>this link</a>.</h6></div>"
    return content

def printCurrentProfileForm(profile):
    name = profile.name
    type = profile.type
    sites = ""
    for site in profile.sites:
        sites+= site.site
    playlist = profile.playlist
    default = profile.default

    return printProfileForm("Profile " + name, name, type, sites, playlist, default)

def printNewProfileForm(email):
    checked = False
    if not getDefaultProfile(email):
        checked = True
    return printProfileForm("Create new profile", "", "Home", "", "", checked)

def printProfileForm(title, name, type, sites, playlist, default):
    optionList = ""
    options = ["Home", "Work", "Travel", "Social", "Other"]
    selected = ""
    deleteForm = ""
    defaultHighlight = ""

    if default:
        defaultHighlight = " defaultThumbnail"

    if name == "":
        profileName = """<div class="col-lg-10">
                    <input class="form-control" id="name" name="name" required placeholder="Name">"""
    else:

        deleteForm = """<button type="button" class="btn btn-danger" onclick="document.getElementById('form""" + name + """').action='/settings/profileDelete';document.getElementById('form""" + name + """').submit();">Delete Profile</button>"""
        profileName = """<div class="col-lg-10 formItemText">
                        <b>""" + name + """</b><input type="hidden" class="form-control" id="name" name="name" required placeholder="Name" value='""" + name + """'>"""

    for option in options:
        if type == option:
            selected = " selected"
        else:
            selected = ""
        optionList += "<option" + selected + " value='" + option + "'>" + option + "</option>"

    checked = ""
    if default:
        checked = " checked"

    contents = """<div class="col-md-12"><div class='thumbnail formThumbnail""" + defaultHighlight + """'>
                    <h6>""" + title + """: </h6>
                    <form class='form form-horizontal' action="/settings/profileSend"  id='form""" + name + """' method="post">

                    <div class="form-group">
                    <label for="name" class="col-lg-2 control-label"><em><b>Name</b></em></label>
                    """ + profileName + """
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="name" class="col-lg-2 control-label"><em><b>Type</b></em></label>
                    <div class="col-lg-10">
                    <select class="form-control select select-primary select-block mbl" name="type">
                    """ + optionList + """
                    </select>
                    <script> $("select").select2({dropdownCssClass: 'dropdown-inverse'}); </script>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="sites" class="col-lg-2 control-label"><em><b>Sites</b></em></label>
                    <div class="col-lg-10">
                    <textarea class="form-control" id="sites" name="sites" required rows="3" placeholder="Sites">""" + sites + """</textarea>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="playlist" class="col-lg-2 control-label"><em><b>Playlist</b></em></label>
                    <div class="col-lg-10">
                    <input class="form-control" id="playlist" name="playlist" placeholder="Playlist" value='""" + playlist + """'>
                    </div>
                    </div>

                    <div class="form-group">
                    <div class="col-lg-offset-2 col-lg-10">
                    <label class="checkbox" for='check""" + name + """' >
                    <input id='check""" + name + """' type="checkbox" data-toggle="checkbox" value="True" name="defaultProfile" class="custom-checkbox" """ + checked + """><span class="icons"><span class="icon-unchecked"></span><span class="icon-checked"></span></span>
                    <em><b>Make default</b></em>
                    </label>
                    </div></div>

                    <div class="form-group">
                    <div class="col-lg-offset-2 col-lg-10">
                    <input class='btn btn-primary' type="submit" value="Save Changes">
                    <button type="button" class="btn btn-default" onclick="location.reload();">Cancel Changes</button>
                    """ + deleteForm + """
                    </div></div>

                    </form></div></div>"""
    return contents

def printProfileList(profile, solo):
    defaultHighlight = ""
    if profile.default:
        defaultHighlight = " defaultThumbnail"

    sites = ""
    siteFunction = rs.generateProfileScript(profile)
    for site in profile.sites:
        sites+= "<a href='" + site.site + "' target='_blank'>" + site.site + "</a><br/>"

    soloClasses = ""
    if solo:
        soloClasses = " col-sm-offset-3 col-md-offset-4"

    contents = """<div class='col-sm-6 col-md-4 """ + soloClasses + """'><div class='thumbnail """ + defaultHighlight + """'>
                <button class="btn btn-primary" onclick=" """ + siteFunction + """ ">Run Profile</button>
                <a href="/settings/profiles.html"><button class="btn btn-default">Edit Profile</button></a>
                <br/><br/>
                <b><em>Name: </em> """ + profile.name + """</b><br/>
                <b><em>Type: </em></b> """ + profile.type + """<br/>
                <b><em>Sites: </em></b> """ + sites + """
                <b><em>Playlist: </em></b> """ + profile.playlist + """<br/>
                <b><em>Default: </em></b> """ + str(profile.default) + """
                </div></div>
                """
    return contents

def removeDefaultProfile(email):
    profile = getDefaultProfile(email)
    if profile:
        profile.default = False
        profile.put()

def updateProfile(email, name, newName, type, sites, playlist, default):
    profile = checkForProfile(email, name)
    changed = False
    if (profile.name != newName):
        profile.name = newName
        changed = True
    if (profile.type != type):
        profile.type = type
        changed = True

    # TODO: Check if same
    profile.sites = []
    for site in sites:
        siteX = ProfileSite()
        siteX.site = site
        profile.sites.append(siteX)
    changed = True

    if (profile.playlist != playlist):
        profile.playlist = playlist
        changed = True
    if (profile.default != default):
        profile.default = default
        if default:
            removeDefaultProfile(email)
        changed = True
    if changed:
        profile.put()

# Location methods

def checkForLocation(email, name):
    location_query = Location.query(Location.email == email, Location.name == name)
    location = location_query.fetch(1)
    if location:
        return location[0]
    else:
        return False
    return False

def createLocationData(email, name, type, gpsLat, gpsLong, gpsRange, profileName):
    location = Location()
    location.email = email
    location.name = name
    location.type = type
    location.gpsLat = gpsLat
    location.gpsLong = gpsLong
    location.gpsRange = gpsRange
    location.profileName = profileName
    location.put()

def deleteLocation(name, email):
    location = checkForLocation(email, name)
    if location:
        location.put().delete()

def getAllLocations(email):
    location_query = Location.query(Location.email == email).order(Location.name)
    locations = location_query.fetch(20)
    return locations

def printCurrentLocationForm(location):
    name = location.name
    type = location.type
    gpsLat = location.gpsLat
    gpsLong = location.gpsLong
    gpsRange = location.gpsRange
    profileName = location.profileName
    return printLocationForm("Location " + name, name, type, gpsLat, gpsLong, gpsRange, profileName)

def printNewLocationForm(email):
    content = printLocationForm("Add new location", "", "Home", "", "", 20, "")
    return content

def printLocationForm(title, name, type, gpsLat, gpsLong, gpsRange, profileNameX):
    optionList = ""
    options = ["Home", "Work", "Travel", "Social", "Other"]
    selected = ""
    deleteForm = ""

    if name == "":
        profileName = """<div class="col-lg-10">
                    <input class="form-control" id="name" name="name" required placeholder="Name">"""
    else:

        deleteForm = """<button type="button" class="btn btn-danger" onclick="document.getElementById('form""" + name + """').action='/settings/locationDelete';document.getElementById('form""" + name + """').submit();">Delete Profile</button>"""
        profileName = """<div class="col-lg-10 formItemText">
                        <b>""" + name + """</b><input type="hidden" class="form-control" id="name" name="name" required placeholder="Name" value='""" + name + """'>"""

    for option in options:
        if type == option:
            selected = " selected"
        else:
            selected = ""
        optionList += "<option" + selected + " value='" + option + "'>" + option + "</option>"

    contents = """<div class="col-md-12"><div class='thumbnail formThumbnail'>
                    <h6>""" + title + """: </h6>
                    <form class='form form-horizontal' action="/settings/locationSend"  id='form""" + name + """' method="post">

                    <div class="form-group">
                    <label for="name" class="col-lg-2 control-label"><em><b>Name</b></em></label>
                    """ + profileName + """
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="name" class="col-lg-2 control-label"><em><b>Type</b></em></label>
                    <div class="col-lg-10">
                    <select class="form-control select select-primary select-block mbl" name="type">
                    """ + optionList + """
                    </select>
                    <script> $("select").select2({dropdownCssClass: 'dropdown-inverse'}); </script>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="gpsLat" class="col-lg-2 control-label"><em><b>Latitude</b></em></label>
                    <div class="col-lg-10">
                    <input class="form-control" id="gpsLat" name="gpsLat" required placeholder="Latitude" value=""" + str(gpsLat) + """>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="gpsLong" class="col-lg-2 control-label"><em><b>Longitude</b></em></label>
                    <div class="col-lg-10">
                    <input class="form-control" id="gpsLong" name="gpsLong" required placeholder="Longitude" value=""" + str(gpsLong) + """>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="gpsRange" class="col-lg-2 control-label"><em><b>Range</b></em></label>
                    <div class="col-lg-10">
                    <input class="form-control" id="gpsRange" name="gpsRange" required placeholder="Range" value=""" + str(gpsRange) + """>
                    </div>
                    </div>

                    <div class="form-group">
                    <label for="profileNameX" class="col-lg-2 control-label"><em><b>Profile name</b></em></label>
                    <div class="col-lg-10">
                    <input class="form-control" id="profileNameX" name="profileNameX" required placeholder="Profile name" value=""" + profileNameX + """>
                    </div>
                    </div>

                    <div class="form-group">
                    <div class="col-lg-offset-2 col-lg-10">
                    <input class='btn btn-primary' type="submit" value="Save Changes">
                    <button type="button" class="btn btn-default" onclick="location.reload();">Cancel Changes</button>
                    """ + deleteForm + """
                    </div></div>

                    </form></div></div>"""
    return contents

def updateLocation(email, name, newName, type, gpsLat, gpsLong, gpsRange, profileName):
    location = checkForLocation(email, name)
    changed = False
    if (location.name != newName):
        location.name = newName
        changed = True
    if (location.type != type):
        location.type = type
        changed = True
    if (location.gpsLat != gpsLat):
        location.gpsLat = gpsLat
        changed = True
    if (location.gpsLong != gpsLong):
        location.gpsLong = gpsLong
        changed = True
    if (location.gpsRange != gpsRange):
        location.gpsRange = gpsRange
        changed = True
    if (location.profileName != profileName):
        location.profileName = profileName
        changed = True

    if changed:
        location.put()

def getGPSProfile(email, gps):
    # search
    location_query = Location.query(Location.email == email)
    locations = location_query.fetch(20)
    if locations:
        bestLocation = ""
        bestLocationDistance = 9999999999999999999
        for location in locations:
            print("a")
            print(rs.getGPSm(gps[0], gps[1], location.gpsLat, location.gpsLong))
            print(location.gpsRange)
            print("asdf")
            distance = rs.getGPSm(gps[0], gps[1], location.gpsLat, location.gpsLong)
            if (distance < bestLocationDistance) and (distance < location.gpsRange):
                bestLocation = location

        profile = checkForProfile(email, bestLocation.profileName)
        if profile:
            return profile
        else:
            return False
    else:
        return False
    return False