from datasaver.parser import ExcelParser
from datasaver.extractor import ExtractorFactory
from datasaver.service import DataSaverService, DataArchiver

# Factory Pattern


def save(path):
    excelParser = ExcelParser()
    extractorFactory = ExtractorFactory()
    dataArchiver = DataArchiver()
    dataService = DataSaverService(dataArchiver)
    ds = DataSaver(excelParser, extractorFactory, dataService)
    ds.save(path)


class DataSaver(object):

    def __init__(self, parser, extractorFactory, service):
        self.parser = parser
        self.extractorFactory = extractorFactory
        self.service = service

    def save(self, path):
        df = self.parser.parse(path)
        for row in len(df):
            df_row = df[row]
            url = df_row["url"]
            extractor = self.extractorFactory.getExtractor(url)
            text = extractor.extract(url)
            df_row["text"] = text
            row = self.service.getEvent(df_row["id"])

            if row:
                self.service.updateEvent(df_row)
                return

            self.service.insertEvent(df_row)
