from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.postgresql import UUID
import uuid

db = SQLAlchemy()

class Ticket(db.Model):
    __tablename__ = 'ticket'

    id = db.Column(UUID(as_uuid=True), primary_key=True, nullable=False, server_default=str(uuid.uuid4()))
    name = db.Column(db.String(length=100), nullable=False)
    status = db.Column(db.Integer, nullable=False, server_default='0')
    url = db.Column(db.String(length=100), nullable=True)

    def __repr__(self):
        return f"Ticket: name={self.name}, status={self.status}, url={self.url}"

    #get string representation of status
    @property
    def get_status(self):
        all_statuses = {'0': 'Reported', '1': 'In Progress', '2': 'In Review', '3': 'Resolved'}
        return all_statuses[str(self.status)]
