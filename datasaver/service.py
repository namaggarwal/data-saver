from datasaver.modal import Books


class Service(object):
    def getEvent(self, id):
        raise NotImplementedError("")

    def insertEvent(self, event):
        raise NotImplementedError("")

    def updateEvent(self, event):
        raise NotImplementedError("")


class Archival(object):
    def archive(self, content):
        raise NotImplementedError("")


class DataArchiver(Archival):
    def archive(self, content):
        pass


class DataSaverService(Service):
    def __init__(self, archiver, conn):
        self.archiver = archiver
        self.conn = conn

    def getEvent(self, id):
        return Books.getBook(id)

    def insertEvent(self, event):
        event.save(self.conn)

    def updateEvent(self):
        pass
