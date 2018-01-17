#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Base(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime,
                           default=datetime.utcnow,
                           onupdate=datetime.utcnow)


class User(Base, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)


class Company(Base, UserMixin):
    __tablename__ = 'company'

    id = db.Column(db.Integer, primary_key=True)


class Job(Base):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)


class Resume(Base):
    __tablename__ = 'resume'

    id = db.Column(db.Integer, primary_key=True)
