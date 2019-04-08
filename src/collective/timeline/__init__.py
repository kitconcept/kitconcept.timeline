# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PROJECTNAME = 'collective.timeline'
_ = MessageFactory(PROJECTNAME)
logger = logging.getLogger(PROJECTNAME)
config = {}
