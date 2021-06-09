from datetime import datetime

class WorkLogs(object):
    def __init__(self, date: str, event: str, gate: str):
        self._date = date
        self._event = event
        self._gate = gate

    @property
    def date(self):
        return self._date

    @property
    def event(self):
        return self._event

    @property
    def gate(self):
        return self._gate      

    def weekNumber(self):
        return self._date.date().isocalendar()[1]


      