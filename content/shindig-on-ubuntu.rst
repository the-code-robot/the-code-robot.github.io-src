Shindig on Ubuntu
#################
:date: 2011-01-15 07:01
:author: Robin Abbi (noreply@blogger.com)
:slug: shindig-on-ubuntu

I was busy building a Google Gadget when I ran into a glitch. My
gadget worked fine in the gagdget container on Google Sites and iGoogle
but did not work too well on "Gadgets-For-Your-Webpage". (according to
Firebug gadgets.io was undefined.)
In any case, my grand plan to use Google's container for gadgets for
my own site was clearly not going to fly - it was a poor idea to rely
too much on a third party service for this type of thing.
So I decided to install
`Shindig <http://shindig.apache.org/index.html>`__. This would allow my
gadgets to be re-used all around the web, as long as I can keep the
shindig service running.

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Shindig gives the choice of a PHP or Java version. I chose PHP.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

My server was Ubuntu 10.04.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I had Apache already installed.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

First things first - check that PHP exists on my box. That would be a
no.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

sudo aptitude install php5

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Then check that it runs with the classic phpinfo(); script of your
choice.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

testphp.php

.. raw:: html

   </div>

.. raw:: html

   <div>

<?php

.. raw:: html

   </div>

.. raw:: html

   <div>

echo phpinfo();

.. raw:: html

   </div>

.. raw:: html

   <div>

?>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Yes, PHP's up and running

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Shindig has PHP dependencies - mcrypt, curl, simplexml and json.

.. raw:: html

   </div>

.. raw:: html

   <div>

But grepping through the output of phpinfo() there is no curl and mcrypt
module.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Let's fix that.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

sudo aptitidue install php5-mcrypt php5-curl

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Now we have a working PHP environment.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Next up, configure Apache for Shindig.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Shindig requires that it's .htaccess file be honoured and also that
mod\_rewrite be enabled.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

First, mod\_rewrite. In my Apache out-of-the-box setup mod\_rewrite was
not enabled. That was an easy fix:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

cd /etc/apache2/mods-enabled

.. raw:: html

   </div>

.. raw:: html

   <div>

ls -s ../rewrite.load

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I'm not a big .htaccess fan. Which means I want to configure Apache to
honour .htaccess in the Shindig installation directory. And to do that,
I need to install Shindig.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

So, get the Shindig application from here:
http://www.apache.org/dist/shindig/2.0.0/shindig-2.0.0-php.tar.gz

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

I unpacked it to /var/www and then I renamed it form shindig-2.0.0 to
just plain old shindig.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

cd ~

.. raw:: html

   </div>

.. raw:: html

   <div>

wget http://www.apache.org/dist/shindig/2.0.0/shindig-2.0.0-php.tar.gz

.. raw:: html

   </div>

.. raw:: html

   <div>

cd /var/www

.. raw:: html

   </div>

.. raw:: html

   <div>

tar xfzv ~/shindig-2.0.0-php.tar.gz

.. raw:: html

   </div>

.. raw:: html

   <div>

mv shindig-2.0.0 shindig

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

So, in the appropriate part of my Apache config, in my case
/etc/apache2/sites-available/default enabled the .htaccess file thus:

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

<Directory>

.. raw:: html

   </div>

.. raw:: html

   <div>

AllowOverride All

.. raw:: html

   </div>

.. raw:: html

   <div>

</Directory>

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

Next up is the configuration of the Shindig application itself.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

In version 2.0.0 there is a README file at the top level of the unpacked
distribution. It describes two options for installing Shindig. Option A,
is to create a new virtual host container in Apache, Option B is to use
an existing configuration. For me, option B was the more practical.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

The instructions contained in the
`README <http://svn.apache.org/repos/asf/shindig/tags/shindig-project-2.0.0/php/README>`__
have are two small errors in the B instructions:

.. raw:: html

   </div>

.. raw:: html

   <div>

#. paths beginning php/ are incorrect.
#. no reference is made to the need to edit the .htaccess file.

.. raw:: html

   </div>

.. raw:: html

   <div>

To correct error 1 above, just ignore the php part of the path because
there is no php directory in the PHP Shindig distribution. [ It looks
like what has happened is that the instructions where written for use
from the Subversion source tree, where the PHP and JAVA versions live
side by side in /php/ and /java/ directories respectively] I installed
Shindig to /var/www/shindig and the correct path for web\_prefix was
/shindig .

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

To correct error 2, just know that you need to edit the .htaccess file.
Once you know this, you will find the instructions in the file itself.
But if you didn't already know that, you would be a bit stuck.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

That's it. Enjoy using Shindig.

.. raw:: html

   </div>

.. raw:: html

   </p>

