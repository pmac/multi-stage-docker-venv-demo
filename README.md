# Multistage Docker and Virtualenv Demo

Demo app for [my blog post on multistage-dockerfiles and python virtualenvs][blog-post].

## Getting started

Have [Docker][] and [Docker Compose][] installed and then simply run:

```bash
$ docker-compose up
```

This will build the docker image and start the server. So far the service is very simple, but should give you a starting point.
See the [Responder docs][] if you'd like to play around more with that.
I think it's quite an interesting project.

[blog-post]: https://pmac.io/2019/02/multi-stage-dockerfile-and-python-virtualenv/
[Docker]: https://www.docker.com/products/docker-desktop
[Docker Compose]: https://docs.docker.com/compose/overview/
[Responder docs]: https://python-responder.org/en/latest/quickstart.html