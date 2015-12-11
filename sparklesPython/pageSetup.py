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
    headerContents = """<link rel='stylesheet' type='text/css' href='css/bootstrap.min.css'>
                    <link rel='stylesheet' type='text/css' href='css/flat-ui-pro.min.css'>
                    <link rel='stylesheet' type='text/css' href='css/style.css'>"""
    headerContents += "<header>"
    headerContents += "<div class='container'>"
    headerContents += "<div class='row'>"
    headerContents += "<div class='col-xs-6 col-sm-6 col-md-6'>"
    headerContents += "<a href='index.html'> <h4>PROJECT SPARKLES</h4></a>"
    headerContents += "</div>"
    headerContents += "<div class='col-xs-6 col-sm-6 col-md-6'>"
    headerContents += "<a href='index.html'>About</a><br>"
    headerContents += "<a href='/run/manual.html'>Run</a><br>"
    headerContents += "<a href='/settings/general.html'>Settings</a><br>"
    headerContents += "<em>[User]</em>"
    headerContents += "</div>"
    headerContents += "</div>"
    headerContents += "</div>"
    headerContents += "</header><br/>"


    headerContents = """<link rel='stylesheet' type='text/css' href='css/bootstrap.min.css'>
                    <link rel='stylesheet' type='text/css' href='css/flat-ui-pro.min.css'>
                    <link rel='stylesheet' type='text/css' href='css/style.css'>
                    <script src='js/jQuery.js'></script>
                    <script src='js/flat-ui.min.js'></script>"""
    headerContents += "<header>"
    headerContents += "<div class='container'>"
    headerContents += "<div class='row'>"
    headerContents += """<nav class="navbar navbar-inverse" role="navigation">
                    <div class="navbar-header">
                    <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#navbar-collapse-5">
                    <span class="sr-only">Toggle navigation</span>
                    </button>
                    <a class="navbar-brand" href="/">PROJECT SPARKLES</a>
                    </div>
                    <div class="collapse navbar-collapse" id="navbar-collapse-5">
                    <ul class="nav navbar-nav navbar-right">
                    <li class="active"><a href="/">About</a></li>
                    <li><a href="/run/manual.html">Run</a></li>
                    <li><a href="/settings/general.html">Settings</a></li>
                    <li><a>Account</a></li>
                    </ul></div></nav>"""
    headerContents += "</div>"
    headerContents += "</div>"
    headerContents += "</header>"




    return headerContents

def getContents(contents):
    return "<div class='container'><div class='row'>" + contents + "</div></div>"

def getFooter():
    return """<footer class="container">
            <div class="row">
            <hr/><p class="bigMargin softenText text-center"> &copy; 2015. Matt Weeks, Leon Su, Zak Walker</p>
            </div>
            </footer>"""