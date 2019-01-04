import os
import xml.etree.ElementTree as ElementTree
from pathlib import Path
from string import capwords
from typing import List
from xml.etree.ElementTree import Element
from xml.etree.ElementTree import SubElement

from lecture import Lecture


class Converter(object):
    _xml_filename = 'lectures.xml'
    _data_file_name = 'data.txt'

    def convert(self):
        if Path(self._data_file_name).is_file():
            self.process_file(self._data_file_name)

    def process_file(self, filename):

        lectures = []
        with open(filename, 'r') as file:
            for line in file:
                lecture = self.process_line(line=line)
                lectures.append(lecture)

        self.write_as_xml(lectures=lectures)

    def remove_xml(self):
        try:
            file = Path(self._xml_filename)
            if file.is_file():
                os.remove(self._xml_filename)
        except OSError as e:
            print(e.errno)

    def process_line(self, line):

        processed_items = []
        items = line.split(' ')
        index_of_bro = 0
        index = 0

        for item in items:
            if len(item) == 0:
                continue
            if item == 'Bro.':
                index_of_bro = index
            processed_items.append(item)
            index += 1

        lecture = self.process_item(processed_items=processed_items, index=index_of_bro)
        return lecture

    @staticmethod
    def process_item(processed_items, index):

        lecture = Lecture()
        lecture.month = processed_items[0]
        lecture.day = processed_items[1]

        title = ''
        for position in range(2, index):
            title += "{} ".format(str(processed_items[position]).lower())
        lecture.title = capwords(title.strip())

        speaker = ''
        for position in range(index + 1, len(processed_items)):
            speaker += "{} ".format(str(processed_items[position]).strip('.').lower().title())
        lecture.speaker = speaker.strip()
        return lecture

    @staticmethod
    def write_as_xml(lectures=List[Lecture]):

        root = Element('lectures')
        for lecture in lectures:
            print("{} {} {} {}".format(lecture.title, lecture.month, lecture.day, lecture.speaker))
            lecture_element = SubElement(root, 'lecture')

            date_element = SubElement(lecture_element, 'date')
            date_element.text = "{}-{}".format(lecture.day, lecture.month)

            title_element = SubElement(lecture_element, 'title')
            title_element.text = lecture.title

            speaker_element = SubElement(lecture_element, 'speaker')
            speaker_element.text = lecture.speaker

            presider_element = SubElement(lecture_element, 'preside')
            presider_element.text = 'TBA'

        tree = ElementTree.ElementTree(root)
        tree.write('lectures.xml')


c = Converter()
c.convert()
