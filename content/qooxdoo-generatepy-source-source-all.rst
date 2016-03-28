Qooxdoo generate.py source, source-all
######################################
:date: 2011-10-21 08:28
:author: Robin Abbi (noreply@blogger.com)
:slug: qooxdoo-generatepy-source-source-all

Health warning - this may not be accurate but it reflects my current
understanding.
When you write an application in Qooxdoo, your raw code has to be
referenced into a master javascript file which is loaded by the browser.
You do this initially by running the generate source command.
Thereafter, provided you do not refer to any new classes (either ones
you have written or ones provided by qooxdoo or contributors) you may
simple edit your code and refresh the browser to see your changes. No
need to run generate.
But if you create some new classes in your application, the master
javascript file does not know about them. Therefore you need to run
generate source again to update the master.
Or if you decide to use some additional qooxdoo classes then again the
master javascript file does not know about this change and you will need
to run generate source so that it knows to include the additional
qooxdoo classes.
Because in writing your qooxdoo application it is much more common for
you to add references to qooxdoo classes than it is to create additional
classes of your own, the generate source-all command exists. This causes
the master javascript file to contain references to all the qooxdoo
classes whether you are currently using them or not. Thus, provided you
are not writing any new classes of your own, you can in future skip the
generate source command entirely. To see the effect of your code changes
you need only refresh the browser.
In a nutshell, the difference between source and source-all is that
using source-all can save you time in development because you only need
to recompile the master when you add new classes of your own. If you
were not to use source-all you would need to recompile every time you
made reference to a new qooxdoo class.
This thread was the source of this article:
http://qooxdoo.678.n2.nabble.com/v0-8-generate-py-source-to-include-even-qx-classes-tp1556404p1556404.html
