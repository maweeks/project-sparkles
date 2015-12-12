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

from google.appengine.api import users

def getUser():
    return users.get_current_user()

def getHeader(page):
    aboutClass = ""
    runClass = ""
    settingsClass = ""
    accountInfo = ""
    user = getUser()

    if page is "About":
        aboutClass = " class='active'"
    elif page is "Run":
        runClass = " class='active'"
    elif page is "Settings":
        settingsClass = " class='active'"

    # check user details
    if user:
        accountInfo = "<li class='thinRightPadding'><a class='whiteLink'>" + user.nickname() + """</a></li>
        <li class='signout thinLeftPadding'><a href="%s">sign out</a></li>""" % (users.create_logout_url(''))
    else:
        accountInfo = '<li class="signin"><a class="whiteLink" href="%s">Sign in or register</a></li>' % users.create_login_url('')

    headerContents = """<title>Sparkles - """ + page + """</title>
                    <link rel='stylesheet' type='text/css' href='/css/bootstrap.min.css'>
                    <link rel='stylesheet' type='text/css' href='/css/flat-ui-pro.min.css'>
                    <link rel='stylesheet' type='text/css' href='/css/style.css'>
                    <script src='/js/jQuery.js'></script>
                    <script src='/js/flat-ui.min.js'></script>
                    <header class='container'>
                    <div class='row'>
                    <nav class="navbar navbar-inverse" role="navigation">
                    <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-5">
                    <span class="sr-only">Toggle navigation</span>
                    </button>
                    <a class="navbar-brand whiteLink" href='/'>PROJECT SPARKLES</a>
                    </div>
                    <div class="collapse navbar-collapse" id="navbar-collapse-5">
                    <ul class="nav navbar-nav navbar-right">
                    <li""" + aboutClass + """><a href='/'>About</a></li>
                    <li""" + runClass + """><a href='/run/manual.html'>Run</a></li>
                    <li""" + settingsClass + """><a href='/settings/general.html'>Settings</a></li>
                    """ + accountInfo + """
                    </ul></div></nav>
                    </div>
                    </header>"""

    return headerContents

def getRunHeadings(active):
    return getSubheadings("Run", ["Manual", "Auto"], active)

def getSettingHeadings(active):
    return getSubheadings("Settings", ["General", "Profiles", "Locations"], active)

def getSubheadings(title, pages, active):
    pageList = ""

    for i in range(0, len(pages)):
        classList = ""
        if active == i:
            classList = " class='active'"
        pageList += "<li" + classList + " ><a href='/" + (title + "/" + pages[i] + ".html").lower() + "'>" + pages[i] + "</a></li>"

    contents = """<nav class="navbar navbar-default" role="navigation">
                    <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">
                    <span class="sr-only">Toggle navigation</span></button>
                    <a class="navbar-brand blueLink">""" + title + """</a>
                    </div><div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
                    <ul class="nav navbar-nav">""" + pageList + """</ul>
                    <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown"></ul>
                    </div>
                    </nav>"""

    return getRow(contents)

def getContents(contents):
    return "<div class='container'>" + contents + "</div>"

def getRow(contents):
    return "<div class='row'>" + contents + "</div>"

def getFooter():
    return """<footer class="container">
            <div class="row">
            <hr/><p class="bigMargin softenText text-center"> &copy; 2015. Matt Weeks, Leon Su &amp; Zak Walker</p>
            </div>
            </footer>"""
