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
page = "Run"
url = "/run/auto.html"

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
            self.response.write(p.getRunHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())

    def post(self):
        user = p.getUser()
        pageContents = ""

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
            self.response.write(p.getRunHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())

def generateGetPage(account):
    pageContents = p.getRow(rs.getGPSJavascript(url))
    return pageContents

def generatePage(account, gps):
    pageContents = p.getRow(p.getGPSBox(gps))
    error = 0
    if gps != "Not available.":
        profile = ndb.getGPSProfile(account.email, gps)
        error = 2
    else:
        profile = ndb.getDefaultProfile(account.email)
        error = 1
    if profile:
        pageContents += "<script>" + rs.generateProfileScript(profile) + "</script>"
        pageContents += "<br/><div class='text-center'><h4>Profile <em>" + profile.name + "</em> has been executed!</h4></div>"
        pageContents += ndb.printProfileList(profile, True)
    else:
        pageContents += ndb.noProfiles(error)
    return p.getRow(pageContents);

app = webapp2.WSGIApplication([
    ('/run/auto\..*', MainHandler)
], debug=True)
