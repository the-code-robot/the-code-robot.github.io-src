Readability vs Correctness
##########################
:date: 2017-05-01 10:01
:author: Robin Abbi (robin.abbi@downley.net)
:tags: self documenting code
:slug: readability-vs-correctness
:category: engineering


I read this today: `Readability Matters More Than Correctness <https://xph.us/2017/04/23/readability.html>`_  which got me thinking about the relationship between readability and self-documenting code. The article itself did not mention self-documenting code but when I think about some of the self-documenting code I have seen (and that I have written), the word that comes to mind is unreadable. I don't know if you find that odd. I do: the paradox of code so clear that it explains itself being at the same time incomprehensible.

Code with absurdly long function and variable names. Code that labels the stages of transformation of a data item by adding the name of the last transformation to an already very long name. And in the case of public APIs, code which forces these monstrosities out into the namespace of the consuming code. How am I meant to form an understanding of code when there is 8 times as much text on screen as there needs to be, and 90% of every name is the same as every other name?


How can such a thing happen?

Relatively easily:

.. code::

    post_request_bananas_prices_protocol_buffer = PostRequestBananasPricesProtocolBuffer()
    post_request_bananas_prices_protocol_buffer.ParseFromString(serialized_post_request_bananas_prices_protocol_buffer)
    bananas_prices_list = convert_post_request_bananas_prices_protocol_buffer_to_banana_prices_list(post_request_bananas_prices_protocol_buffer)


In the code snippet above which is based on a real life example, you can see how the need to provide semantically meaningful names to data items can soon get out of control. And when you have functions which must also be semantically named, you can see how quickly the good intentions of self-documenting code descend into unreadable alphabet soup. Imagine what the code would look like if the method of the last line where to take second parameter. It's also worth noting that nowhere in the self-documenting code can you explain using names that the ParseFromString method is a mutating method that does not return a new object. Now further imagine that this code was part of some public API. Would you really want your customers to be forced to use functions with names like convert_post_request_bananas_prices_protocol_buffer_to_banana_prices_list? It's also obvious that you are at the mercy of method names used in libraries you import.

Sometimes the DRY (Do not repeat yourself)  concept is used to try to justify self-documenting code. This is an incorrect application of the principle as comments and documentation are not a repeat of the code. The correct software engineering metaphor is that of the single-responsibility principle. The comments and documentation have the role of setting out context, requirements, constraints, choices and motivation. The role of the code is to implement. If the code should happen to conform to the comments and documentation then that is not repetition. Rather it shows that each has fulfilled its purpose.

To those who are irritated by code and documentation which are in conflict one with another, there is a remedy. My first law: 'when code and documentation conflict, it is the code which is wrong.' If you adopt this mindset, and you start to have your pull requests rejected because the code you sweated over doesn't match the documentation you ignored, you will learn to document first, code second. An example of this approach is contained in the concept of `Readme Driven Development <http://tom.preston-werner.com/2010/08/23/readme-driven-development.html>`_. You will find that this approach is compatible with an agile way of working.

Finally, because it is late and I am tired, the last nail in the coffin of the corpse that is self-documenting code (which by the way is neither sufficient nor necessary) is this thought: if self-documenation is good for code, shouldn't it be good for mathematics too?

Finally finally, we will let `Stack Overflow have the last word on self-documenting code <http://stackoverflow.com/q/209015>`_ .
