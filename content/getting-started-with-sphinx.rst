Getting started with Sphinx
###########################
:date: 2015-12-05 07:59
:author: Robin Abbi (noreply@blogger.com)
:tags: documentation generation, pdoc, python, sphinx
:slug: getting-started-with-sphinx

I really like `pdoc <https://github.com/BurntSushi/pdoc>`__ as a great
lightweight python source code documentation tool.
I like to invoke it:
*PYTHONPATH=. pdoc --http --http-host 0.0.0.0 --http-port 8888
--only-pypath*
I like to use `ReST to format
docstrings <http://stackoverflow.com/questions/5334531/python-documentation-standard-for-docstring>`__.
Unfortunately I have not been able to get pdoc to display parameter
lists as I would hope.
(UPDATE: 20151205: pdoc will honour parameter lists created using
Markdown.)
So I switched to using Sphinx. It seems I am not alone in finding the
`Sphinx documentation hard to
use <http://stackoverflow.com/questions/4616693/automatically-generating-documentation-for-all-python-package-contents>`__.
After a bit of futzing around, this recipe meets my objective of
having nice documentation with the power of Sphinx but the ease of pdoc.
1. Install Sphinx.
2. Invoke sphinx-apidoc -F -o dox
3. cd to the dox directory.
4. Edit conf.py to ensure that sys.path can find the module to be
document.
5. make html
6. python3 -m http.server
I hope it works for you.
