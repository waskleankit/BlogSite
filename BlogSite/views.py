from django.http import HttpResponse
from django.shortcuts import render
from BlogAdmin.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.db.models import Q








def home(request):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    if request.method == "POST":
        tag = request.POST['sv']
        posts = Posts.objects.filter(Q(description__contains=tag) | Q(title__contains=tag))
            # .paginate(page=page, per_page=ROWS_PER_PAGE)
    else:
        posts = Posts.objects.order_by('-date_created')
    #     posts = Posts.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    user1 = Users.objects.filter(name=name).first()
    try:
        if user1.name == None:
            latest_user = Users.objects.latest('user_id')
            user_id=latest_user.user_id + 1
            password = "kuchbhi"
            role = "BlogAdmin"
            print(name)
            print(email)
            name = "{}".format(name)
            email = "{}".format(email)
            userinserting = Users(user_id,role,name,email,password)
            userinserting.save();
            print(" new user saved")
            name = request.user
            email = request.user.email
    except:
        name = None
        email =None
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"index.html",context)


def home2(request,category_id):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    searchcat = category_id
    posts = Posts.objects.filter(category_id=searchcat)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"index.html",context)

from django.shortcuts import get_object_or_404
def post_detail(request,post_id):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    posts = get_object_or_404(Posts, pk=post_id)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,"singlepost.html",context)

def about(request):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    context = {'name': name, 'email': email}
    return render(request,"aboutus.html",context)


def dashboard(request):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    user = Users.objects.filter(email = email).first()
    userid = user.user_id
    # return render_template('blogdashboard.html',email=email1,posts=posts,category=cate,name=name)
    if request.method == "POST":
        if request.POST['sv'] != None:
           tag = request.POST['sv']
           posts = Posts.objects.filter( Q(Q(description__contains=tag) | Q(title__contains=tag)) & Q(user_id=userid))
           # posts = Posts.objects.filter(user_id=userid).all()
         # .paginate(page=page, per_page=ROWS_PER_PAGE)
    else:
         posts = Posts.objects.filter(user_id = userid)
             # order_by('-date_created')
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email ,'posts':posts, 'category': cate, 'username': username}
    return render(request, "blogdashboard.html", context)

def dashboard2(request,category_id):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    searchcat = category_id
    user = Users.objects.filter(email = email).first()
    userid = user.user_id
    posts = Posts.objects.filter(Q(category_id=searchcat) & Q(user_id=userid)).all
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email ,'posts':posts, 'category': cate, 'username': username}
    return render(request, "blogdashboard.html", context)

def createblog(request):
    # try excepet agr name email nhi chle to
    name = request.user
    email = request.user.email
    user = Users.objects.filter(email = email).first()
    userid = user.user_id
    countblogs = Posts.objects.filter(user_id=userid).count()
    if countblogs >= 5:
        context = {'name': name, 'email': email }
        return render(request,"plans.html", context)
    else:
        cate = Category.objects.all()
        context = {'name': name, 'email': email ,'category': cate}
        return render(request, "createblog.html", context)

# this post_user is for creating new  post
from django.utils import timezone
def post_user(request):
    title = request.POST['name']
    description = request.POST['desc']
    date_created = timezone.now()
    category_id = request.POST['category']
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    user = Users.objects.filter(email = email).first()
    userid = user.user_id
    latest_post = Posts.objects.latest('id')
    id=latest_post.id + 1
    post=Posts(id,title,description,date_created,category_id,userid)
    post.save();
    posts = Posts.objects.filter(user_id=userid)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email ,'posts':posts, 'category': cate, 'username': username}
    return render(request, "blogdashboard.html", context)


def edit(request,post_id):
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    posts = get_object_or_404(Posts, pk=post_id)
    cate = Category.objects.all()
    username = Users.objects.all()
    context = {'name': name, 'email': email,'posts':posts,'category' : cate,'username':username}
    return render(request,'editblog.html',context)


def update(request):
    id = request.POST.get('b')
    title = request.POST['name']
    description = request.POST['desc']
    category_id = request.POST.get('category')
    date_created = timezone.now()
#     email1 = dict(session).get('email', None)
    try:
        name = request.user
        email = request.user.email
    except:
        name = None
        email =None
    user = Users.objects.filter(email=email).first()
    userid = user.user_id
    # posts = Posts.objects.filter(user_id=userid).all()
#     cate = Category.query.all()
    post=Posts(id,title,description,date_created,category_id,userid)
    post.save();
    return redirect('/dashboard')


def deletepost(request):
    idvalue = request.POST["a"]
    posts = Posts.objects.filter(id=idvalue).delete()
    return redirect('/dashboard')


def selectedplan(request):
    idvalue = request.POST["plan"]
    posts = None
    price = None
    plan = None
    if idvalue == "1":
        posts = 20
        price = 1
        plan = "Basic"
    elif idvalue == "2":
        posts = 100
        price = 5
        plan = "Standard"
    elif idvalue == "3":
        posts = 1000
        price = 10
        plan = "Premium"
    # try excepet agr name email nhi chle to
    name = request.user
    email = request.user.email
    context = { 'email' : email , 'name' : name , 'planid' : idvalue , 'post' : posts , 'price' : price , 'plan' : plan}
    return render(request,'selectedplan.html',context)

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

# @app.route('/thankyou',methods = ["GET","POST"])
def thank(request):
    # try excepet agr name email nhi chle to
    name = request.user
    email = request.user.email
    transaction = request.POST['transactions']
    # amount = request.POST['amount']
    # print(amount)
    # print(user_id)
    # success = request.args.get('success')
    # print(success)
    # print(request.form['price'])
    context = {"email":email,"name":name}
    return render(request,'thankyou.html',context)
