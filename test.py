from datasaver.service import DataSaverService
from datasaver.modal import Books

ds = DataSaverService(None)

b = Books("rukmani")
ds.insertEvent(b)
