# -*- coding: utf-8 -*-
from plone.app.testing import TEST_USER_ID
from zope.component import queryUtility
from zope.component import createObject
from plone.app.testing import setRoles
from plone.dexterity.interfaces import IDexterityFTI
from plone import api

from kitconcept.timeline.testing import KITCONCEPTTIMELINE_CORE_INTEGRATION_TESTING  # noqa
from kitconcept.timeline.interfaces import ITimeline

import unittest


class TimelineIntegrationTest(unittest.TestCase):

    layer = KITCONCEPTTIMELINE_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])
        self.installer = api.portal.get_tool('portal_quickinstaller')
        fti = queryUtility(IDexterityFTI, name='Timeline')
        fti.global_allow = True

    def test_schema(self):
        fti = queryUtility(IDexterityFTI, name='Timeline')
        schema = fti.lookupSchema()
        self.assertEqual(ITimeline, schema)

    def test_fti(self):
        fti = queryUtility(IDexterityFTI, name='Timeline')
        self.assertTrue(fti)

    def test_factory(self):
        fti = queryUtility(IDexterityFTI, name='Timeline')
        factory = fti.factory
        obj = createObject(factory)
        self.assertTrue(ITimeline.providedBy(obj))

    def test_adding(self):
        self.portal.invokeFactory('Timeline', 'timeline')
        self.assertTrue(
            ITimeline.providedBy(self.portal['timeline'])
        )
