from django.http import HttpResponse
from django.shortcuts import render
from BlogAdmin.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.db.models import Q


name = "name"
email = "email"




def home(request):
    # ROWS_PER_PAGE = 5
    # page = request.args.get('page', 1, type=int)
    # email = dict(session).get('email',None)
    # name = dict(session).get('name',None)
    if request.method == "POST":
        tag = request.POST['sv']
        posts = Posts.objects.filter(Q(description__contains=tag) | Q(title__contains=tag))
            # .paginate(page=page, per_page=ROWS_PER_PAGE)
    else:
        posts = Posts.objects.order_by('-date_created')
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

    cate = Category.objects.all()
    username = Users.objects.all()
    # print(posts)
    # print(posts.user_id)
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    # context = {'name': name, 'email': email}
    return render(request,"index.html",context)

def home2(request,category_id):
    searchcat = category_id
    posts = Posts.objects.filter(category_id=searchcat)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"index.html",context)

from django.shortcuts import get_object_or_404
def post_detail(request,post_id):
#     idvalue = request.values.get("b")
#     print(idvalue)
#     posts = Posts.query.filter_by(id = idvalue).first()
#     username = Users.query.all()
#     cate = Category.query.all()
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     return render_template('singlepost.html',email=email,posts=posts,category=cate,username=username,name=name)
    posts = get_object_or_404(Posts, pk=post_id)
    cate = Category.objects.all()
    username = Users.objects.all()

    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"singlepost.html",context)

# from django.shortcuts import get_object_or_404
# def customer_detail(request,customer_id):
#     customer = get_object_or_404(Customer, pk=customer_id)
#     context = {'customer': customer,}
#     return render(request, 'CustomerApp/customer_details.html',context)


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
    if request.method == "POST":
        if request.POST['sv'] != None:
           tag = request.POST['sv']
           posts = Posts.objects.filter(Q(description__contains=tag) | Q(title__contains=tag))
         # .paginate(page=page, per_page=ROWS_PER_PAGE)
        else:
            posts = Posts.objects.filter(category_id=searchcat)
    else:
         posts = Posts.objects.order_by('-date_created')
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email ,'posts':posts, 'category': cate, 'username': username}
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
    cate = Category.objects.all()
    context = {'name': name, 'email': email ,'category': cate}
    return render(request, "createblog.html", context)

# this post_user is for creating new  post
from django.utils import timezone
def post_user(request):
    # name = request.POST['name']
    title = request.POST['name']
    description = request.POST['desc']
    date_created = timezone.now()
    category_id = request.POST['category']
#     email1 = dict(session).get('email', None)
#     user = Users.query.filter_by(email = email1).first()
#     user_id = user.user_id
    user_id = 2
    latest_post = Posts.objects.latest('id')
    id=latest_post.id + 1
    post=Posts(id,title,description,date_created,category_id,user_id)
    post.save();
    # user = Users.query.filter_by(email = email1).first()
#     userid = user.user_id
#     posts = Posts.query.filter_by(user_id = userid).all()
#     name = dict(session).get('name', None)
    posts = Posts.objects.all()
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email ,'posts':posts, 'category': cate, 'username': username}
    return render(request, "blogdashboard.html", context)


# @app.route("/edit",methods = ["GET","POST"])
def edit(request,post_id):
#     idvalue = request.values.get("b")
#     posts = Posts.query.filter_by(id = idvalue).first()
#     cate = Category.query.all()
#     email = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     return render_template('editblog.html',email=email, post=posts,category=cate,name=name)
    posts = get_object_or_404(Posts, pk=post_id)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,'editblog.html',context)
#
# @app.route('/update',methods=['POST'])
def update(request):
    id = request.POST.get('b')
    title = request.POST['name']
    description = request.POST['desc']
    category_id = request.POST.get('category')
    date_created = timezone.now()

#     id = request.form['b']
#     posts = db.session.query(Posts).filter_by(id = request.form['b']).update({"title": title,"description":description,"date_created":date_created,"category_id":category})
#     db.session.commit()
#     email1 = dict(session).get('email', None)
#     name = dict(session).get('name', None)
#     user = Users.query.filter_by(email=email1).first()
#     userid = user.user_id
    user_id = 2
#     posts = Posts.query.filter_by(user_id=userid).all()
#     cate = Category.query.all()
#     return render_template("blogdashboard.html",email=email1,posts=posts,category=cate,name=name)
    post=Posts(id,title,description,date_created,category_id,user_id)
    post.save();
    return redirect('/dashboard')
#
# @app.route('/deletepost',methods=['POST','GET'])
def deletepost(request):
    idvalue = request.POST["a"]
    posts = Posts.objects.filter(id=idvalue).delete()
    return redirect('/dashboard')
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
