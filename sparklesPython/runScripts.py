from decimal import Decimal
import math
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

def getGPSm(lat1, long1, lat2, long2):
    # Convert latitude and longitude to
    # spherical coordinates in radians.
    dToR = float(math.pi/180.0)

    # latitude in radians
    latX1 = (90.0 - float(lat1))*dToR
    latX2 = (90.0 - float(lat2))*dToR

    # longitude in radians
    longX1 = float(long1)*dToR
    longX2 = long2*dToR

    # Compute spherical distance from spherical coordinates.
    calc = (math.sin(latX1)*math.sin(latX2)*math.cos(longX1 - longX2) +
           math.cos(latX1)*math.cos(latX2))
    arc = math.acos( calc )

    # return distance between 2 points in meters.
    return int(arc * 6373000)

def getGPSJavascript(url):
    script = """<script>
                function getLocation() {
                    var location = "";
                    if (navigator.geolocation) {
                        navigator.geolocation.getCurrentPosition(showPosition);
                    }
                    else {
                        document.getElementById('gettingLocation').style.display = "none";
                    }
                }

                function showPosition(position) {
                    document.getElementById('location').value = (position.coords.latitude +
                    " " + position.coords.longitude);
                    document.getElementById('gettingLocation').style.display = "none";
                    geoPost();
                }

                function geoPost() {
                    document.getElementById('geoForm').submit();
                }
                getLocation();
                setTimeout(geoPost, 10000);
                </script>

                <div class="col-lg-12 gettingGPS" id="gettingLocation">
                <div class='thumbnail formThumbnail text-center' id="gettingLocationThumb">
                <b>Currently attempting to access your location.</b><br/>
                This could take up to 10 seconds and you have to allow us to use your location.
                </div></div><br/>


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