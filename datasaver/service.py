class Service(object):
    def getEvent(self, id):
        raise NotImplementedError("")

    def insertEvent(self):
        raise NotImplementedError("")

    def updateEvent(self):
        raise NotImplementedError("")


class Archival(object):
    def archive(self, content):
        raise NotImplementedError("")


class DataArchiver(Archival):
    def archive(self, content):
        pass


class DataSaverService(Service):
    def __init__(self, archiver):
        self.archiver = archiver
        # create db connection here

    def getEvent(self, id):
        pass

    def insertEvent(self):
        pass

    def updateEvent(self):
        pass
