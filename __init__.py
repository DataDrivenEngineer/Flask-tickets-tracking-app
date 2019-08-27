from flask import Flask, render_template, url_for, redirect, request
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__.split('.')[0])

    app.config.from_mapping(
            SECRET_KEY='dev'
            )

    app.config.from_pyfile('config.py', silent = True)

    from .models import db, Ticket

    migrate = Migrate(app, db)

    db.init_app(app)

    @app.route('/')
    def get_index():
       return redirect(url_for('index'))

    @app.route('/tickets', methods=('GET', 'POST'))
    def index():
        tickets = db.session.query(Ticket).all()
        return render_template('ticket_index.html', tickets=tickets)

    @app.route('/tickets/<uuid:ticket_uuid>')
    def show_ticket(ticket_uuid):
        ticket = db.session.query(Ticket).filter_by(id = ticket_uuid).first()
        if not ticket.url:
            ticket.url = '/tickets/' + str(ticket_uuid)
            db.session.add(ticket)
            db.session.commit()

        return render_template('ticket_info.html', ticket=ticket)

    @app.route('/add_tickets')
    def add_tickets():
        ticket_2 = Ticket(name='Approvers are not assigned automatically', status=2)
        ticket_3 = Ticket(name='App crashes when click "Reject"', status = 3)
        db.session.add(ticket_2)
        db.session.add(ticket_3)
        db.session.commit()
        return 'Success'

    return app
