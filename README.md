

Kibble is a set of scripts / templates for quickly creating simple apps for personal use that require a relational-database-type structure in the backend.
# Overview

The aim is to address a common application where:
* want to track a set of genric objects (eg milestones, inventory items), with arbitrary properties
* there's some simple relationships between objects (parent/child, etc)
* only have simple uses cases (view objects, filter, simple workflow / lifecycle)
* would like to integrate with some tool (eg BambooHR, smartsheets, Asana, Github, Slack, etc) that has a well-published API
* it's not for some large customer / official product, just aims to meet a personal / internal need (ie, not mission / product critical)

It aims to fill the gap for a tool where:
* a set of spreadsheets is becoming too complex / slow / janky
* there are likely off-the-shelf solutions, but they are too complex, fit the workflow, or are missing

Application ideas:
* home / hobby inventory system
* ticket tracking / bug tracking + ranking system
* project + resource + milestone management
* requirement / test / result tracking system


# Per-app setup

## Host setup
1. Clone kibble git repo
1. Set up virtual environment
1. Install Flask

## Heroku Setup
1. Create production and staging apps with `heroku create X`
1. Add remotes w/ `git remote add pro git@heroku.com:YOUR_APP_NAME.git`

## General notes
* To update the requirements file, use `pip freeze > requirements.txt`