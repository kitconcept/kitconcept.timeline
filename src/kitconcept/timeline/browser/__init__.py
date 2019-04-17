# -*- coding: utf-8 -*-
from plone import api
from plone.app.layout.viewlets import ViewletBase
from plone.dexterity.browser.view import DefaultView


class TimelineView(DefaultView):
    """Defaul view for Timeline content type."""

    def results(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type="Timeline Entry",
            sort_on="date",
            sort_order="reverse",
        )


class ResourcesViewlet(ViewletBase):
    """This viewlet inserts static resources on page header."""
