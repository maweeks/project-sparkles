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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        pageContents = p.getRunHeadings(1)
        url = "run/auto.html"

        if not p.getUser():
        	pageContents += p.getLoginPage(url)
        else:
        	pageContents += p.getRow('Run auto script!')

        self.response.write(p.getHeader("Run", url))
        self.response.write(p.getContents(pageContents))
        self.response.write(p.getFooter())

app = webapp2.WSGIApplication([
    ('/run/auto\..*', MainHandler)
], debug=True)
