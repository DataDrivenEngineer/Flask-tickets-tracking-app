from flask import Flask, Blueprint, render_template, url_for, redirect, request, jsonify, g, session

from .models import db, Ticket

ticket_routes_bp = Blueprint('tickets', __name__.split('.')[0], url_prefix='/tickets')

@ticket_routes_bp.route('/', methods=('GET', 'POST'))
def index():
    tickets = db.session.query(Ticket).all()
    return render_template('ticket_index.html', tickets=tickets)

@ticket_routes_bp.route('/<uuid:ticket_uuid>')
def show_ticket(ticket_uuid):
    ticket = db.session.query(Ticket).filter_by(id = ticket_uuid).first()
    if not ticket.url:
        ticket.url = '/tickets/' + str(ticket_uuid)
        db.session.add(ticket)
        db.session.commit()

    return render_template('ticket_info.html', ticket=ticket)


