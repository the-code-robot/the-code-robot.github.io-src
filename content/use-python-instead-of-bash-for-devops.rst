Use Python instead of Bash for DevOps
#####################################
:date: 2017-01-01 10:39
:author: Robin Abbi (robin.abbi@downley.net)
:slug: use-python-instead-of-bash-for-devops

Maximize resources on the application
-------------------------------------
When working on a project it seems wrong to spend more time on the plumbing around the project than on the project application code. My definition of plumbing includes anything written in <insert name of preferred shell>.

All code should be testable
---------------------------
To me it seems wrong to treat plumbing code as a lesser species than application code. Code is code. And code should be tested, or at least testable. I don't know of any framework for testing shell scripts.

Code to your team's strengths
-----------------------------
I am not as proficient at Bash as I am in Python. I have not worked on a devops project where anyone else was better at shell scripting than they were at Python. If both Bash and Python are able to achieve the same end without deleterious side-effects (eg inefficiency in execution), what reason whould there be to use a tool with which I am less familiar? 

Summary
-------
For the working devopsist, cognitive load is already pretty high. The mental cost of context switching is a well known issue in software development. Anything that reduces the number of things you need to know, and the number of times you need to switch contexts is worth experimenting with if it might make you better at delivering quality projects.

References
----------
1. http://superuser.com/questions/414965/when-to-use-bash-and-when-to-use-perl-python-ruby/936296#936296
2. https://en.wikipedia.org/wiki/Task_switching_(psychology)
3. https://www.quora.com/How-can-programmers-deal-with-the-cognitive-load-of-programming
