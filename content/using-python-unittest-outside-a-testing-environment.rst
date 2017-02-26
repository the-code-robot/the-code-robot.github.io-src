Using Python unittest outside a testing environment
###################################################
:date: 2015-12-21 22:28
:author: Robin Abbi (noreply@blogger.com)
:tags: outside the box, python, testing, unittest
:slug: using-python-unittest-outside-a-testing-environment


Test frameworks are not just for testing code during development and
deployment.

Test frameworks may also be put to good use within your application.
By way of example, consider the possibility of running diagnostics on
a live application. Another possibility is checking the validity of an
on-the-fly configuration change.

The Python unittest library, part of the standard distribution can
easily be incorporated into your live code.

The code example below presents a toy example of a test case, which is
then exercised by your application process. The outcome is a test result
object which you can query and report on.

.. code-block:: python
    :linenostart: 1

    import unittest
    class TestMe(unittest.TestCase):

        def test_this(self):
            self.assertTrue(False)

        def test_that(self):
            self.assertTrue(True)

    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestMe)
    result = unittest.TestResult()
    suite.run(result) # run actually returns result as well as populating it
    print result


.. code:: python

    <unittest .result.testresult="" errors="0" failures="1" run="2">

The variable 'result' is an instance of unittest.TestResult() and has a rich set of attributes and methods as `documented
here <https://docs.python.org/2/library/unittest.html#unittest.TestResult>`__.
