# -*- coding: utf-8 -*-

from Acquisition import aq_inner

from z3c.form import validator

from z3c.form.interfaces import IValidator

from zope.component import getMultiAdapter, provideAdapter, queryUtility

from zope.schema import ValidationError

from zope.interface import implements, Interface
from zope.schema.interfaces import IField
from zope.component import adapts

from plone.registry.interfaces import IRegistry

from plone.app.discussion.interfaces import ICaptcha
from plone.app.discussion.interfaces import IComment
from plone.app.discussion.interfaces import IDiscussionSettings
from plone.app.discussion.interfaces import IDiscussionLayer
from plone.app.discussion.interfaces import MessageFactory as _

from collective.akismet.browser.validator import AkismetReject

from zope.interface import implements, Interface
from zope.schema.interfaces import IField
from zope.component import adapts

from zope.schema import ValidationError

from collective.akismet import _


class AkismetReject(ValidationError):
    __doc__ = _("""Akismet thinks your comment is spam. If you are not a spam
                   bot, please contact Akismet (http://akismet.com/contact).""")
    

class AkismetValidator(validator.SimpleFieldValidator):
    implements(IValidator)
    adapts(Interface, IDiscussionLayer, Interface, IField, Interface)
    #       Object, Request, Form, Field, Widget,
    # We adapt the AkismetValidator class to all form fields (IField)

    def validate(self, value):
        super(AkismetValidator, self).validate(value)
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IDiscussionSettings)
        if settings.captcha == 'akismet':
            captcha = getMultiAdapter((aq_inner(self.context), self.request), 
                                      name=settings.captcha)
            if not captcha.verify(input=value):
                raise AkismetReject
            else:
                return True


validator.WidgetValidatorDiscriminators(AkismetValidator, 
                                        field=IComment['text'])
                