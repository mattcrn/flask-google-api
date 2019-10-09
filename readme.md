# Docker Flask Boilerplate

A fast way to start your next flask project.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Make sure you have installed to following dependencies before moving on:

* Docker
* Docker-Compose
* [jwilder's nginx-proxy](https://github.com/jwilder/nginx-proxy)

### Installing

First, adapt the following lines in the docker-compose.yml ot your needs:

```
my-service:
```
will be the name for the service
```
container_name: my-container
```
will be the name of the container
```
VIRTUAL_HOST: my-app.local
```
will be your dev URL
<br />

Save the File and run:

```
docker-compose up -d
```

Now add the dev URL to your .hosts file like this:

```
127.0.0.1 my-app.local
```
Now visit the dev URL and you should be greeted with:
>This is my Flask App!

## Deployment

To deploy an app you can simply build and deploy the docker image.

