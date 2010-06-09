from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import ptc
from Products.PloneTestCase import layer
from Products.Five import zcml
from Products.Five import fiveconfigure

ptc.setupPloneSite(
    extension_profiles=('collective.akismet:default', )
)

class AkismetLayer(layer.PloneSite):
    """Configure collective.akismet"""

    @classmethod
    def setUp(cls):
        fiveconfigure.debug_mode = True
        import collective.akismet
        zcml.load_config("configure.zcml", collective.akismet)
        fiveconfigure.debug_mode = False
        ztc.installPackage("collective.akismet", quiet=1)

    @classmethod
    def tearDown(cls):
        pass
