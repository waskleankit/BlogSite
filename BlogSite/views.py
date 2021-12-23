from django.http import HttpResponse
from django.shortcuts import render
from BlogAdmin.models import *
from django.views.decorators.csrf import csrf_exempt

# from googlelogin import *
#
#
#
# # gmail login
# @app.route('/login')
# def login():
#     google = oauth.create_client('google')
#     redirect_uri = url_for('authorize', _external=True)
#     return google.authorize_redirect(redirect_uri)
# @app.route('/authorize')
# def authorize():
#     google = oauth.create_client('google')
#     token = google.authorize_access_token()
#     resp = google.get('userinfo')
# #   resp.raise_for_status()
#     user_info = resp.json()
#     # do something with the token and profile
#     session['email'] = user_info['email']
#     session['name'] = user_info['name']
#     return redirect('/')
# @app.route('/logout')
# def logout():
#     for key in list (session.keys()):
#         session.pop(key)
#     return redirect('/')







name = "name"
email = "email"
def home(request):
    # ROWS_PER_PAGE = 5
    # page = request.args.get('page', 1, type=int)
    # email = dict(session).get('email',None)
    # name = dict(session).get('name',None)
    # tag = request.form.get('sv')
    # searchcat = request.args.get("s_cat")
    # if searchcat != None:
    #     posts = Posts.query.filter_by(category_id = searchcat).paginate(page=page, per_page=ROWS_PER_PAGE)

    # elif tag != None:
    #     search = "%{}%".format(tag)
    #     posts = Posts.query.filter(or_(Posts.description.like(search),Posts.title.like(search))).paginate(page=page, per_page=ROWS_PER_PAGE)
    # else:
    #     posts = Posts.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    # cate = Category.query.all()
    # username = Users.query.all()
    # user = Users.query.all()
    # user1 = Users.query.filter_by(name=name).first()
    # if user1 == None:
    #     userinserting = Users(name,email)
    #     db.session.add(userinserting)
    #     db.session.commit()
    # return render_template('/index.html',email=email,posts=posts,category=cate,username=username,name=name)
    # posts = Posts.objects.first()
    # print(posts)
    # print(posts.user_id)
    # context = {'name': name, 'email': email,'posts':posts}
    context = {'name': name, 'email': email}
    return render(request,"index.html",context)


# def singlepost():
#     idvalue = request.values.get("b")
#     print(idvalue)
#     posts = Posts.query.filter_by(id = idvalue).first()
#     username = Users.query.all()
#     cate = Category.query.all()
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     return render_template('singlepost.html',email=email,posts=posts,category=cate,username=username,name=name)



def about(request):
    # email = dict(session).get('email', None)
    # name = dict(session).get('name', None)
    context = {'name': name, 'email': email}
    return render(request,"aboutus.html",context)


def dashboard(request):
    # email1 = dict(session).get('email', None)
    # name = dict(session).get('name', None)
    # user = Users.query.filter_by(email = email1).first()
    # userid = user.user_id
    # cate = Category.query.all()
    # tag = request.form.get('sv')
    # searchcat = request.args.get("s_cat")
    # print(searchcat)
    # if searchcat != None:
    #     posts = Posts.query.filter_by(category_id = searchcat,user_id = userid).all()
    # elif tag != None:
    #     search = "%{}%".format(tag)
    #     posts = Posts.query.filter(or_(Posts.description.like(search),Posts.title.like(search))).filter_by(user_id = userid).all()
    # else:
    #     posts = Posts.query.filter_by(user_id = userid).all()
    # return render_template('blogdashboard.html',email=email1,posts=posts,category=cate,name=name)
    context = {'name': name, 'email': email}
    return render(request, "blogdashboard.html", context)

def createblog(request):
    # email = dict(session).get('email', None)
    # name = dict(session).get('name', None)
    # user = Users.query.filter_by(email = email).first()
    # userid = user.user_id
    # countblogs = Posts.query.filter_by(user_id=userid).count()
    # if countblogs >= 5:
    #     pass
    #     return render_template('plans.html', email=email, name=name)
    # else:
    #     cate = Category.query.all()
    #     return render_template('createblog.html',email=email,category=cate,name=name)
    context = {'name': name, 'email': email}
    return render(request, "createblog.html", context)


# this post_user is for creating new  post
# @app.route('/post_user',methods=['POST'])
# def post_user():
#     title = request.form['name']
#     description = request.form['desc']
#     date_created = datetime.utcnow()
#     category_id = request.form['category']
#     email1 = dict(session).get('email', None)
#     user = Users.query.filter_by(email = email1).first()
#     user_id = user.user_id
#     post=Posts(title,description,date_created,category_id,user_id)
#     db.session.add(post)
#     db.session.commit()
#     cate = Category.query.all()
#     user = Users.query.filter_by(email = email1).first()
#     userid = user.user_id
#     posts = Posts.query.filter_by(user_id = userid).all()
#     name = dict(session).get('name', None)
#     return render_template('blogdashboard.html',email=email1,posts=posts,category=cate,name=name)
#
# @app.route("/edit",methods = ["GET","POST"])
# def edit():
#     idvalue = request.values.get("b")
#     posts = Posts.query.filter_by(id = idvalue).first()
#     cate = Category.query.all()
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     return render_template('editblog.html',email=email, post=posts,category=cate,name=name)
#
# @app.route('/update',methods=['POST'])
# def update():
#     title = request.form['name']
#     description = request.form['desc']
#     category = request.form['category']
#     date_created = datetime.utcnow().strftime('%B %d %Y ')
#     id = request.form['b']
#     posts = db.session.query(Posts).filter_by(id = request.form['b']).update({"title": title,"description":description,"date_created":date_created,"category_id":category})
#     db.session.commit()
#     email1 = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     user = Users.query.filter_by(email=email1).first()
#     userid = user.user_id
#     posts = Posts.query.filter_by(user_id=userid).all()
#     cate = Category.query.all()
#     return render_template("blogdashboard.html",email=email1,posts=posts,category=cate,name=name)
#
# @app.route('/deletepost',methods=['POST','GET'])
# def deletepost():
#     idvalue = request.form.get("a")
#     posts= db.session.query(Posts).filter_by(id=idvalue).first()
#     db.session.delete(posts)
#     db.session.commit()
#     return redirect('/dashboard')
#
# @app.route("/selectedplan",methods = ["GET","POST"])
# def selectedplan():
#     idvalue = request.form.get("plan")
#     posts = None
#     price = None
#     plan = None
#     if idvalue == "1":
#         posts = 20
#         price = 1
#         plan = "Basic"
#     elif idvalue == "2":
#         posts = 100
#         price = 5
#         plan = "Standard"
#     elif idvalue == "3":
#         posts = 1000
#         price = 10
#         plan = "Premium"
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     return render_template('selectedplan.html',email=email,name=name,planid=idvalue,post=posts,price=price,plan=plan)
#
# @app.route('/payment', methods=['POST'])
# def payment():
#     payment = paypalrestsdk.Payment({
#         "intent": "sale",
#         "payer": {
#             "payment_method": "paypal"},
#         "redirect_urls": {
#             "return_url": "http://localhost:3000/payment/execute",
#             "cancel_url": "http://localhost:3000/"},
#         "transactions": [{
#             "item_list": {
#                 "items": [{
#                     "name": "Blogposts",
#                     "sku": "20",
#                     "price": "1.00",
#                     "currency": "USD",
#                     "quantity": 1}]},
#             "amount": {
#                 "total": "1.00",
#                 "currency": "USD"},
#             "description": "This is the payment transaction description."}]})
#     if payment.create():
#         pass
#         # print('Payment success!')
#     else:
#         print(payment.error)
#     return jsonify({'paymentID' : payment.id})
#
# @app.route('/execute', methods=['POST'])
# def execute():
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     success = False
#     payment = paypalrestsdk.Payment.find(request.form['paymentID'])
#     if payment.execute({'payer_id' : request.form['payerID']}):
#         # print('Execute success!')
#         payer_id = request.form['payerID']
#         payment_id = request.form['paymentID']
#         user = Users.query.filter_by(email=email).first()
#         user_id = user.user_id
#         json_response = payment.success()
#         getresponses = payment
#         print(getresponses)
#         # amount = payment(id)
#         # print(amount)
#         success = True
#         paymenttable = Paymenttable(payment_id, payer_id, email, name,user_id,json_response)
#         db.session.add(paymenttable)
#         db.session.commit()
#     else:
#         print(payment.error)
#     return jsonify({'success' : success})
#
#
#
# @app.route('/thankyou',methods = ["GET","POST"])
# def thank():
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     amount = request.args.get('amount')
#
#
#     # print(amount)
#     # print(user_id)
#     # success = request.args.get('success')
#     # print(success)
#     # print(request.form['price'])
#     return render_template('thankyou.html',email=email,name=name)
