# -*- coding: utf-8 -*-
from plone import api
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

import json
import os


class TimelineView(BrowserView):
    """Defaul view for Timeline content type."""

    template = ViewPageTemplateFile('timeline.pt')

    def __call__(self):
        self.manifest = self.read_manifest_json()
        return self.template()

    def results(self):
        return api.content.find(
            context=self.context,
            depth=1,
            portal_type="Timeline Entry",
            sort_on="date",
            sort_order="reverse",
        )

    def read_manifest_json(self):
        return json.loads(
            open(os.path.join(
                os.path.dirname(__file__),
                'static', 'webpack-assets.json'), 'r').read())
