from zope.schema import ValidationError

from collective.akismet import _


class AkismetReject(ValidationError):
    __doc__ = _("""Akismet thinks your comment is spam. If you are not a spam
                   bot, please contact Akismet (http://akismet.com/contact).""")