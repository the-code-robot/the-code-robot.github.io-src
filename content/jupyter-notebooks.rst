Jupyter notebooks
#################
:date: 2015-12-22 00:08
:author: Robin Abbi (noreply@blogger.com)
:tags: ipython, jupyter
:slug: jupyter-notebooks

.. raw:: html

   <p>

My typical working setup is a headless GNU/Linux VM which I access via
ssh. This means that when I working in a newly initialized project
environment and I want to pop up a Jupyter notebook I do this:

::

    pip install jupyterjupyter notebook

And bang! there I have a w3m text based browser, nicely colourized,
but not what I was hoping for.
Every month or so I go through this. And I have been trained to find
the Jupyter config file or the IPython config file as was and edit it to
suit.
So this time the version of Jupyter which pip harvests for me is
4.0.6. And could I find the configuration? No I could not.
It turns out you have to generate the configuration before you can
actually edit it:

::

    jupyter notebook --generate-config

Once that is done, then you can

#. change the host from localhost to '0.0.0.0' and
#. change start browser by default to 'False'.

Oh, and look for the configuration in

::

    .jupyter

.

.. raw:: html

   </p>

