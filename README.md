# Overview

Kibble is a set of scripts / templates for quickly creating simple CRUD (Create, Read, Update, Delete) apps that require a relational-database-type structure in the backend.

The aim is to fill the gap for a tool where a set of spreadsheets is becoming too complex / slow, but an off-the-shelf dedicated solutions, is too complex, costly, or perscriptive of in terms of structure / workflow, or missing some key element.

The common elements of the need are:
* I want to track a set of genric objects, with their own attributes, and with some relationships between them
* I have a loosely defined workflow, and just want to something that is CRUD and customizable.
* It's not for some large customer / official product, just aims to meet a personal / internal need (ie, not mission / product critical)
* (optionally) I would like to integrate with some external system that has a well-published API (eg BambooHR, smartsheets, Asana, Github, Slack, etc)

Some example applications include:
* home / hobby inventory system
* ticket tracking / bug tracking with custom rankings
* project + resource + milestone management
* requirement / test / result tracking system

# Standard libraries / functions
The aim is to have a set of standard functinality that is available in the "main-branch" that can be merged into the specific applications. The following things come out-of-the-box:
* Flask / Postgres / SQLAlchemy backend requirements

## Implented so far
* virtualenv with Flask server

## TODO
* Auto-create history table for each table by default
* tagging infrastructure
* Authentication using OAuth
* CSS templates for standard pages and widgets
* bash script for automating the per-app config

# Setup Notes

## Host setup
Only required once, not for each application
1. Install virtualenv using `pip install virtualenv`
1. Setup autoenv using `pip install autoenv`
1. Install heroku CLI as per: https://devcenter.heroku.com/articles/heroku-cli
1. Setup automatically entering the virtualenv:
```
echo "source `which activate.sh`" >> ~/.bashrc
source ~/.bashrc
```
1. Install postgres on local machine
1. Install redis on local machine as per https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-redis-on-ubuntu-16-04

## New application Setup

### Set up local development environment
1. Clone kibble git repo
1. Create new virtual environment using `virtualenv env`
1. Create heroku production and staging apps with `heroku create X`
1. Add remotes w/ `git remote add pro git@heroku.com:YOUR_APP_NAME.git`
1. Configure heroku environment settings

```
heroku config:set APP_SETTINGS=config.StagingConfig --remote stage
heroku config:set APP_SETTINGS=config.ProductionConfig --remote pro
```
### Set up databases

1. Create psql database locally for development
```
psql
CREATE DATABASE <application name>
```
1. Update the DATABASE_URL variable in .env to use the application name. 
1. Setup models 
1. Initialize alembic
```
python manage.py db init
python manage.py db migrate
```
1. Add postgres add-ons to remotes
```
heroku addons:create heroku-postgresql:hobby-dev --app <app name>
```
1. Migrate development databases to staging
```
heroku run python manage.py db upgrade --app <app name>
```

## General notes
* To update the requirements file, use `pip freeze > requirements.txt`
migration:
```
python manage.py db migrate
python manage.py db upgrade
```