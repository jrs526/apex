# ApEx

An API Example project with basic asynchronous workers.  The basic scripts make
use of Heroku's tool belt, but there's no reason that it can't be deployed
differently.


## Setup
You should make (and use) a `virtualenv`.  If you don't have
`virtualenvwrapper` installed, I recommend doing that.

Once `virtualenvwrapper` is installed, you can simply:

```bash
mkvirtualenv apex
```


## Running a Local (Development) Server
You need 4 things to run locally:

1. A working virtualenv
2. The Heroku tool belt (this isn't strictly necessary, it's just convenient)
3. A running Celery-compatible broker of some kind, with the URL exported to
   `CELERY_BROKER_URL`
4. A running Celery-compatible task backend, with the URL exported to
   `CELERY_RESULT_BACKEND`

For example, the broker (RabbitMQ) & backend (Redis) could be spun up using
docker:

```bash
docker run -P -d --name apex-rabbit rabbitmq
docker run -P -d --name apex-redis redis redis-server
```

Then you simply:

```bash
./scripts/run-local
```


## Deploying to Heroku
To setup a Heroku deployment for experimental purposes, simply:

```bash
./scripts/initialize-heroku
```
