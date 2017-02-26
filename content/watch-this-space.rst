Swagger testing in Python
#########################
:date: 2017-02-24 22:55
:author: Robin Abbi (robin.abbi@downley.net)
:slug: swagger-testing-in-python
:tags: testing, swagger, openapi, python, microservices
:category: microservices

TL;DR
-----
OpenAPI/Swagger can be the governing document for your microservice. Tools are now available to support the workflow: create swagger yaml, validate yaml, create swagger implementation tests, create microservice implemention.

Overview
--------
In microservices architecture, it is important to document and publish the public API. Swagger provides a framework to help you. Introducing Swagger means there are (at least) two descriptions of the API: the Swagger specification and the definition implicit in the implementation of your service. This gives a choice: get your code correct and then create a Swagger specification or create your Swagger definition and then write your code to match. I have tried each method concluding the latter works better for me. Your mileage may vary.

The steps are:
1. Write Swagger specification
2. Validate Swagger specification
3. Write Swagger tests
4. Run Swagger tests.
5. Write service implementation.
6. Iterate until happy.
