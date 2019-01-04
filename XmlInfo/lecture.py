class Lecture(object):
    _month = ''
    _day = 0
    _title = ''
    _speaker = ''

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, month):
        self._month = month

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, day):
        self._day = day

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def speaker(self):
        return self._speaker

    @speaker.setter
    def speaker(self, speaker):
        self._speaker = speaker