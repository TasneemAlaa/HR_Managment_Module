from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from flask import Flask, jsonify


class CheckRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    checkin = db.Column(db.DateTime(timezone=True), default=func.now())
    checkout = db.Column(db.DateTime(timezone=True), default=func.now())
    late_arrival = db.Column(db.String(150))
    early_arrival = db.Column(db.String(150))
    overtime = db.Column(db.Integer)
    attendence_id = db.Column(db.Integer, db.ForeignKey('attendence.id'))

class Attendence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.Date(), default=func.now())
    ischeckedin = db.Column(db.Boolean, default=False)
    ischeckedout = db.Column(db.Boolean, default=False)
    checkin_date = db.Column(db.DateTime(timezone=True), default=func.now())
    checkout_date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True)
    first_name = db.Column(db.String(50))
    # role = db.Column(db.String(50))
    password = db.Column(db.String(50))
    isAdmin = db.Column(db.Boolean, default=False)
    attendence = db.relationship('Attendence')
    
    

