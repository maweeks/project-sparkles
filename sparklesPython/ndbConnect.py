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
	return account

#     greetings_query = Greeting.query(
#     ancestor=guestbook_key(guestbook_name)).order(-Greeting.date)
# greetings = greetings_query.fetch(10)

# user = users.get_current_user()
# for greeting in greetings:
#     if greeting.author:
#         author = greeting.author.email
#         if user and user.user_id() == greeting.author.identity:
#             author += ' (You)'
#         self.response.write('<b>%s</b> wrote:' % author)
#     else:
#         self.response.write('An anonymous person wrote:')
#     self.response.write('<blockquote>%s</blockquote>' %
#                         cgi.escape(greeting.content))