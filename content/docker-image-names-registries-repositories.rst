Docker image names, registries and repositories
###############################################
:date: 2016-12-29 23:37
:author: Robin Abbi (robin.abbi@downley.net)
:slug: docker-image-names-registries-and-repositories

A docker push or pull command requires an image name whose structure is:

[<registry>/]<repository>[:<tag>]


The registry part is optional and if not detected will default to docker.io

I presume that when you run docker push for example, that the previous login primes docker to expect that a subsequent push might have a registry hostname at the front.
