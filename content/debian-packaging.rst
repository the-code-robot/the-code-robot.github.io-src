Debian Packaging
################
:date: 2011-06-27 14:44
:author: Robin Abbi (noreply@blogger.com)
:slug: debian-packaging

How I made a .deb file

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Create a directory

.. raw:: html

   </div>

.. raw:: html

   <div>

mkdir foo

.. raw:: html

   </div>

.. raw:: html

   <div>

Descend into it.

.. raw:: html

   </div>

.. raw:: html

   <div>

cd foo

.. raw:: html

   </div>

.. raw:: html

   <div>

Create a directory DEBIAN

.. raw:: html

   </div>

.. raw:: html

   <div>

mkdir DEBIAN

.. raw:: html

   </div>

.. raw:: html

   <div>

Descend into it.

.. raw:: html

   </div>

.. raw:: html

   <div>

Create a text file called 'control'

.. raw:: html

   </div>

.. raw:: html

   <div>

vim control

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Create key:value pairs as per
http://www.debian.org/doc/debian-policy/ch-binary.html

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The postinst and prerm scripts also go in the DEBIAN directory.

.. raw:: html

   </div>

.. raw:: html

   <div>

The actual install files go in the foo directory

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo/DEBIAN

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo/DEBIAN/control

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo/DEBIAN/postinst

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo/DEBIAN/prerm

.. raw:: html

   </div>

.. raw:: html

   <div>

./foo/bar.....

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Finally, go to the directory above foo and do:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

dpkg -b ./foo foo.deb and that is it! done!

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   </p>

