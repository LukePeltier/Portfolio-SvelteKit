import time
from django_cassiopeia import cassiopeia as cass


class GlobalVars():
    ver = None

    def getLoLVersion():
        while GlobalVars.ver is None:
            try:
                GlobalVars.ver = cass.get_version(region="NA")
            except ValueError:
                time.sleep(1)
        return GlobalVars.ver
