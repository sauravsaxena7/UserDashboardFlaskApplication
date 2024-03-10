from flask import Flask
from sqlalchemy import create_engine
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
import pandas as pd
from flask_cors import CORS, cross_origin
hostname="localhost"
username="root"
password="Lola@121"
port=3306
db_name="flask_tutorial"
#Flask is a class it is a collection of function
app=Flask(__name__)

CORS(app, support_credentials=True)

app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:Lola%40121@localhost:3306/flask_tutorial'

app.config['SECRET_KEY']='MYSECRETKEY'

db=SQLAlchemy(app)

#from User import Userss
class Userss(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200),nullable=False)
    password=db.Column(db.String(200),nullable=False)
    role=db.Column(db.String(200),nullable=False)
    email=db.Column(db.String(200),nullable=False,unique=True)
    phone=db.Column(db.String(20),nullable=False)
    date_added=db.Column(db.DateTime,default=datetime.utcnow)

    def __repr__(self):
        return '<Name %r>' % self.name



#add database


#engine = create_engine("mysql://root:Lola%40121@localhost:3306/flask_tutorial",echo=True)

#conn=engine.connect()

#DECORATOR
@app.route("/")
def welcome():
    return "HELLO WORLD"


# import controller.UserController as UserController;
# import controller.ProductController as ProductController;

# from controller import ProductController,UserController

from controller import *
# it is not going to be worked because we need to tell to python 
# virtual env, controller is a python package by creating __init__.py file

