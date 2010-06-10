Introduction
============

`Akismet`_ is a web service for recognising spam comments. collective.akismet 
provides a Plone integration of the `Akismet`_ web service and is based 
on the `Akismet Python interface`_ package.

.._Akismet: http://akismet.com/

.._`Akismet Python interface`: http://pypi.python.org/pypi/akismet/

collective.akismet was developed as Spam protection plugin for 
`plone.app.discussion`_, but it can be used independently

.. _plone.app.discussion: http://pypi.python.org/pypi/plone.app.discussion

collective.akismet provides a form validator that connects to the Akismet web 
service and raises a validation error if Akismet detects spam. The form 
validator expects three form fields/values in the request: 
'form.widgets.author_name', 'form.widgets.author_email', and 'form.widgets.text'.


Buildout Installation
---------------------

Add the following code to your buildout.cfg to install collective.captcha::

    [buildout]
    ...
    eggs =
        ...
        collective.akismet
        ...

    ...
    [instance]
    ...
    zcml =
        ...
        collective.akismet
    ...
