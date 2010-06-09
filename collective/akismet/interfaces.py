from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('collective.akismet')


class IAkismetSettings(Interface):
    """Global discussion settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    akismet_key = schema.TextLine(title=_(u"Akismet (Wordpress) Key"),
                                  description=_(u"help_akismet_key",
                                                default=u"Enter in your Wordpress key here to "
                                                         "use Akismet to check for spam in comments."),
                                  required=False,
                                  default=u'',)

    akismet_key_site = schema.TextLine(title=_(u"Site URL"),
                                  description=_(u"help_akismet_key_site",
                                                default=u"Enter the URL to this site as per your "
                                                         "Akismet settings."),
                                  required=False,
                                  default=u'',)
