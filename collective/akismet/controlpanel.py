from Products.Five.browser import BrowserView

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry

from plone.app.registry.browser import controlpanel

from collective.akismet.interfaces import IAkismetSettings, _


class AkismetSettingsEditForm(controlpanel.RegistryEditForm):

    schema = IAkismetSettings
    label = _(u"Akismet settings")
    description = _(u"""""")

    def updateFields(self):
        super(AkismetSettingsEditForm, self).updateFields()
        

    def updateWidgets(self):
        super(AkismetSettingsEditForm, self).updateWidgets()

class AkismetSettingsControlPanel(controlpanel.ControlPanelFormWrapper):
    form = AkismetSettingsEditForm
