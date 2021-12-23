from django.db import models
from django.db.models import Model
# Create your models here.
from datetime import datetime
from django.utils import timezone

# class Customer(models.Model):
#     id = models.IntegerField(default=0,primary_key=True)
#     name = models.CharField(max_length=50)
#     gender = models.CharField(max_length=10)
#     account_type = models.CharField(max_length=10)
#     balance = models.IntegerField(default=0)
#     account_no = models.IntegerField(default=0)
#     pub_date = models.DateTimeField('date published',default=timezone.now())
#
#     def __str__(self):
#         return "{0} , {1} , AccNo-{2} , Balance-{3}".format(self.name,self.gender,self.account_no,self.balance)



class Posts(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    date_created = models.DateTimeField('date published',default=timezone.now())
    category_id = models.IntegerField(default=0)
    user_id = models.IntegerField(default=0)
    # def __init__(self,title,description,date_created,category_id,user_id):
    #     self.title = title
    #     self.description = description
    #     self.date_created = date_created
    #     self.category_id=category_id
    #     self.user_id=user_id

    def __str__(self):
        return "{0} , {1} , AccNo-{2} , Balance-{3}".format(self.user_id,self.title,self.description,self.date_created,self.category_id,self.user_id)


# class Category(db.Model):
#     category_id = db.Column(db.Integer,primary_key=True)
#     category_name = db.Column(db.String(200),unique= False)
#     create_date = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
#     update_date = db.Column(db.DateTime,unique= False, default=datetime.utcnow)
#     def __init__(self,category_name,create_date,update_date):
#         self.category_name = category_name
#         self.create_date = create_date
#         self.update_date = update_date
#     def __repr__(self):
#         return '<User %r>' % self.category_id
#
#
# class Users(db.Model):
#     user_id = db.Column(db.Integer,primary_key=True)
#     role = db.Column(db.String(200),unique= False)
#     name = db.Column(db.String(200),unique= False , nullable=False)
#     email = db.Column(db.String(200),unique= False)
#     password = db.Column(db.String(200),unique= False)
#
#     def __init__(self,name,email):
#         self.name = name
#         self.email = email
#
#     def __repr__(self):
#         return '%r' % self.user_id
#
#
#
#
# class Paymenttable(db.Model):
#     payment_id = db.Column(db.String,primary_key=True)
#     user_id = db.Column(db.Integer,unique= False)
#     payer_id = db.Column(db.String,unique= False)
#     amount = db.Column(db.Integer,unique= False)
#     email = db.Column(db.String, unique=False)
#     name = db.Column(db.String, unique=False)
#     json_response = db.Column(db.String(200), unique=False)
#     def __init__(self,payment_id, payer_id, email, name,user_id,json_response):
#         self.name = name
#         self.email = email
#         self.payment_id = payment_id
#         self.payer_id = payer_id
#         self.user_id = user_id
#         # self.amount = amount
#         self.json_response = json_response
#
#
#     def __repr__(self):
#         return '%r' % self.payment_id











#    user_id integer NOT NULL,
#     role character varying COLLATE pg_catalog."default" DEFAULT USER,
#     name character varying COLLATE pg_catalog."default",
#     email character varying COLLATE pg_catalog."default",
#     password character varying COLLATE pg_catalog."default",
#     CONSTRAINT "Users_pkey" PRIMARY KEY (user_id)
#     def __repr__(self):
#         return '<User %r>' % self.id