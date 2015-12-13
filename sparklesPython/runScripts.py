import ndbConnect as ndb

def hasAutohide(account):
    return account.autoHide

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