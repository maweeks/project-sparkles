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

itemNo = 0
page = "Run"
url = "/run/manual.html"

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
            self.response.write(p.getRunHeadings(itemNo))

        self.response.write(p.getContents(pageContents))

        self.response.write(p.getFooter())


def generatePage(account):
    content = ""
    profiles = ndb.getAllProfiles(account.email)
    for profile in profiles:
        content += ndb.printProfileList(profile, False)
    if content == "":
        content += ndb.noProfiles(0)

    return p.getRow(content);

app = webapp2.WSGIApplication([
    ('/run/manual\.html', MainHandler),
    ('/run/.*', MainHandler)
], debug=True)
