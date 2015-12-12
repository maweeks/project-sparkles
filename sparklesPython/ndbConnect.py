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

from google.appengine.ext import ndb

DEFAULT_ACCOUNT_NAME = "userAccount"

class Account(ndb.Model):
    """A main model for representing an individual Profile entry."""
    email = ndb.StringProperty(indexed=True)
    spotify = ndb.StringProperty(indexed=False)
    autoHide = ndb.BooleanProperty(indexed=False)

def createAccountData(email):
	account = Account()
	account.spotify = ""
	account.email = email
	account.autoHide = False
	account.put()

def checkForAccount(email):
	account_query = Account.query(Account.email == email)
	account = account_query.fetch(1)
	return account[0]

def updateAccountData(email, autoHide, spotify):
	account = checkForAccount(email)
	account.autoHide = autoHide
	account.spotify = spotify
	account.put()