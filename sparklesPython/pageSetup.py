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

def getHeader(page):
    headerContents = "<header>"
    headerContents += "<h1>PROJECT SPARKLES</h1>"
    headerContents += "<em>Links:</em>"
    headerContents += "<a href='index.html'>About</a>"
    headerContents += "<a href='/run/manual.html'>Run</a>"
    headerContents += "<a href='/settings/general.html'>Settings</a>"
    headerContents += "<em>[User]</em>"
    headerContents += "</header><br/>"
    return headerContents

def getContents(contents):
    return "" + contents + ""

def getFooter():
    return """<footer class="container">
                <div class="row">
                <hr/><p class="bigMargin softenText text-center"> &copy; 2015. Matt Weeks, Leon Su, Zak Walker</p>
                </div>
                </footer>"""