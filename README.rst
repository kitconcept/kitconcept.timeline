.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

==============================================================================
kitconcept.timeline
==============================================================================

.. image:: https://secure.travis-ci.org/kitconcept/kitconcept.timeline.svg?branch=master
    :target: http://travis-ci.org/kitconcept/kitconcept.timeline

.. image:: https://img.shields.io/pypi/status/kitconcept.timeline.svg
    :target: https://pypi.python.org/pypi/kitconcept.timeline/
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/v/kitconcept.timeline.svg
    :target: https://pypi.python.org/pypi/kitconcept.timeline
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/l/kitconcept.timeline.svg
    :target: https://pypi.python.org/pypi/kitconcept.timeline
    :alt: License

|

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.timeline/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/


kitconcept.timeline allows to create a timeline in Plone.


Features
--------

- Adds Timeline and TimeLineEntry content types (Dexterity based)
- Displays a timeline overview


Examples
--------

This add-on can be seen in action at the following sites:

- Is there a page on the internet where everybody can see the features?


Translations
------------

This product has been translated into

- German


Installation
------------

Install kitconcept.timeline by adding it to your buildout::

    [buildout]

    ...

    eggs =
        kitconcept.timeline


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/kitconcept/kitconcept.timeline/issues
- Source Code: https://github.com/kitconcept/kitconcept.timeline


Support
-------

If you are having issues,
`please let us know <https://github.com/kitconcept/kitconcept.timeline/issues>`_.

If you require professional support, feel free to drop us a note at info@kitconcept.com.


Credits
-------

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.timeline/master/dpg.svg
   :height: 97px
   :width: 434px
   :scale: 100 %
   :alt: Deutsche Physikalsiche Gesellschaft
   :target: https://www.dpg-physik.de/

|

The development of this plugin has been kindly financed by the `Deutsche Physikalische Gesellschaft`_.

|

.. image:: https://raw.githubusercontent.com/kitconcept/kitconcept.timeline/master/kitconcept.png
   :alt: kitconcept
   :target: https://kitconcept.com/

Developed by `kitconcept`_.


License
-------

The project is licensed under the GPLv2.

.. _Deutsche Physikalische Gesellschaft: https://www.dpg-physik.de
.. _kitconcept: http://www.kitconcept.com/

Development
-----------

Requirements:

- Python 2.7
- Virtualenv

Setup::

  make

Run Static Code Analysis::

  make code-Analysis

Run Unit / Integration Tests::

  make test

Run Robot Framework based acceptance tests::

  make test-acceptance
