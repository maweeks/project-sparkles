import ndbConnect as ndb

def generateProfileScript(profile):
    script = ""
    hidden = True
    if hasAutohide(ndb.checkForAccount(profile.email)):
        hidden = False
    for site in profile.sites:
        if not hidden:
            script += "window.open(' " + site.site.rstrip() + "','_self');"
            hidden = True
        else:
            script += "window.open(' " + site.site.rstrip() + "');"
    return script

def getGPSJavascript(url):
    script = """<script>
                function getLocation() {
                    var location = "";
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(showPosition);
                    }
                }

                function showPosition(position) {
                    document.getElementById('location').value = (position.coords.latitude +
                    " " + position.coords.longitude);
                    geoPost();
                }

                function geoPost() {
                    document.getElementById('geoForm').submit();
                }
                getLocation();
                setTimeout(geoPost, 10000);
                </script>
                <div class="col-lg-12">
                <form id='geoForm' class='form form-horizontal' action='""" + url + """' method="post">
                <div class="form-group">
                <label for="location" class="col-lg-2 control-label"><em><b>Location</b></em></label>
                <div class="col-lg-10">
                <input class="form-control" id="location" name="location" placeholder="Location" value=''><br/>
                <input class='btn btn-primary' type="submit" value="Submit GPS">
                <button type="button" class="btn btn-default" onclick="
                document.getElementById('location').value=''; geoPost();">Don't Submit GPS</button>
                </div>
                </div>
                </form>
                </div>"""
    return script

def hasAutohide(account):
    return account.autoHide



# setTimeout(geoPost, 5000);