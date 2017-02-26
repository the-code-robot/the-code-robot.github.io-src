Android Studio up and running
#############################
:date: 2015-06-14 11:25
:author: Robin Abbi (noreply@blogger.com)
:tags: android, android studio, ant, gradle, zipzipbooks
:slug: android-studio-up-and-running
:category: android

My standard development environment for native Android development has
been Vim and Ant.

Today I finally took the plunge and got started with Android Studio
(AS).

I ported in ZipZipBooks, which is my mobile record keeping application
for HMRC with a view to giving at a bit of a refresh. Didn't take too
long to get it up and running on AS.

Key issues:

#. The code for the existing project is in a Mercrurial repository. My
   first attempt to import the project, I went down the "Check out the
   project from version control" route, and chose Mercurial.
   Unfortunately this did not play niceley with Gradle. Instead, I found
   that I could instead start with the "Import Project" route. That
   allowed AS to convert my Ant build to Gradle.
#. Adding library dependencies for which `this
   answer <http://stackoverflow.com/a/18321935/4999639>`__ was very
   helpful;
#. I might need to get a faster/bigger/hotter/noisier laptop.
#. Running on Windows 8, there was no need to update any drivers for the
   physical Android devices on which I performed testing.

