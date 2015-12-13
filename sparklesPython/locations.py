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



def generateGetPage(account):
    pageContents = p.getRow(rs.getGPSJavascript(url))
    return pageContents

def generatePage(account, gps):
    pageContents = p.getRow("""POST""")
    pageContents = p.getRow(p.getGPSBox(gps))

    return pageContents






app = webapp2.WSGIApplication([
    ('/settings/locations\..*', MainHandler)
], debug=True)
