import unittest

from zope.component import getMultiAdapter

from plone.registry import Registry

from Products.CMFCore.utils import getToolByName
from Products.PloneTestCase.ptc import PloneTestCase

from collective.akismet.interfaces import IAkismetSettings
from collective.akismet.tests.layer import AkismetLayer


class RegistryTest(PloneTestCase):

    layer = AkismetLayer

    def afterSetUp(self):
        # Set up the akismet settings registry
        self.loginAsPortalOwner()
        self.registry = Registry()
        self.registry.registerInterface(IAkismetSettings)

    def test_akismet_controlpanel_view(self):
        # Test the akismet setting control panel view
        view = getMultiAdapter((self.portal, self.portal.REQUEST), 
                               name="akismet-settings")
        view = view.__of__(self.portal)
        self.failUnless(view())

    def test_akismet_controlpanel_view_protected(self):
        # Test that the akismet setting control panel view can not be accessed
        # by anonymous users
        from AccessControl import Unauthorized
        self.logout()
        self.assertRaises(Unauthorized,
                          self.portal.restrictedTraverse,
                         '@@akismet-settings')           
        
    def test_akismet_in_controlpanel(self):
        # Check that there is an akismet entry in the control panel
        self.controlpanel = getToolByName(self.portal, "portal_controlpanel")
        self.failUnless('akismet' in [a.getAction(self)['id']
                            for a in self.controlpanel.listActions()])

    def test_record_akismet_key(self):
        # Test that the akismet_key record is in the control panel
        record_akismet_key = self.registry.records[
            'collective.akismet.interfaces.IAkismetSettings.akismet_key']
        self.failUnless('akismet_key' in IAkismetSettings)
        self.assertEquals(record_akismet_key.value, u"")

    def test_record_akismet_key_site(self):
        # Test that the akismet_key_site record is in the control panel
        record_akismet_key_site = self.registry.records[
            'collective.akismet.interfaces.IAkismetSettings.akismet_key_site']        
        self.failUnless('akismet_key_site' in IAkismetSettings)
        self.assertEquals(record_akismet_key_site.value, u"")

def test_suite():
    return unittest.defaultTestLoader.loadTestsFromName(__name__)