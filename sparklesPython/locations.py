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
import webapp2

import ndbConnect as ndb
import pageSetup as p
import runScripts as rs
import time

itemNo = 2
page = "Settings"
url = "/settings/locations.html"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = p.getUser()
        pageContents = ""

        if not user:
            pageContents = p.getLoginPage(url)
        else:
            email = user.email()
            pageContents = generateGetPage(ndb.forceAccount(email))

        self.response.write(p.getHeader(page, url))

        if itemNo != -1:
            self.response.write(p.getSettingHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())

    def post(self):
        user = p.getUser()
        pageContents = ""

        print(self.request.get('location'))
        gps = "Not available."
        if self.request.get('location') != "":
            gps = self.request.get('location').split(" ")



        if not user:
            pageContents = p.getLoginPage(url)
        else:
            email = user.email()
            pageContents = generatePage(ndb.forceAccount(email), gps)

        self.response.write(p.getHeader(page, url))

        if itemNo != -1:
            self.response.write(p.getSettingHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())


class StoreHandler(webapp2.RequestHandler):
    def post(self):
        email = p.getUser().email()

        name = self.request.get('name')
        newName = name
        type = self.request.get('type')
        gpsLat = float(self.request.get('gpsLat'))
        gpsLong = float(self.request.get('gpsLong'))
        gpsRange = int(self.request.get('gpsRange'))
        profileName = self.request.get('profileNameX')

        profile = ndb.checkForLocation(email, name)
        if profile:
            ndb.updateLocation(email, name, newName, type, gpsLat, gpsLong, gpsRange, profileName)
        else:
            ndb.createLocationData(email, name, type, gpsLat, gpsLong, gpsRange, profileName)
        time.sleep(0.1)
        self.redirect(url)


class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        email = p.getUser().email()
        ndb.deleteLocation(name, email)
        time.sleep(0.1)
        self.redirect(url)

def generateGetPage(account):
    pageContents = p.getRow(rs.getGPSJavascript(url))
    return pageContents

def generatePage(account, gps):
    pageContents = p.getRow(p.getGPSBox(gps))

    pageContents += p.getRow(ndb.printNewLocationForm(account.email))

    # print all current locations
    locations = ndb.getAllLocations(account.email)
    for location in locations:
        pageContents += p.getRow(ndb.printCurrentLocationForm(location))

    return pageContents

app = webapp2.WSGIApplication([
    ('/settings/locations\..*', MainHandler),
    ('/settings/locationSend', StoreHandler),
    ('/settings/locationDelete', DeleteHandler)
], debug=True)
