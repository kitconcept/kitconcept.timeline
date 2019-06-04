# -*- coding: utf-8 -*-
from kitconcept.timeline.interfaces import ITimeline
from kitconcept.timeline.interfaces import ITimelineEntry
from plone import api
from plone.dexterity.content import Container
from zope.interface import implementer


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

        util = api.portal.get_tool('translation_service')
        month = util.translate(
            util.month_msgid(self.month),
            domain='plonelocales',
            context=self
        )

        return '{}. {} {}'.format(self.day, month, self.year)
