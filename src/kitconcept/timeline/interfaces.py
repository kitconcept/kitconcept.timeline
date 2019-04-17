# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""
from kitconcept.timeline import _
from plone.namedfile import field
from plone.supermodel import model
from zope import schema
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IKitconcepttimelineCoreLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class ITimeline(model.Schema):
    """Timeline content type interface."""


class ITimelineEntry(model.Schema):
    """Timeline Item content type interface."""

    image = field.NamedBlobImage(title=_(u"Image"), required=False)

    copyright = schema.TextLine(title=_(u"Copyright"), required=False)

    date = schema.Choice(
        title=_(u"Date"), vocabulary="kitconcept.timeline.Year", required=False
    )
