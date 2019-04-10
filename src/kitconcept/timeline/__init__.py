# -*- coding: utf-8 -*-
"""Init and utils."""
from zope.i18nmessageid import MessageFactory

import logging


PROJECTNAME = 'kitconcept.timeline'
_ = MessageFactory(PROJECTNAME)
logger = logging.getLogger(PROJECTNAME)
config = {}
