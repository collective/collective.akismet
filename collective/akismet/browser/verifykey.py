# -*- coding: utf-8 -*-

import urllib
import urllib2

from akismet import Akismet, AkismetError

from Acquisition import aq_inner

from Products.Five import BrowserView

from zope import schema

from zope.annotation import factory
from zope.component import adapts, queryMultiAdapter, queryUtility
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IBrowserRequest

from recaptcha.client.captcha import displayhtml, submit

from plone.registry.interfaces import IRegistry

from collective.akismet.interfaces import IAkismetSettings


class VerifyKeyView(BrowserView):
    """Verify the Akismet key that has been entered into the control panel. 
    """

    def __call__(self):

        context = aq_inner(self.context)
        
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IAkismetSettings)

        url = 'http://rest.akismet.com/1.1/verify-key'
        values = {'key' : settings.akismet_key,
                  'blog' : settings.akismet_key_site}
        
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        the_page = response.read()
        return the_page
