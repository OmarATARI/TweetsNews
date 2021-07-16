# API News Twitter

## Features

- Fetch tweets according to a seach query and filter by languages
- Fetch last twitter trends according to city locations
- Save tweets and trends in a postgres database
- Export tweets from database to csv file according to parameters submitted to a form

## Stack

We use docker environnement for developpement and deployement:

- Python 3.9 as image
- Flask as python framework
- Material & Boostrap
- Postgresql as database
- SQLalchemy as ORM
- Twitter API v1 

## Installation

### Prerequites

You must have docker installed on your machine to run this project easely.

### Getting started

Create a new .env under frontend folder and replace the variable with your twitter bearer access token.
```sh
cp .env.txt .env
```

Run the projects:
```sh
cp .env.txt .env
docker-compose build
docker-compose up -d
```

Website is now avaible on localhost:5000

## Improvments

- Manage exceptions and errors case
- Improve quality
- Implements unit tests
- Refactor is needed for some parts.
