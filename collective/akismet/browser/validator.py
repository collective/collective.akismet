# -*- coding: utf-8 -*-

from akismet import Akismet, AkismetError

from Products.Five import BrowserView

from zope import schema

from zope.annotation import factory
from zope.component import adapts, queryMultiAdapter, queryUtility
from zope.interface import Interface, implements
from zope.publisher.interfaces.browser import IBrowserRequest

from recaptcha.client.captcha import displayhtml, submit

from plone.registry.interfaces import IRegistry

from collective.akismet.interfaces import IAkismetSettings
from collective.akismet import _


class AkismetReject(schema.ValidationError):
    __doc__ = _("""Akismet thinks your comment is spam. If you are not a spam 
                   bot, please contact Akismet (http://akismet.com/contact).""")


class AkismetValidatorView(BrowserView):
    """Akismet validator view 
    """
    def __init__(self, context, request):
        self.context = context
        self.request = request
        registry = queryUtility(IRegistry)
        self.settings = registry.forInterface(IAkismetSettings)

    def verify(self, input=None):
        if self.settings.akismet_key and self.settings.akismet_key_site:
            request = self.request
            data = request.form
            
            api = Akismet(self.settings.akismet_key, self.settings.akismet_key_site)
            
            d = {}
            d['user_ip'] = request.get('REMOTE_ADDR', '')
            d['user_agent'] = request.get('HTTP_USER_AGENT', '')
            d['referrer'] = request.get('HTTP_REFERER', '')
            d['comment_author'] = data['form.widgets.author_name']
            d['comment_author_email'] = data['form.widgets.author_email']

            comment = data['form.widgets.text']
            
            try:
                # Returns True for spam and False for ham.
                if api.comment_check(comment, d):
                    # Spam => not valid
                    return False
                else:
                    # No spam => valid
                    return True
            except AkismetError:
                # Akismet temporarily down, so let comment through
                # XXX: write to log
                return True
