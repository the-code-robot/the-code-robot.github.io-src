Create a custom content type in Plone3
######################################
:date: 2008-04-27 16:27
:author: Robin Abbi (noreply@blogger.com)
:tags: plone
:slug: create-a-custom-content-type-in-plone3

.. raw:: html

   <p>

::

    paster create -t plone <somepackage.somemodule>

Then edit the buildout.cfg to record the egg in the:
eggs section,(somepackage.somemodule)
develop eggs section (src/somepackage.somemodule)
and the instance zcml section (to put the zcml slug in)
then:-

::

    ./bin/buildout -o


Create the initiailize function in the
somepackage.somemodule.\_\_init\_\_.py file. Other examples say this is
also the place where you can create a MessageFactory object.
The initialize function makes reference to the content object being
created so you need to have that created.

::

    $> mkdir content$> cd content$> touch contentthing.py


Also, it is suggested in the Optilude book that you create a config.py
file to contain various constants to enable easier future reference.
The body of the contentthing.py breaks down into a few sections.
Firstly you define a schema for the content type. The schema defines
the what parts the content type has, and what type of thing those parts
are. The schema begins by copying the already existing general purpose
schema using *atapi.ATContentTypeSchema.copy()* and to this you then add
your own, using *atapi.Schema()*.
Once the schema has been defined it has to be finalized. This requires
hints as to whether or not the schema is folder-like, and whether or not
conversations can be moved (don't understand this part).
After the schema is in place one may then move on to define the
content type class proper.
The class inherits from *base.ATCTContent*.
The class has a *schema* attribute. It should be no surprise that the
schema is set to the one just created. The class is also given a
*portal\_type* attribute. This value is a string value, presumably used
for UI purposes. The class also calls the *zope.interface.implements()*
method. Previously you will have defined a zope style interface for the
product. I did this, although I set the interface to *pass*. I'm not
sure why the zope interface is required when there is already an
Archetypes schema. Perhaps they are just preparing for the future?
The class is next given a series of attributes. These attributes are
made to have the same names as those created in the schema, but are all
initialized using methods such as *atapi.ATFieldProperty()*.
Finally, after trhe class has been defined, the module registers the
class thus:
*atapi.registerType(<classname>, PROJECTNAME)*
At this stage, if you try to install the content type to plone, you
should find that the restart succeeds, and that the product appears in
the product section of the ZMI. However, the product will be invisible
to Plone.
We make the product visible to plone by going the the package's
*configure.zcml* file and using the generic setup extension profile
mechanism. A good example of this is on page 71 of the Professional
Plone Development book.
Restarting zope at this point will allow the product to appear in the
"Add New Products" section of the "Site Setup" page in the Plone
interface.
Installing the product should proceed without error. The next hurdle
will be that the product is not present in the "Add new ..." drop down
menu in the Plone user interface.
We make the product appear as addable in the UI by the simple
expedient of going to the *profile/defaults/types/<sometype>.xml* and
ensure that *global\_allow* property is set to true.

.. raw:: html

   </p>

