# -*- coding: utf-8 -*-
from kitconcept.timeline.interfaces import ITimelineEntry
from plone.indexer import indexer


@indexer(ITimelineEntry)
def dateIndexer(context):
    return context.date
