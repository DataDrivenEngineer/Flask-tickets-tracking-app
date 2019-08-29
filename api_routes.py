from flask import Flask, Blueprint, render_template, url_for, redirect, request, jsonify, g, session

from .models import db, Ticket

api_routes_bp = Blueprint('api', __name__.split('.')[0], url_prefix='/api')

@api_routes_bp.route('/tickets', methods=('GET', 'POST'))
def get_all_tickets_api():
    list_of_tickets = []
    tickets = db.session.query(Ticket).all()
    for ticket in tickets:
        ticket_dict = {}
        ticket_dict['ticket_id'] = ticket.id
        ticket_dict['ticket_name'] = ticket.name
        ticket_dict['ticket_status'] = ticket.status
        ticket_dict['ticket_url'] = ticket.url
        list_of_tickets.append(ticket_dict)

    return jsonify(list_of_tickets)

@api_routes_bp.route('/tickets/<uuid:ticket_uuid>')
def get_ticket_api(ticket_uuid):
    ticket = db.session.query(Ticket).filter_by(id = ticket_uuid).first()
    ticket_dict = {}
    ticket_dict['ticket_id'] = ticket.id
    ticket_dict['ticket_name'] = ticket.name
    ticket_dict['ticket_status'] = ticket.status
    ticket_dict['ticket_url'] = ticket.url

    return jsonify(ticket_dict)
