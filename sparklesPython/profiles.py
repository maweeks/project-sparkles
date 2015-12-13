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

itemNo = 1
page = "Settings"
url = "/settings/profiles.html"

class MainHandler(webapp2.RequestHandler):
    def get(self):
        user = p.getUser()
        pageContents = ""

        if not user:
            pageContents = p.getLoginPage(url)
        else:
            email = user.email()
            pageContents = generatePage(ndb.forceAccount(email))

        self.response.write(p.getHeader(page, url))

        if itemNo != -1:
            self.response.write(p.getSettingHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())


class StoreHandler(webapp2.RequestHandler):
    def post(self):
        email = p.getUser().email()
        # print (self.request)

        name = self.request.get('name')
        newName = name
        type = self.request.get('type')

        lines = self.request.get('sites')
        sites = [l for l in lines.split("\n") if l]

        playlist = self.request.get('playlist')
        default = False

        if (self.request.get('defaultProfile') == "True"):
            default = True

        profile = ndb.checkForProfile(email, name)

        # name=X&sites=Y&playlist=Z&defaultProfile=True

        profile = ndb.checkForProfile(email, name)
        if profile:
            ndb.updateProfile(email, name, newName, type, sites, playlist, default)
        else:
            ndb.createProfileData(email, name, type, sites, playlist, default)
        time.sleep(0.1)
        self.redirect(url)


class DeleteHandler(webapp2.RequestHandler):
    def post(self):
        name = self.request.get('name')
        email = p.getUser().email()
        ndb.deleteProfile(name, email)
        time.sleep(0.1)
        self.redirect(url)


def generatePage(account):
    content = ndb.printNewProfileForm(account.email)

    # print all current profiles
    profiles = ndb.getAllProfiles(account.email)
    print(profiles)
    for profile in profiles:
        print(profile.name)
        content += ndb.printCurrentProfileForm(profile)

    return p.getRow(content)

app = webapp2.WSGIApplication([
    ('/settings/profiles\..*', MainHandler),
    ('/settings/profileSend', StoreHandler),
    ('/settings/profileDelete', DeleteHandler)
], debug=True)
