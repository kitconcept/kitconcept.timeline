# -*- coding: utf-8 -*-
from kitconcept.timeline.interfaces import ITimeline
from kitconcept.timeline.interfaces import ITimelineEntry
from plone.dexterity.content import Container
from zope.interface import implementer


@implementer(ITimeline)
class Timeline(Container):
    """The Timeline object"""


@implementer(ITimelineEntry)
class TimelineEntry(Container):
    """The Timeline Entry object."""
