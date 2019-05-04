# -*- coding: utf-8 -*-
from kitconcept.timeline.interfaces import ITimeline
from kitconcept.timeline.interfaces import ITimelineEntry
from plone.dexterity.content import Container
from Products.CMFCore.utils import getToolByName
from zope.i18n import translate
from zope.i18nmessageid import MessageFactory
from zope.interface import implementer


PLMF = MessageFactory('plonelocales')


@implementer(ITimeline)
class Timeline(Container):
    """The Timeline object"""


@implementer(ITimelineEntry)
class TimelineEntry(Container):
    """The Timeline Entry object."""

    def get_date(self):
        items = [self.year, self.month, self.day]
        unique = set(items)

        # just year set
        if len(unique) == 2 and self.year is not None:
            return self.year

        ts = getToolByName(self, 'translation_service')
        month_name = PLMF(ts.month_msgid(self.month),
                          default=ts.month_english(self.month))

        return '{}. {} {}'.format(self.day, translate(month_name), self.year)
