Generate self-signed SSL cert
#############################
:date: 2011-06-30 13:10
:author: Robin Abbi (noreply@blogger.com)
:slug: generate-self-signed-ssl-cert

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

   </p>

