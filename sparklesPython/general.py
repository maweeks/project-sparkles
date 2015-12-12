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
import time

itemNo = 0
page = "Settings"
url = "settings/general.html"

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
            self.response.write(p.getSettingHeadings(itemNo))

        self.response.write(p.getContents(pageContents))
        self.response.write(p.getFooter())

class StoreHandler(webapp2.RequestHandler):
    def post(self):
        email = p.getUser().email()
        autohide = False

        print(self.request)

        if (self.request.get('autohide') == "True"):
            autohide = True
        ndb.updateAccountHide(email, autohide)
        time.sleep(0.1)
        self.redirect('/settings/general.html')

def generatePage(account):
    return p.getRow(ndb.printAccountForm(account))

app = webapp2.WSGIApplication([
    ('/settings/general\..*', MainHandler),
    ('/settings/generalSend', StoreHandler),
    ('/settings/.*', MainHandler)
], debug=True)

# ndb.updateAccountData(email(), True, "NA")