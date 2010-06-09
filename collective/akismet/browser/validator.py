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
                if api.comment_check(comment, d):
                    raise ValidationError
            except AkismetError:
                # Akismet temporarily down, so let comment through
                # XXX: write to log
                pass
