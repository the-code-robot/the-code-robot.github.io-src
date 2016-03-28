Plone and Subversion
####################
:date: 2008-05-16 16:01
:author: Robin Abbi (noreply@blogger.com)
:slug: plone-and-subversion

.. raw:: html

   <p>

When making a plone product in subversion, setup the repository thus:

::

    package.module/trunk/package.module/package/module


This will allow you to checkout your product into the src directory:

::

    http://svn.example.com/svn/package.module/trunk/package.module


Don't forget to do this after running bootstrap.py but before running
the buildout.

.. raw:: html

   </p>

