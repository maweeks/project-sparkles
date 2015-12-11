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
    aboutClass = ""
    runClass = ""
    settingsClass = ""
    accountInfo = ""

    if page is "About":
        aboutClass = " class='active'"
    elif page is "Run":
        runClass = " class='active'"
    elif page is "Settings":
        settingsClass = " class='active'"

    # check user details
    # if signed in
    # show username
    # else
    accountInfo = "<a href=''>Sign In</a>"

    headerContents = """<title>Sparkles - """ + page + """</title>
                    <link rel='stylesheet' type='text/css' href='/css/bootstrap.min.css'>
                    <link rel='stylesheet' type='text/css' href='/css/flat-ui-pro.min.css'>
                    <link rel='stylesheet' type='text/css' href='/css/style.css'>
                    <script src='/js/jQuery.js'></script>
                    <script src='/js/flat-ui.min.js'></script>
                    <header>
                    <div class='container'>
                    <div class='row'>
                    <nav class="navbar navbar-inverse" role="navigation">
                    <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-5">
                    <span class="sr-only">Toggle navigation</span>
                    </button>
                    <a class="navbar-brand" href="/">PROJECT SPARKLES</a>
                    </div>
                    <div class="collapse navbar-collapse" id="navbar-collapse-5">
                    <ul class="nav navbar-nav navbar-right">
                    <li""" + aboutClass + """><a href='/'>About</a></li>
                    <li""" + runClass + """><a href='/run/manual.html'>Run</a></li>
                    <li""" + settingsClass + """><a href='/settings/general.html'>Settings</a></li>
                    <li>""" + accountInfo + """</li>
                    </ul></div></nav>
                    </div>
                    </div>
                    </header>"""

    return headerContents

def getContents(contents):
    return "<div class='container'><div class='row'>" + contents + "</div></div>"

def getFooter():
    return """<footer class="container">
            <div class="row">
            <hr/><p class="bigMargin softenText text-center"> &copy; 2015. Matt Weeks, Leon Su, Zak Walker</p>
            </div>
            </footer>"""