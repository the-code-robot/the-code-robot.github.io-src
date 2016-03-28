update to make_sslcert.py script
################################
:date: 2012-03-09 12:50
:author: Robin Abbi (noreply@blogger.com)
:slug: update-to-make_sslcertpy-script

.. raw:: html

   <div>

{{{

.. raw:: html

   </div>

.. raw:: html

   <div>

#!/usr/bin/env python

.. raw:: html

   </div>

.. raw:: html

   <div>

"""

.. raw:: html

   </div>

.. raw:: html

   <div>

A self-signed certificate generator.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl genrsa" generates a private key

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl req" generates a certificate signing request

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl rsa" removes the passphrase

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl x509 -req" creates the certificate from the certificate signing
request and the private key with the passphrase removed.

.. raw:: html

   </div>

.. raw:: html

   <div>

"""

.. raw:: html

   </div>

.. raw:: html

   <div>

import os

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

\_name="server"

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

commands = [

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl genrsa -des3 -out %s.key 1024" % \_name,

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl req -new -key %s.key -out %s.csr" % (\_name,\_name),

.. raw:: html

   </div>

.. raw:: html

   <div>

"cp %s.key %s.key.org" % (\_name,\_name),

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl rsa -in %s.key.org -out %s.key" % (\_name,\_name),

.. raw:: html

   </div>

.. raw:: html

   <div>

"openssl x509 -req -in %s.csr -signkey %s.key -out %s.crt" %
(\_name,\_name,\_name)

.. raw:: html

   </div>

.. raw:: html

   <div>

]

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

for c in commands:

.. raw:: html

   </div>

.. raw:: html

   <div>

 os.system(c)

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

#credit to http://www.akadia.com/services/ssh\_test\_certificate.html
where the information comes from.

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

#When you run this code, where it asks for Common Name or YourName,
enter the name of the host eg - www.example.com or
mywebserver.sales.example.com .

.. raw:: html

   </div>

.. raw:: html

   <div>

.. raw:: html

   </div>

.. raw:: html

   <div>

#See
http://artins.org/ben/how-to-create-a-multihomed-certificate-with-openssl
for creating one certificate to protect multiple hosts.

.. raw:: html

   </div>

.. raw:: html

   <div
   style="font-family: Georgia, serif; font-size: 100%; font-style: normal; font-variant: normal; font-weight: normal; line-height: normal;">

}}}

.. raw:: html

   </div>

.. raw:: html

   </p>

