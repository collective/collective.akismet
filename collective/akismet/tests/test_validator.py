import unittest

from zope.component import getMultiAdapter

from plone.registry import Registry

from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase

from collective.akismet.interfaces import IAkismetSettings
from collective.akismet.tests.layer import AkismetLayer


class AkismetValidatorViewTest(PloneTestCase):

    layer = AkismetLayer

    def afterSetUp(self):
        # Set up the akismet settings registry
        self.registry = Registry()
        self.registry.registerInterface(IAkismetSettings)

    def test_akismet_validator_view(self):
        # Test the akismet setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST), 
                               name="akismet")
        view = view.__of__(self.portal)
        self.failUnless(view())

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)