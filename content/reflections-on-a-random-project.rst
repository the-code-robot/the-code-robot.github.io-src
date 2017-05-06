Reflections on a random project
###############################
:date: 2017-04-11 10:01
:author: Robin Abbi (noreply@blogger.com)
:tags: python
:slug: reflections-on-a-random-project
:category: engineering

Project: netflix/Aminator

Notes:

* NullHandler for logs.
* info() on entrance and exit, debug for the innards.
* use of __all__ = () for __init__.py .
* setup.cfg and pbr from Openstack.
* Docstrings used, and occasional comments in code, including TODO.
* Sphinx for docs, with its own Makefile.
* Use of __metaclass__.
* Uses abstract base class.
* comma separated imports.
* Long code lines, but not too long.
* Deeply nested context managers.
* When implementing context managers, sometimes they are defined:

.. code-block:: python

    def __exit__(self, typ, val, trc):
        pass

and at other times:

.. code-block:: python

    def __exit__(self, exc_type, exc_value, trace):
        pass

* use of @property decorators.
* variable names use snake case.
* Git used. Commit messages are one or two lines.
* Authors can merge their own code after one review.
* Pull requests are comprehensively described.
* Does not use relative imports.
