Tickets
=========

A web application that provides dashboard for viewing statuses of existing bug tickets.

## Ticket structure

Name: Required
Status: Required, available options are:
  0 (Reported)
  1 (In Progress)
  2 (In review)
  3 (Resolved)
URL: Optional

## What is needed to do

1. Render a listing view at `/tickets`
2. Render an individual ticket's information at `/tickets/:id`
3. Provide a JSON API for `/api/tickets` and `/api/tickets/:id`

## Database details

user - `demo`
database - `dashboard`
password - `securepassword`
table - `ticket`
  `id` - (UUID, required, automatic) unique identifier
  `name` - (string, 100 character limit, required) name of ticket
  `status` - (integer, required, default `0`) state of ticket (see information above)
  `url` - (string, 100 character limit, optional)

## Useful documentation and Packages

Flask `http://flask.pocoo.org/docs/1.0/`
Flask - Database Configuration `http://flask.pocoo.org/docs/1.0/tutorial/database/`
Flask - Views `http://flask.pocoo.org/docs/1.0/tutorial/views/`
Flask - Templates `http://flask.pocoo.org/docs/1.0/tutorial/templates/`
Flask - SQLAlchemy `http://flask-sqlalchemy.pocoo.org/2.3/quickstart/`
psycopg2 `http://initd.org/psycopg/`
