"""
Definition of users and roles models.
"""
from flask.ext.security import UserMixin, RoleMixin

#from api.extensions import db
from api import db

# Relationship between users and roles
roles_users = db.Table(
    'roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))


class Role(db.Model, RoleMixin):
    """
    A role can be thought of as a group of users that may have
    elevated privileges. A user with the "admin" role would have
    access to the administration section of an app, a "manager"
    could view financial reports, etc.
    """
    __tablename__ = 'role'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class User(db.Model, UserMixin):
    """
    The user model stores login credential and optional audit
    information (create time, last login time, IP address, etc.)
    for all individuals who have access to your app.
    """
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship(
        'Role', secondary=roles_users,
        backref=db.backref('user', lazy='dynamic'))
