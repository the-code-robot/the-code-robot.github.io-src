Swagger driven testing in Python
################################
:date: 2017-02-24 22:55
:author: Robin Abbi (robin.abbi@downley.net)
:slug: swagger-driven-testing-in-python
:tags: testing, swagger, openapi, python, microservices, flask
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

Step 1 Write Swagger Specification
----------------------------------
Before getting started, a word of advice. I found that it was best to start with a minimal swagger specfication. There is an interplay between the swagger file, the application and the application tests which can make it tricky to work out whether it is your code which is not working properly or whether it is your test setup. Starting with the smallest swagger file (ideally only one http method and endpoint (eg GET /pets from the code example below) means you will only have one function to implement in your application in order to achieve passing tests, It also means your swagger file should be quick and easy to validate. Once you get a working setup it will be easy to extend.


Note in the yaml example below the use of the fields operationId and x-example. operationId references a method get_pets in a python module swagproj which you create later. x-example fields are the values that will be used to test your code by the swagger-tester application.

.. code-block:: yaml 
    :linenostart: 1

    swagger: '2.0'
    info:
      title: Pet Shop Example API
      version: "0.1"
    consumes:
      - application/json
    produces:
      - application/json
    security:
      # enable OAuth protection for all REST endpoints
      # (only active if the TOKENINFO_URL environment variable is set)
      - oauth2: [uid]
    paths:
      /pets:
        get:
          tags: [Pets]
          operationId: swagproj.get_pets
          summary: Get all pets
          parameters:
            - name: animal_type
              in: query
              type: string
              pattern: "^[a-zA-Z0-9]*$"
              x-example: dog
            - name: limit
              in: query
              type: integer
              minimum: 0
              default: 100
              x-example: 99
          responses:
            200:
              description: Return pets
              schema:
                type: array
                items:
                  $ref: '#/definitions/Pet'
              examples:
                'application/json':
                  cheese: "cheddar"
    
    definitions:
      Pet:
        type: object
        required:
          - name
          - animal_type
        properties:
          id:
            type: string
            description: Unique identifier
            example: "123"
            readOnly: true
          name:
            type: string
            description: Pet's name
            example: "Susie"
            minLength: 1
            maxLength: 100
          animal_type:
            type: string
            description: Kind of animal
            example: "cat"
            minLength: 1
          created:
            type: string
            format: date-time
            description: Creation time
            example: "2015-07-07T15:49:51.230+02:00"
            readOnly: true
    
    
    securityDefinitions:
      oauth2:
        type: oauth2
        flow: implicit
        authorizationUrl: https://example.com/oauth2/dialog
        scopes:
          uid: Unique identifier of the user accessing the service.

Step 2 Validate Swagger Specification
-------------------------------------

I use https://www.npmjs.com/package/swagger-cli to perform command line validation.

.. code-block:: bash
    :linenostart: 1

    $ sudo -H npm -g install swagger-cli
        
    # Usage:
        
    $ swagger validate petshop.yaml
    petshop.yaml is valid

Now that we a minimal validated swagger specification the first thing to do is to test it out. This involves creating a bare flask application and using the swagger file to automagically create the flask application endpoints within it.

Step 3 Create Bare Flask Application
------------------------------------

The magic that makes all this possible is the https://github.com/zalando/connexion project. Add it to your project:

.. code-block:: bash
    :linenostart: 1

    $ pip install connexion


Then import connexion into your bare flask application:

.. code-block:: python
    :linenostart: 1

    # swagproj.py
    import connexion
    
    app = connexion.App(__name__)
    app.add_api('swagger/my_api.yaml')
    
    # set the WSGI application callable to allow using uWSGI:
    # uwsgi --http :8080 -w app
    application = app.app
    
    if __name__ == '__main__':
        app.run(port=8080)

If you try to start the connexion server, you will find that if fails with an error. The last line of the stack trace might read 

.. code-block:: python
    :linenostart: 1

    connexion.exceptions.ResolverError: <ResolverError: Cannot resolve operationId "swagproj.get_pets"!>

What this tells us is that we have not implemented the endpoint for our GET /pets endpoint defined in our swagger yaml specification.

Let's update swagproj.py to include the get_pets implementation.

.. code-block:: python
    :linenostart: 1

    # swagproj.py
    import connexion

    def get_pets():
	return [{
	    'animal_type': 'cat',
	    'created': '2015-07-07T15:49:51.230+02:00',
            'id': '123',
            'name': 'Susie'}]

    
    app = connexion.App(__name__)
    app.add_api('swagger/my_api.yaml')
    
    # set the WSGI application callable to allow using uWSGI:
    # uwsgi --http :8080 -w app
    application = app.app
    
    if __name__ == '__main__':
        app.run(port=8080)

Now your application should start. As a bonus, the swagger ui is available at 'http://<your-server-name>:8080/ui'.

Let's review what we have achieved:

* Written a swagger specification

* Validated the swagger specification

* Implemented a basic http server which refuses to start unless the swagger endpoints have implementations (even if they are just stubs.)

* Got free access to the swagger ui with no extra work.

Next shall create try to see if we can use the information in our swagger specification to test our implementation.


Step 4 Use swagger specfication to test implementation
------------------------------------------------------

First install https://github.com/Trax-air/swagger-tester .

.. code-block:: bash
    :linenostart: 1

    $ pip install swagger-tester

Then you can move on to writing the actual test.

.. code-block:: python
    :linenostart: 1

    # test_swagproj.py
    import unittest
    
    from swagger_tester import swagger_test
    
    
    class TestTester(unittest.TestCase):
    
        def test_server(self):
            swagger_test(app_url='http://localhost:8080', use_example=True)

As you can see, the test assumes that you have an instance of your application up and serving. If this is not the case your tests won't work. There is a mode within swagger-tester which works via a swagger yaml specification file directly - it uses it to start a connexion server in another thread, however I have not yet worked out how to get this mode to execute.

As you would expect, if you wish to use this test setup, you may wish to initialize your application with test fixtures for the database if there is any chance of your tests affecting production systems.

Conclusion
----------

I like the above approach. To me, it feels that the steps are in the right order. It is cumbersome to build a Swagger specification - for me that's the toughest part. I'm on the lookout for tools, and there must be some, which might make that job a little easier. The Swagger Editor is great - but that requires me to write yaml and then show me graphically what I wrote. I am hoping to find a tool which works the other way round - I populate a gui and it writes the yaml.
