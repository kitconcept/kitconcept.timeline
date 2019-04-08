# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from collective.timeline.testing import COLLECTIVETIMELINE_CORE_INTEGRATION_TESTING  # noqa
from plone import api

try:
    from Products.CMFPlone.utils import get_installer
except ImportError:  # Plone < 5.1
    HAS_INSTALLER = False
else:
    HAS_INSTALLER = True

import unittest


class TestSetup(unittest.TestCase):
    """Test that collective.timeline is properly installed."""

    layer = COLLECTIVETIMELINE_CORE_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal)
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if collective.timeline is installed."""
        if HAS_INSTALLER:
            self.assertTrue(
                self.installer.is_product_installed('collective.timeline')
            )
        else:
            self.assertTrue(
                self.installer.isProductInstalled(
                    'collective.timeline'
                )
            )

    def test_browserlayer(self):
        """Test that ICollectivetimelineCoreLayer is registered."""
        from collective.timeline.interfaces import (
            ICollectivetimelineCoreLayer)
        from plone.browserlayer import utils
        self.assertIn(ICollectivetimelineCoreLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = COLLECTIVETIMELINE_CORE_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        if HAS_INSTALLER:
            self.installer = get_installer(self.portal)
            self.installer.uninstall_product('collective.timeline')
        else:
            self.installer = api.portal.get_tool('portal_quickinstaller')
            self.installer.uninstallProducts(['collective.timeline'])

    def test_product_uninstalled(self):
        """Test if collective.timeline is cleanly uninstalled."""
        if HAS_INSTALLER:
            self.assertFalse(
                self.installer.is_product_installed('collective.timeline')
            )
        else:
            self.assertFalse(
                self.installer.isProductInstalled(
                    'collective.timeline'
                )
            )

    def test_browserlayer_removed(self):
        """Test that ICollectivetimelineCoreLayer is removed."""
        from collective.timeline.interfaces import ICollectivetimelineCoreLayer
        from plone.browserlayer import utils
        self.assertNotIn(ICollectivetimelineCoreLayer, utils.registered_layers())
