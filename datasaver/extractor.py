class ExtractorFactory(object):
    def getExtractor(self, url):
        return HTMLExtractor()


class Extractor(object):
    def extract(self, url):
        raise NotImplementedError("This should be implemented")


class TextExtractor(Extractor):
    def extract(self, url):
        pass


class HTMLExtractor(Extractor):
    def extract(self, url):
        pass


class RSSExtractor(Extractor):
    def extract(self, url):
        pass
