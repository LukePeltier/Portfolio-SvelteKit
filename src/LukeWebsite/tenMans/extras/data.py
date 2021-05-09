import time
from django_cassiopeia import cassiopeia as cass


class GlobalVars():
    ver = None

    def getLoLVersion():
        try:
            GlobalVars.ver = cass.get_version()
        except ValueError:
            time.sleep(1)
        return GlobalVars.ver
