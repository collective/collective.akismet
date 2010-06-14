from setuptools import setup, find_packages
import os

version = '1.0a1'

setup(name='collective.akismet',
      version=version,
      description="Akismet plugin for plone.app.discussion",
      long_description=open("README.txt").read() + "\n" +
                       open("CHANGES.txt").read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='plone discussion plone.app.discussion spam akismet',
      author='Timo Stollenwerk',
      author_email='timo@zmag.de',
      url='http://pypi.python.org/pypi/collective.akismet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'akismet',
          'plone.app.registry',
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
