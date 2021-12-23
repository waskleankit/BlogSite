from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


# @app.route('/admin',methods = ["GET","POST"])
def blogadmin(request):
    # context = {'latest_customer_list': latest_customer_list, }
    return render(request,'BlogAdmin/adminlogin.html')
    # return render(request,'BlogAdmin/adminlogin.html',context)


#
# @app.route('/adminpassword',methods = ["GET","POST"])
def adminpassword(request):
    name = request.POST["loginid"]
    password = request.POST["pd"]
    # blogadmin = db.session.query(Users).filter_by(role="admin").first()
    # username=blogadmin.role
    # userpassword=blogadmin.password
    username = "ankit"
    userpassword = "waskle"
    if name == username and password == userpassword:
        return render(request,'BlogAdmin/admindashboard.html')
    else:
        message="Enter correct userid and password"
        context = {'message': message}
        return render(request, 'BlogAdmin/adminlogin.html',context)
        # posts = Posts.query.all()
        # cate = Category.query.all()
    #     username = Users.query.all()
    #     return render_template('admindashboard.html', posts=posts, category=cate, username=username,blogadmin=blogadmin)
    # else:
    #     return render_template('adminlogin.html', message="Enter correct userid and password")

#
#
# @app.route('/adminboard', methods=["GET", "POST"])
def adminboard(request):
    return render(request,'BlogAdmin/admindashboard.html')
#     posts = Posts.query.all()
#     cate = Category.query.all()
#     username = Users.query.all()
#     blogadmin = db.session.query(Users).filter_by(role="admin").first()
#     return render_template('admindashboard.html',posts=posts,category=cate,username=username,blogadmin=blogadmin)

#
# @app.route('/deletebyadmin',methods=['POST','GET'])
# def deletebyadmin():
#     idvalue = request.form.get("a")
#     posts= db.session.query(Posts).filter_by(id=idvalue).first()
#     db.session.delete(posts)
#     db.session.commit()
#     posts = Posts.query.all()
#     cate = Category.query.all()
#     username = Users.query.all()
#     blogadmin = db.session.query(Users).filter_by(role="admin").first()
#     return render_template('admindashboard.html',posts=posts,category=cate,username=username,blogadmin=blogadmin)
#
#
#
# @app.route("/category")
def category(request):
#     cat=Category.query.all()
#     blogadmin = db.session.query(Users).filter_by(role="admin").first()
#     return render_template('/categories.html',category = cat,blogadmin=blogadmin)
    return render(request, 'BlogAdmin/categories.html')
#
# @app.route('/add_category',methods=['POST'])
# def add_category():
#     category_name = request.form['name']
#     create_date = datetime.utcnow()
#     # print(create_date)
#     update_date = datetime.utcnow()
#     cat=Category(category_name,create_date,update_date)
#     db.session.add(cat)
#     db.session.commit()
#     cate = Category.query.all()
#     blogadmin = db.session.query(Users).filter_by(role="admin").first()
#     return render_template('categories.html',category=cate,blogadmin=blogadmin)
#
# @app.route('/deletecategory',methods=['POST','GET'])
# def deletecategory():
#     idvalue = request.form.get("a")
#     print(idvalue)
#     category= db.session.query(Category).filter_by(category_id = idvalue).first()
#     db.session.delete(category)
#     db.session.commit()
#     return redirect('/category')
#
# @app.route('/editcategory',methods=['POST','GET'])
# def editcategory():
#     update_date = datetime.utcnow()
#     name=request.form['upda']
#     posts = db.session.query(Category).filter_by(category_id = request.form['b']).update({"category_name": name })
#     db.session.commit()
#     return redirect('/category')
#
