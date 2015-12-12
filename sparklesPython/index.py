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

import pageSetup as p

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	mainContents = """<div class='text-center'>
    					<h2 >Project Sparkles</h2>
    					<em><b>Automate your device, and carry on with your life!</b></em>
    					</div><br/>
    					<h5 class='text-primary'>What is Project Sparkles?</h5>
    					<b>Project Sparkles is a simple application that allows you to automate actions to speed up the setting up your device.</b><br/><br/>
    					<h5 class='text-primary'>What actions are available?</h5>
    					<b><ul>
    					<li>Open websites.</li>
    					<li>Play music through spotify (coming soon).</li>
    					</ul></b><br/>
    					<h5 class='text-primary'>How do you use it?</h5>
    					<b><ol>
    					<li>Sign into your Google account.</li>
    					<li>Connect any external accounts that you want to connect to.</li>
    					<li>Create profiles full of the actions that you want to occur.</li>
    					<li>Set the actions that you want to trigger each of the profiles.</li>
    					</ol></b><br/>
    					<h5 class='text-primary'>Got some feedback?</h5>
    					<b>If you have any feedback or suggestions for the project, please send an email to <a href='mailto:projectsparkles1@gmail.com'>projectsparkles1@gmail.com</a></b>"""

        pageContents = p.getRow(mainContents)

        self.response.write(p.getHeader("About", "/"))
        self.response.write(p.getContents(pageContents))
        self.response.write(p.getFooter())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/index\..*', MainHandler)
], debug=True)
