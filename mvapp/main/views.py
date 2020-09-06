'''主蓝本中的路由和视图函数'''
from flask import render_template, redirect, request, url_for, flash,jsonify
from . import main
from flasky.mvapp.models import Grade


@main.route('/home',methods=['GET','POST'])
def home():
    if request.method=='GET':
        # page = int(request.args.get('page',1))
        # num = int(request.args.get('num',5))
        # paginate = Grade.query.order_by('id').paginate(page,num)
        grades=Grade.query.order_by('id').all()
        templist=[]
        for i in range(len(grades)):
            tempdict = {}
            tempdict.fromkeys(['id', 'name', 'create_time'])
            tempdict['id']=grades[i].id
            tempdict['name']=grades[i].name
            tempdict['create_time']=grades[i].create_time
            templist.append(tempdict)
        return render_template('home.html',grades=templist)
        #return jsonify({'grades':templist})

        # response = jsonify({'grades':templist})
        # response.status_code = 200
        # return response
    return render_template('home.html')