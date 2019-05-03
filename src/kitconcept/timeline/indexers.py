# -*- coding: utf-8 -*-
from kitconcept.timeline.interfaces import ITimelineEntry
from plone.indexer import indexer


@indexer(ITimelineEntry)
def dateIndexer(context):
    items = [context.year, context.month, context.day]
    unique = set(items)

    # just year set
    if len(unique) == 2 and context.year is not None:
        return (context.year, 0, 0,)

    return (context.year, context.month, context.day,)
