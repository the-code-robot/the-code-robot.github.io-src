update to make_sslcert.py script
################################
:date: 2012-03-09 12:50
:author: Robin Abbi (noreply@blogger.com)
:slug: update-to-make_sslcertpy-script

.. code:: python

  #!/usr/bin/env python

  """
  A self-signed certificate generator.
  "openssl genrsa" generates a private key
  "openssl req" generates a certificate signing request
  "openssl rsa" removes the passphrase
  "openssl x509 -req" creates the certificate from the certificate signing
  request and the private key with the passphrase removed.
  """

  import os
  _name="server"
  
  
  commands = [
      "openssl genrsa -des3 -out %s.key 1024" % _name,
      "openssl req -new -key %s.key -out %s.csr" % (_name,_name),
      "cp %s.key %s.key.org" % (_name,_name),
      "openssl rsa -in %s.key.org -out %s.key" % (_name,_name),
      "openssl x509 -req -in %s.csr -signkey %s.key -out %s.crt" % (_name,_name,_name)
  ]
  
  for c in commands:
      os.system(c)
  
  #credit to http://www.akadia.com/services/ssh_test_certificate.html where the information comes from.
  
  #When you run this code, where it asks for Common Name or YourName, enter the name of the host eg - www.example.com or mywebserver.sales.example.com .
  
  
  #See http://artins.org/ben/how-to-create-a-multihomed-certificate-with-openssl for creating one certificate to protect multiple hosts.

