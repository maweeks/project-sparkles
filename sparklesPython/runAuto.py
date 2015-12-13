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
        email = user.email()
        pageContents = ""

        if not user:
            pageContents = p.getLoginPage(url)
        else:
            pageContents = generatePage(ndb.forceAccount(email))

        self.response.write(p.getHeader(page, url))

        if itemNo != -1:
            self.response.write(p.getRunHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())

def generatePage(account):
    content = ""
    profile = ndb.getDefaultProfile(account.email)
    content += "<script>" + rs.generateProfileScript(profile) + "</script>"
    content += "<div class='text-center'><h4>Profile <em>" + profile.name + "</em> has been executed!</h4></div>"
    content += ndb.printProfileList(profile, True)

    return p.getRow(content);

app = webapp2.WSGIApplication([
    ('/run/auto\..*', MainHandler)
], debug=True)
