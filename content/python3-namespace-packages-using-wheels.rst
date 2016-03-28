Python3 Namespace Packages Using Wheels
#######################################
:date: 2015-12-06 23:28
:author: Robin Abbi (noreply@blogger.com)
:tags: namespace package, python3, wheel
:slug: python3-namespace-packages-using-wheels

| I was experimenting with Python3.4 and namespace packages.

| Here's what I did.

| I created two completely separate repos, A and B.

| I had a top level namespace, toplevel.

| I created a directory structure:

| repoA/toplevel/libA/moda.py

| repoA/setup.py

| repoB/toplevel/libB/modb.py

| repoB/setup.py

| The setup.py files were very similar:

| from setuptools import setup

| setup(

|     name = "toplevel libA",

|     version = "0.1",

|     packages = ['toplevel.libA']

| )

| and:

| from setuptools import setup

| setup(

|     name = "toplevel libB",

|     version = "0.1",

|     packages = ['toplevel.libB']

| )

| To be able to work with the bdist\_wheel extension to setuptools, I

had to use pip to install wheel.
| pip install wheel

| Then in repoA and repoB it was possible to execute:

| python setup.py bdist\_wheel -d /tmp/wheels

| In this way, two wheels were created:

| /tmp/wheels/toplevel.libB-0.1-py3-none-any.whl

| /tmp/wheels/toplevel.libA-0.1py3-none-any.whl

| 

I then created a third project repo which used these two wheel packages.
| repoC/someotherproject

| In this repo, after creating and virtual envirionment, it was possible

to install the two wheels:
| pip install /tmp/wheels/toplevel.libB-0.1-py3-none-any.whl

| pip install /tmp/wheels/toplevel.libA-0.1py3-none-any.whl

| 

In the site-packages directory of the repoC environment there was a tree
structure installed:
| ./toplevel/liba

|           /libb

| Showing that libA and libB, although separately developed, were

available in the client project as a unified namespace. (Note that liba
and libb could have been independently installed on different branches
of sys.path and they would stilll appear to the interpreter as an
integrated whole.)
