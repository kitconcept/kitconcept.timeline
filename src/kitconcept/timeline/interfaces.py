# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from datetime import datetime
from kitconcept.timeline import _
from plone.namedfile import field
from plone.supermodel import model
from zope import schema
from zope.interface import Invalid
from zope.interface import invariant
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IKitconcepttimelineCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITimeline(model.Schema):
    """Timeline content type interface."""


class ITimelineEntry(model.Schema):
    """Timeline Item content type interface."""

    image = field.NamedBlobImage(title=_(u"Image"), required=True)

    copyright = schema.TextLine(title=_(u"Copyright"), required=False)

    year = schema.Int(title=_(u"Year"), required=True)

    month = schema.Int(title=_(u"Month"), min=1, max=12, required=False)

    day = schema.Int(title=_(u"Day"), min=1, max=31, required=False)

    @invariant
    def date_invariant(data):
        items = [data.year, data.month, data.day]

        # just year set
        if len(set(items)) == 2 and data.year is not None:
            return

        # year, month, day set
        try:
            datetime(data.year, data.month, data.day)
        except ValueError:
            raise Invalid(_(u'Invalid date'))
