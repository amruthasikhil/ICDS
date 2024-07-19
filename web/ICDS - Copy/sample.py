from flask import Flask,render_template,request,session,jsonify
from connection import Db
import demjson
from dateutil.relativedelta import relativedelta
from dateutil import parser
import datetime

app = Flask(__name__)
app.secret_key='abc'



#..............Login portion...........................#
@app.route('/')
def login():
    return render_template("admin/loginboot.html")


@app.route('/loggs',methods=['post'])
def loggs():
    db=Db()
    name=request.form['name']
    password=request.form['pass']
    type=""
    lid=""
    qry=db.selectone("select * from login where user_name='"+name+"' and password='"+password+"'")
    if qry!=None:
        type=qry[3]
        lid=qry[0]
        session['lid']=lid
    if type=='admin':
        return render_template('admin/index.html')
    elif type == 'anganavadi':
        return render_template('anganavadi/anganavadiindex.html')
    elif type == 'hospital':
        return render_template("Hospital/hospital index.html")
    elif type == 'healthcenter':
        return render_template('healthcenter/health index.html')
    elif type == 'user':
        x=session['lid']
        qry="select angu_id from enroll_mother where lid='"+str(x)+"'"
        res=db.selectone(qry)
        print(res)
        session['angu_id']=res[0]
        qry1="select mother_id from enroll_mother where enroll_mother.lid='"+str(x)+"'"
        res=db.selectone(qry1)
        print(res)
        session['motherid']=res[0]
        return render_template('User/User_index.html')
    else:
        return render_template('admin/loginboot.html',l=1)

#-------------------------admin section------------------------------#
#-------------hospital----------#
@app.route('/hospital')
def hospital():
    return render_template("/admin/Hospital.html ")

@app.route('/addhos',methods=['post'])
def addhos():
    db=Db()
    name=request.form['txt_name']
    licno=request.form['txt_lno']
    ownername=request.form['txt_ownname']
    year=request.form['txt_yr']
    place=request.form['txt_place']
    post=request.form['txt_post']
    pin=request.form['txt_pin']
    email=request.form['em']
    phone=request.form['ph']
    dt=parser.parse(year).year
    print(dt)
    ds=datetime.datetime.now().year
    print(ds)
    x=ds>dt
    print(x)
    qr1=db.selectall("select Licence_no from hospital where Licence_no='"+licno+"'")
    qry2=db.selectall("select user_name from login where user_name='"+email+"'")
    if (len(qr1)==0 and len(qry2)==0 and ds > dt):
            qryy = "insert into login values(NULL,'" + email + "','" + phone + "','hospital')"
            res = db.nonreturn(qryy)
            qry = "insert into hospital values(NULL,'" + name + "','" + licno + "','" + ownername + "','" + year + "','" + place + "','" + post + "','" + pin + "','" + email + "','" + phone + "','" + str(res) + "')"
            res1 = db.nonreturn(qry)
            return render_template("/admin/Hospital.html ")
    else:
            return render_template("/admin/Hospital.html",m=1)




@app.route('/hospitalmanagement')
def hospitalmanagement():
    db=Db()
    qry=db.selectall("select * from hospital")
    print(qry)
    return render_template("/admin/view and manage hsptl.html",data22=qry)

@app.route('/hospitalselect',methods=['post'])
def hospitalselect():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from hospital where name like '%"+name+"%'")
    return render_template("/admin/view and manage hsptl.html",data22=qry)


@app.route('/hospitaledit/<did>')
def hospitaledit(did):
    db=Db()
    qry="select * from hospital where lid='"+did+"'"
    res=db.selectone(qry)
    session['id'] = did
    return render_template("/admin/update_hospital.html",data=res)

@app.route('/hospitalupdated',methods=['post'])
def hospitalupdateing():
    db = Db()
    y=session['id']
    name = request.form['name']
    print(name)
    licno = request.form['lno']
    ownername = request.form['ownname']
    year = request.form['yr']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    # email = request.form['em']
    phone = request.form['ph']
    dt = parser.parse(year).year
    print(dt)
    ds = datetime.datetime.now().year
    print(ds)
    x = ds > dt
    print(x)
    qry="update hospital set name='"+name+"',Licence_no='"+licno+"',owner_name='"+ownername+"',Year_ofestablishment='"+year+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+phone+"' where lid='"+str(y)+"'"
    res=db.nonreturn(qry)
    return hospitalmanagement()



@app.route('/hospitaldelete/<lid>')
def hospitaldelete(lid):
    db=Db()
    qry="delete from hospital where  lid='"+lid+"'"
    qryy="delete from login where  login_id='"+lid+"'"""
    res=db.nonreturn(qry)
    res1=db.nonreturn(qryy)
    return hospitalmanagement()


#------------------anganavadi------------------#
@app.route('/anganavadimanagement')
def anganavadimanagement():
    return render_template("/admin/anganavadi.html ")

@app.route('/addangu',methods=['post'])
def addangu():
    db=Db()
    name=request.form['txt_name']
    licno=request.form['txt_lno']
    place=request.form['txt_place']
    post=request.form['txt_post']
    pin=request.form['txt_pin']
    email=request.form['em']
    phone=request.form['ph']
    qr1 = db.selectall("select Licence_no from anganavadi where licence_no='" + licno + "'")
    qry2 = db.selectall("select user_name from login where user_name='" + email + "'")
    if (len(qr1) == 0 and len(qry2) == 0):
        qryy="insert into login values(NULL,'"+email+"','"+phone+"','anganavadi')"
        res = db.nonreturn(qryy)
        qry="insert into anganavadi values(NULL,'"+name+"','"+licno+"','"+place+"','"+phone+"','"+email+"','"+post+"','"+pin+"','"+str(res)+"')"
        res1=db.nonreturn(qry)
        return render_template("/admin/anganavadi.html ")
    else:
        return render_template("/admin/anganavadi.html",m=1)

@app.route('/viewanganavadimanagement')
def viewanganavadimanagement():
    db = Db()
    qry = db.selectall("select * from anganavadi")
    return render_template("/admin/view and manage anganavadi.html ",data22=qry)

@app.route('/viewselectanganavadi',methods=['post'])
def viewselectanganavadi():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from anganavadi where name like '%"+name+"%'")
    return render_template("/admin/view and manage anganavadi.html",data22=qry)

@app.route('/anganavadimanagement1/<lid>')
def anganavadimanagement1(lid):
    db=Db()
    qry=db.selectone("select * from anganavadi where login_id='"+lid+"'")
    did=qry[8]
    session['id']=did
    return render_template("/admin/update_anganavadi.html",data=qry)

@app.route('/anganavadiedit',methods=['post'])
def anganavadiedit():
    db=Db()
    y=session['id']
    name = request.form['name']
    licno = request.form['lno']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['ph']
    qry="update anganavadi set name='"+name+"',licence_no='"+licno+"',place='"+place+"',phone='"+phone+"',post='"+post+"',pin='"+pin+"' where login_id='"+str(y)+"'"
    res1=db.nonreturn(qry)
    return viewanganavadimanagement()

@app.route('/anganavadidelete/<lid>')
def anganavadidelete(lid):
    db = Db()
    qry = "delete from anganavadi where  login_id='" + lid + "'"
    qryy="delete from login where  login_id='"+lid+"'"""
    res = db.nonreturn(qry)
    res1=db.nonreturn(qryy)
    return viewanganavadimanagement()

#........................Health center Portion............................#

@app.route('/healthcentremanagement')
def healthcentremanagement():
    return render_template("/admin/healthcentre.html ")

@app.route('/addhealth',methods=['post'])
def addhealth():
    db=Db()
    name=request.form['txt_name']
    licno=request.form['txt_lno']
    place=request.form['txt_place']
    post=request.form['txt_post']
    pin=request.form['txt_pin']
    email=request.form['em']
    phone=request.form['ph']
    # dt = parser.parse(year).year
    # print(dt)
    # ds = datetime.datetime.now().year
    # print(ds)
    # x = ds > dt
    # print(x)
    qr1 = db.selectall("select Licence_no from healthcentre where licence_no='" + licno + "'")
    qry2 = db.selectall("select user_name from login where user_name='" + email + "'")
    if (len(qr1) == 0 and len(qry2) == 0 ):
        qryy="insert into login values(NULL,'"+email+"','"+phone+"','healthcenter')"
        res = db.nonreturn(qryy)
        qry="insert into healthcentre values(NULL,'"+str(res)+"','"+name+"','"+licno+"','"+place+"','"+post+"','"+pin+"','"+email+"','"+phone+"')"
        res1=db.nonreturn(qry)
        return healthcentremanagement()
    else:
        return render_template("/admin/healthcentre.html", m=1)


@app.route('/viewhealthcentremanagement')
def viewhealthcentremanagement():
    db = Db()
    qry = db.selectall("select * from healthcentre")
    return render_template("/admin/view and manage healthcentre.html ",data=qry)

@app.route('/healthcenterselectview',methods=['post'])
def healthcenterselectview():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from healthcentre where name like '%"+name+"%'")
    return render_template("/admin/view and manage healthcentre.html ",data=qry)

@app.route('/healthedit/<lid>')
def healthedit(lid):
    db = Db()
    qry = "select * from healthcentre where login_id='" + lid + "'"
    res = db.selectone(qry)
    did=res[1]
    session['id']=did
    return render_template("/admin/update_healthcentre.html",data=res)

@app.route('/healthupdates',methods=['post'])
def healthupdates():
     db=Db()
     y=session['id']
     name = request.form['name']
     licno = request.form['lno']
     place = request.form['place']
     post = request.form['post']
     pin = request.form['pin']
     phone = request.form['ph']
     qr1 = db.selectall("select Licence_no from healthcentre where licence_no='" + licno + "'")
     if (len(qr1) == 0):
         qry="update healthcentre set name='"+name+"',licence_no='"+licno+"',place='"+place+"',post='"+post+"',pin='"+pin+"',phone='"+phone+"'  where login_id='"+str(y)+"'"
         res=db.nonreturn(qry)
         return viewhealthcentremanagement()
     else:
         return '''<script>alert("error");window.location='/viewhealthcentremanagement'</script>'''


@app.route('/loggss')
def loggss():
    return render_template("admin/index.html")
@app.route('/healthdelete/<lid>')
def healthdelete(lid):
    db=Db()
    qry="delete from healthcentre where login_id='"+lid+"'"
    qryy="delete from login where  login_id='"+lid+"'"""
    res=db.nonreturn(qry)
    res1=db.nonreturn(qryy)
    return viewhealthcentremanagement()

#.................................................................#

#....................view vaccination report........................#
@app.route('/viewrepoert')
def viewreport():
    return render_template("admin/view and manage vaccintion entry.html")

@app.route('/viewvaccinationreport',methods=['post'])
def viewvaccinationreport():
    db=Db()
    # qry1=db.selectall("select * from vaccination")
    qry=db.jsonsel("select vaccination_entry.date,anganavadi.name as anguname,child_reg.name as cname,vaccination.name as vname from anganavadi,vaccination_entry,vaccination,child_reg where child_reg.child_reg_id=vaccination_entry.child_id and vaccination_entry.vaccination_id=vaccination.vaccination_id and anganavadi.angu_id=vaccination_entry.venuid")
    print(qry)
    return jsonify(qry)

@app.route('/viewreports',methods=['post'])
def viewreports():
    db=Db()
    fdate=request.form['f_date']
    tdate=request.form['t_date']
    qry=db.jsonsel("select vaccination_entry.date,vaccination_entry.venuetype,child_reg.name as cname,vaccination.name as vname from vaccination_entry,vaccination,child_reg where child_reg.child_reg_id=vaccination_entry.child_id and vaccination_entry.vaccination_id=vaccination.vaccination_id and date between '"+fdate+"' and '"+tdate+"'")
    print(qry)
    return jsonify(qry)

#...............................................................................#



#................................Vaccination Management.................#
@app.route('/vacview')
def vacview():
    db=Db()
    qry=db.selectall("select * from vaccination")
    return render_template("/admin/view and manage vaccintion entry.html ",data2=qry)

@app.route('/vaccimanagement')
def vaccimanagement():
    return render_template("/admin/vaccination add.html ")

@app.route('/addvac',methods=['post'])
def addvac():
    db=Db()
    name=request.form['txt_name']
    imp=request.form['txt_lmp']
    det=request.form['txt_det']
    qry="insert into vaccination values(NULL,'"+name+"','"+det+"','"+imp+"')"
    res1=db.nonreturn(qry)
    return render_template("/admin/vaccination add.html ")


@app.route('/viewvaccination')
def vaccinationmanagement():
    db = Db()
    qry = db.selectall("select * from vaccination")
    return render_template("/admin/view and manage vaccination.html ",data=qry)

@app.route('/selectviewvaccination',methods=['post'])
def selectviewvaccination():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from vaccination where name like '%"+name+"%'")
    return render_template("/admin/view and manage vaccination.html ",data=qry)

@app.route('/updatevaccination/<lid>')
def updatevaccination(lid):
    db=Db()
    qry=db.selectone("select * from vaccination where vaccination_id='"+lid+"'")
    did=qry[0]
    session['id']=did
    return render_template("/admin/update_vaccination.html",data=qry)

@app.route('/updatesvac',methods=['post'])
def updatesvac():
    db=Db()
    y=session['id']
    name=request.form['name']
    imp=request.form['imp']
    det=request.form['det']
    qry="update vaccination set name='"+name+"',details='"+det+"',importance='"+imp+"' where vaccination_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return vaccinationmanagement()

@app.route('/deletevaccination/<lid>')
def deletevaccination(lid):
    db=Db()
    qry="delete from vaccination where vaccination_id='"+lid+"'"
    res=db.nonreturn(qry)
    return vaccinationmanagement()

#........................Vaccination schedule management.........................#
@app.route('/snutri')
def snutri():
    db = Db()
    qry = db.selectall("select * from vaccination")
    return render_template('admin/Vaccination schedule.html',data=qry)






    # return '''<script>alert("kkk");window.location='/ss'</script>'''

@app.route('/scheduleadd',methods=['post'])
def scheduleadd():
    db=Db()
    vacci=request.form['select']
    date=request.form['date']
    dt = parser.parse(date)
    print(dt)
    ds = datetime.datetime.now()
    print(ds)
    x=ds<dt
    print(x)
    if x==True:
        qry="insert into vaccination_date values (null,'"+vacci+"','"+date+"')"
        res=db.nonreturn(qry)
        return '''<script>alert("Vaccination schedule added");window.location='/snutri'</script>'''
    else:
        return '''<script>alert("Please enter the future date");window.location='/snutri'</script>'''


@app.route('/svnutri')
def svnutri():
    db=Db()
    qry=db.selectall("select vaccination.vaccination_id,vaccination.name,vaccination.importance,vaccination.details,vaccination_date.date,vaccination_date.date_id from vaccination,vaccination_date where vaccination.vaccination_id=vaccination_date.vaccination_id")
    return render_template('admin/view and manage vaccintion schedule.html',data=qry)

@app.route('/updatesnutri/<lid>')
def updatesnutri(lid):
    db=Db()
    qry=db.selectone("select vaccination.vaccination_id,vaccination.name,vaccination_date.date from vaccination,vaccination_date where vaccination.vaccination_id=vaccination_date.vaccination_id and vaccination_date.date_id='"+lid+"'")
    qryy=db.selectall("select vaccination_id,name from vaccination")
    session['upid']=lid
    return render_template('admin/update_vaccinationshedule.html',data=qry, data1=qryy)

@app.route('/updating',methods=['post'])
def updating():
    db=Db()
    y=session['upid']
    vaccidate=request.form['date']
    name=request.form['select']
    qry="update vaccination_date set date='"+vaccidate+"',vaccination_id='"+name+"' where date_id='"+str(y)+"' "
    res=db.nonreturn(qry)
    return svnutri()

@app.route('/delvaccishedule/<lid>')
def delvaccishedule(lid):
    db=Db()
    qry="delete from vaccination_date where date_id='"+lid+"'"
    res=db.nonreturn(qry)
    return svnutri()

#...............................................................................................#


#...........................Calender Management....................................#
@app.route('/addcalender')
def addcalender():
    return render_template('admin/calender.html')

@app.route('/addvcalen',methods=['post'])
def addvcalen():
    db=Db()
    date=request.form['date']
    prgm=request.form['prgm']
    det=request.form['det']
    dt = parser.parse(date)
    print(dt)
    ds = datetime.datetime.now()
    print(ds)
    x = ds < dt
    print(x)
    if x==True:
        qry="insert into calendar values(NULL,'"+date+"','"+prgm+"','"+det+"')"
        res1=db.nonreturn(qry)
        return render_template('admin/calender.html')
    else:
        return '''<script>alert("Please enter the future date");window.location='/addcalender'</script>'''


@app.route('/viewcalender')
def viewcalender():
    db = Db()
    qry = db.selectall("select * from calendar")
    return render_template('admin/view and manage calenderl.html',data=qry)



@app.route('/viewbydate',methods=['post'])
def viewbydate():
    db=Db()
    fdate =request.form['date1']
    tdate =request.form['date2']
    qry=db.selectall("select * from calendar where date between '"+fdate+"' AND '"+tdate+"' ")
    return render_template('admin/view and manage calenderl.html',data=qry)



@app.route('/editcalender/<lid>')
def editcalender(lid):
    db=Db()
    qry=db.selectone("select * from calendar where calender_id='"+lid+"'")
    did=qry[0]
    session['id']=did
    return render_template('admin/calenderEDIT.html',data=qry)

@app.route('/updatecalender',methods=['post'])
def updatecalender():
    db=Db()
    y=session['id']
    prgm=request.form['pgm']
    date=request.form['date']
    details=request.form['det']
    qry="update calendar set program='"+prgm+"',details='"+details+"',date='"+date+"' where calender_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return viewcalender()


@app.route('/deletetcalender/<lid>')
def deletetcalender(lid):
    db=Db()
    qry="delete from calendar where calender_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewcalender()
#............................................................................................#


#.................................Nutrition Management.....................................#
@app.route('/addnutri')
def addnutri():
    return render_template('admin/Nutrition.html')

@app.route('/addnutrition',methods=['post'])
def addnutrition():
    db=Db()
    name=request.form['name']
    det=request.form['det']
    type=request.form['type']
    qry="insert into nutrition values(NULL,'"+name+"','"+det+"','"+type+"')"
    res1=db.nonreturn(qry)
    return addnutri()

@app.route('/viewnutri')
def viewnutri():
    db=Db()
    qry=db.selectall("select * from nutrition")
    return render_template('admin/view_and_manage_nutrition.html',data=qry)

@app.route('/updatenutri/<lid>')
def updatenutri(lid):
    db=Db()
    qry=db.selectone("select * from nutrition where nutrition_id='"+lid+"'")
    x=qry[0]
    session['pp']=x
    return  render_template('admin/update_nutrition.html',data=qry)

@app.route('/searching',methods=['post'])
def searching():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from nutrition where name like '%"+name+"%'")
    return render_template('/admin/view_and_manage_nutrition.html',data=qry)



@app.route('/uploading',methods=['post'])
def uploading():
    db=Db()
    y=session['pp']
    name=request.form['name']
    details=request.form['det']
    type=request.form['type']
    qry="update nutrition set name='"+name+"',details='"+details+"',type='"+type+"' where nutrition_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return viewnutri()



@app.route('/deletenutri/<lid>')
def deletenutri(lid):
    db=Db()
    qry="delete from nutrition where nutrition_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewnutri()


@app.route('/allocatenutritoang')
def allocatenutritoang():
    db = Db()
    qry = db.selectall("select * from nutrition")
    qry1=db.selectall("select * from anganavadi")
    return render_template('admin/nutrition stock.html',data1=qry,data2=qry1)

@app.route('/addallocation',methods=['post'])
def addallocation():
    db=Db()
    nutri=request.form['select']
    anganavadi=request.form['select2']
    stock=request.form['stock']
    qry="insert into nutrtion_stock values(NULL,'"+nutri+"','"+anganavadi+"','"+stock+"')"
    res=db.nonreturn(qry)
    return allocatenutritoang()

@app.route('/viewallocatenutritoang')
def viewallocatenutritoang():
    db=Db()
    qry=db.selectall("select nutrition.nutrition_id,nutrition.name as nname,anganavadi.name as aname,nutrtion_stock.stock,nutrtion_stock.stock_id from nutrition,nutrtion_stock,anganavadi where nutrtion_stock.nutrition_id=nutrition.nutrition_id and nutrtion_stock.angu_id=anganavadi.angu_id")
    # aid=qry[0]
    # session['hid']=aid
    return render_template('admin/View and manage nutrition stock.html',data=qry)

@app.route('/updateallocatenutritoang/<lid>')
def updateallocatenutritoang(lid):
    db=Db()
    qryy=db.selectall("select * from nutrition")
    qry2=db.selectall("select * from anganavadi")
    qry=db.selectone("select nutrition.nutrition_id,nutrition.name,anganavadi.angu_id,anganavadi.name,nutrtion_stock.stock,nutrtion_stock.stock_id from nutrtion_stock,nutrition,anganavadi where nutrtion_stock.nutrition_id=nutrition.nutrition_id and nutrtion_stock.angu_id=anganavadi.angu_id and nutrtion_stock.stock_id='"+lid+"'")
    session['ll']=lid
    return  render_template('admin/allocateedit.html',data=qry,data1=qryy,data2=qry2)

@app.route('/updatingdata',methods=['post'])
def updatingdata():
    db=Db()
    y=session['ll']
    nutri=request.form['nm']
    angu=request.form['an']
    stock=request.form['stock']
    qry="update nutrtion_stock set nutrition_id='"+nutri+"',angu_id='"+angu+"',stock='"+stock+"' where stock_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return  viewallocatenutritoang()

@app.route('/deleteallocatenutritoang/<lid>')
def deleteallocatenutritoang(lid):
    db=Db()
    qry="delete from nutrtion_stock where stock_id='"+lid+"'"
    res=db.nonreturn(qry)
    return  viewallocatenutritoang()

@app.route('/comp')
def comp():
    db=Db()
    qry=db.selectall("select * from complaint,anganavadi where complaint.login_id=anganavadi.login_id ")
    return render_template('admin/complaint.html',data=qry)


@app.route('/reply/<lid>')
def reply(lid):
    db=Db()

    qry=db.selectone("select * from complaint where complaint_id='"+lid+"'")
    session['v']=lid
    return render_template('admin/reply.html',data=qry)

@app.route('/seereply/<lid>')
def seereply(lid):
    db=Db()
    qry=db.selectone("select * from reply where complaint_id='"+lid+"'")
    return render_template('admin/seereply.html',data=qry)

@app.route('/pubviewvaccination',methods=['post'])
def choosing():
    db=Db()
    qry=db.jsonsel("select * from vaccination")
    return jsonify(status='ok',data=qry)

@app.route('/df')
def df():
    db=Db()
    qry=db.selectall("select distinct type from login,complaint where complaint.login_id=login.login_id")
    return render_template('admin/complaint.html',data=qry)




@app.route('/replysend',methods=['post'])
def replysend():
    db=Db()
    y=session['v']
    reply=request.form['nn']
    qry="insert into reply values(null,'"+str(y)+"','"+reply+"',current_date) "
    qryy="update complaint set status='seen' where complaint_id='"+str(y)+"'"
    res1=db.nonreturn(qryy)
    res=db.nonreturn(qry)
    return comp()


@app.route('/chat')
def chat():
    return render_template('admin/chat.html')
#-------------------------------------------------------------------------#

#-----------------aganavadi section------------------------------------------#
@app.route('/aganavadihome')
def userhome():
    return render_template('anganavadi/home.html')

@app.route('/enrollmother')
def enrollmother():
    return render_template("anganavadi/entroll mother.html")
@app.route('/addmother',methods=['post'])
def addmother():
    db=Db()
    y=session['lid']
    name=request.form['name']
    dob=request.form['dob']
    blg=request.form['select']
    height=request.form['height']
    weight=request.form['weight']
    aadhar=request.form['aadhar']
    job=request.form['job']
    husname=request.form['husname']
    husaadhar=request.form['husadhar']
    husjob=request.form['husjob']
    hname=request.form['hname']
    post=request.form['post']
    dist=request.form['dist']
    state=request.form['state']
    pin=request.form['pin']
    email=request.form['em']
    phone=request.form['ph']
    img=request.files['pic']
    img.save("D:\\kikik\\ICDS - Copy\\static\\pics\\"+img.filename)
    path='/static/pics/'+img.filename
    print(path)
    import random
    n = random.randint(00000000, 99999999)
    print(n)
    qryy="insert into login values(null,'"+email+"','"+str(n)+"','user')"
    res1=db.nonreturn(qryy)
    qry="insert into enroll_mother values(null,'"+name+"','"+dob+"','"+blg+"','"+height+"','"+weight+"','"+aadhar+"','"+job+"','"+husname+"','"+husaadhar+"','"+husjob+"','"+hname+"','"+post+"','"+pin+"','"+state+"','"+email+"','"+phone+"','"+path+"','"+dist+"','"+str(y)+"','"+str(res1)+"')"
    res=db.nonreturn(qry)
    return enrollmother()

@app.route('/viewenrollmothers')
def viewenrollmothers():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from enroll_mother where angu_id='"+str(y)+"'")
    return render_template("anganavadi/view and manage mother.html",data=qry)

@app.route('/viewenrollmother',methods=['post'])
def viewenrollmother():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from enroll_mother where name like'%"+name+"%'")
    return render_template("anganavadi/view and manage mother.html",data=qry)

@app.route('/update_enroll_mother/<lid>')
def update_enroll_mother(lid):
    db=Db()
    qry=db.selectone(" select * from enroll_mother where mother_id='"+lid+"'")
    session['rr']=lid
    return render_template("anganavadi/update_enroll_mother.html",data=qry)

@app.route('/updats',methods=['post'])
def updats():
    db=Db()
    m=session['rr']
    name = request.form['name']
    dob = request.form['dob']
    blg = request.form['select']
    height = request.form['hg']
    weight = request.form['wg']
    aadhar = request.form['aad']
    job = request.form['job']
    husname = request.form['husnm']
    husaadhar = request.form['husaad']
    husjob = request.form['husjob']
    hname = request.form['hname']
    post = request.form['post']
    dist = request.form['dist']
    state = request.form['state']
    pin = request.form['pin']
    email = request.form['em']
    phone = request.form['ph']

    if request.files is not None:
        print(request.files)
        print(type(request.files))
        if 'pic' in request.files:

            if request.files["pic"].filename!='':

                    photo = request.files['pic']
                    photo.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + photo.filename)
                    path = '/static/pics/' + photo.filename
                    qry = "update enroll_mother set name='" + name + "',dob='" + dob + "',bloodgroup='" + blg + "',height='" + height + "',weight='" + weight + "',aadhar_no='" + aadhar + "',occupation='" + job + "',hus_name='" + husname + "',hus_aadharno='" + husaadhar + "',hus_occupation='" + husjob + "',house='" + hname + "',postoffice='" + post + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',district='" + dist + "',photo='" + str(path) + "' where mother_id='"+str(m)+"'"
                    res=db.nonreturn(qry)
                    return  viewenrollmothers()
            else:
                qry = "update enroll_mother set name='" + name + "',dob='" + dob + "',bloodgroup='" + blg + "',height='" + height + "',weight='" + weight + "',aadhar_no='" + aadhar + "',occupation='" + job + "',hus_name='" + husname + "',hus_aadharno='" + husaadhar + "',hus_occupation='" + husjob + "',house='" + hname + "',postoffice='" + post + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',district='" + dist +  "' where mother_id='" + str(m) + "'"
                res = db.nonreturn(qry)
                return  viewenrollmothers()

        else:
            qry = "update enroll_mother set name='" + name + "',dob='" + dob + "',bloodgroup='" + blg + "',height='" + height + "',weight='" + weight + "',aadhar_no='" + aadhar + "',occupation='" + job + "',hus_name='" + husname + "',hus_aadharno='" + husaadhar + "',hus_occupation='" + husjob + "',house='" + hname + "',postoffice='" + post + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',district='" + dist + "' where mother_id='" + str(m) + "'"
            res = db.nonreturn(qry)
            return viewenrollmothers()


    else:
        qry = "update enroll_mother set name='" + name + "',dob='" + dob + "',bloodgroup='" + blg + "',height='" + height + "',weight='" + weight + "',aadhar_no='" + aadhar + "',occupation='" + job + "',hus_name='" + husname + "',hus_aadharno='" + husaadhar + "',hus_occupation='" + husjob + "',house='" + hname + "',postoffice='" + post + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',district='" + dist + "' where mother_id='" + str( m) + "'"
        res = db.nonreturn(qry)
        return  viewenrollmothers()


@app.route('/deletemother/<lid>')
def deletemother(lid):
    db=Db()
    qry=" delete from enroll_mother where mother_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewenrollmothers()






@app.route('/nutriallotomomandchild/<lid>')
def nutriallotomomandchild(lid):
    db=Db()
    qry=db.selectall("select nutrtion_entry.date,nutrtion_entry.quantity,nutrition.name from nutrtion_entry,nutrition where child_mother_id='"+lid+"' and status='mother'and nutrition.nutrition_id=nutrtion_entry.type")
    session['mm']=lid
    return render_template("anganavadi/nutrialloc.html",data=qry)

@app.route('/nutrialloc')
def nutrialloc():
    db=Db()
    qry=db.selectall("select * from nutrition")
    return render_template("anganavadi/nutriallocnew.html",data=qry)

@app.route('/nutritiongiven',methods=['post'])
def nutritiongiven():
    db=Db()
    x=session['mm']
    name=request.form['st']
    quantity=request.form['qt']
    qry="insert into nutrtion_entry values (null,'"+str(x)+"','"+quantity+"',current_date,'"+name+"','mother') "
    res=db.nonreturn(qry)
    return nutriallotomomandchild(lid=session['mm'])








@app.route('/enrollchild')
def enrollchild():
    return render_template("anganavadi/Enroll_child.html")

@app.route('/addenrollchild',methods=['post'])
def addenrollchild():
    db = Db()
    y = session['lid']
    x = session['vid']
    name = request.form['name']
    dob = request.form['dob']
    blg = request.form['select']
    gender = request.form['gender']
    height =request.form['ht']
    weight =request.form['wt']
    fname=request.form['fname']
    mname=request.form['mname']
    faadhar=request.form['fid']
    maadhr=request.form['mid']
    job=request.form['fjob']
    hname=request.form['hname']
    post = request.form['post']
    dist = request.form['dist']
    state = request.form['state']
    pin = request.form['pin']
    email = request.form['em']
    phone = request.form['ph']
    img = request.files['pic']
    img.save("E:\\ICDS\\static\\pics" + img.filename)
    path = '//static//pics' + img.filename
    print(path)
    qry="insert into enroll_child values(null,'"+str(y)+"','"+str(x)+"','" + name + "','" + dob + "','" + blg + "','" + height + "','" + weight + "','"+fname+"','"+mname+"','" + faadhar + "','"+maadhr+"','" + job + "', '"+ hname + "','" + post + "','" + pin + "','" + state + "','" + email + "','" + phone + "','" + path + "','" + dist + "')"
    res = db.nonreturn(qry)
    return render_template('anganavadi/home.html')


@app.route('/viewenrollchild')
def viewenrollchild():
    return render_template("anganavadi/enrolling child.html")


@app.route('/anguviewenrollchild')
def anguviewenrollchild():
    db = Db()
    y = session['lid']
    qry = db.selectall(" select * from child_reg inner join enroll_child on child_reg.child_reg_id=enroll_child.hospital_child_reg_id and angu_id='"+str(y)+"' ")
    return render_template("anganavadi/anguviewchild.html",data=qry)

@app.route('/selectchild',methods=['post'])
def selectchild():
    db=Db()
    name=request.form['name']
    y = session['lid']
    qry=db.selectall("select * from child_reg inner join enroll_child on child_reg.child_reg_id=enroll_child.hospital_child_reg_id and angu_id='"+str(y)+"' and child_reg.name like '%"+name+"%'")
    return render_template("anganavadi/anguviewchild.html",data=qry)




@app.route('/remarksaddchild/<lid>')
def remarksaddchild(lid):
    db=Db()
    qry=db.selectall("select enroll_child.child_id,checkup.date,checkup.details ,checkup.child_mother_id from enroll_child,checkup where checkup.child_mother_id=enroll_child.hospital_child_reg_id and checkup.child_mother_id='"+lid+"'")
    session['e']=lid
    return render_template('anganavadi/view_and_manage_checkup1.html',data=qry)


@app.route('/nutriallotochild/<lid>')
def nutriallotochild(lid):
    db=Db()
    qry=db.selectall("select * from nutrtion_entry where child_mother_id='"+lid+"'")
    session['mm']=lid
    return render_template("anganavadi/nutrialloc.html",data=qry)






@app.route('/nutriall/<lid>')
def nutriall(lid):
    db=Db()
    qry=db.selectall("select nutrtion_entry.date,nutrtion_entry.quantity,nutrition.name from nutrtion_entry,nutrition where child_mother_id='"+lid+"' and status='child'and nutrition.nutrition_id=nutrtion_entry.type")
    session['mm']=lid
    return render_template("anganavadi/nutrialloc1.html",data=qry)

@app.route('/nutriallocc')
def nutriallocc():
    db=Db()
    qry=db.selectall("select * from nutrition")
    return render_template("anganavadi/nutriallocnew1.html",data=qry)

@app.route('/nutritiongives',methods=['post'])
def nutritiongives():
    db=Db()
    x=session['mm']
    name=request.form['st']
    quantity=request.form['qt']
    qry="insert into nutrtion_entry values (null,'"+str(x)+"','"+quantity+"',current_date,'"+name+"','child') "
    res=db.nonreturn(qry)
    return nutriallocc()















@app.route('/enrollingchild')
def enrollingchild():
    return render_template("anganavadi/enrolling child.html")



@app.route('/child')
def child():
    db=Db()
    qry=db.selectall("select * from child_reg where child_reg.child_reg_id not in (select hospital_child_reg_id from enroll_child)")
    return render_template("anganavadi/enrolling child.html",data=qry)


@app.route('/childdet',methods=['post'])
def childdet():
   db=Db()
   name=request.form['name']
   qry=db.selectall("select * from child_reg where motheraadharno LIKE'%"+name+"%' and child_reg.child_reg_id ")
   # not in (select hospital_child_reg_id from enroll_child
   print("SELECT * FROM child_reg WHERE motheraadharno LIKE'%"+name+"%' ")
   # y = qry['0']
   # session['m1'] = y
   return render_template("anganavadi/enrolling child.html",data=qry)

@app.route('/enrollinggg/<lid>')
def enrollinggg(lid):
    session['mh']=lid
    return render_template("anganavadi/enrollinggggg.html")

@app.route('/substituting',methods=['post'])
def substituting():
    db=Db()
    x=session['mh']
    y=session['lid']
    img = request.files['pic']
    img.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + img.filename)
    path = '/static/pics/' + img.filename
    print(path)
    qry="insert into enroll_child values(null,'"+str(y)+"','"+str(x)+"','"+path+"',current_date )"
    res=db.nonreturn(qry)
    return child()


# @app.route('/routinecheackup')
# def routinecheackup():
#     return render_template('anganavadi/checkup.html')
#
@app.route('/routinecheackupview')
def routinecheackupview():
    return render_template('anganavadi/view_and_manage_checkup.html')

@app.route('/remarksadd/<lid>')
def remarksadd(lid):
    db=Db()
    qry=db.selectall("select enroll_mother.mother_id,checkup.date,checkup.details,enroll_mother.mother_id from enroll_mother,checkup where checkup.child_mother_id=enroll_mother.mother_id and enroll_mother.mother_id='"+lid+"'and checkup.status='mother'")
    session['e']=lid
    return render_template('anganavadi/view_and_manage_checkup.html',data=qry)

@app.route('/remarksaddtochil/<lid>')
def remarksaddtochil(lid):
    db=Db()
    qry=db.selectall("select enroll_child.child_id,checkup.date,checkup.details from enroll_child,checkup where checkup.child_mother_id='"+lid+"' and enroll_child.child_id and enroll_child.child_id=1 and checkup.status='child'")
    session['e']=lid
    return render_template('anganavadi/view_and_manage_checkup1.html',data=qry)

@app.route('/remarkspage')
def remarkspage():
    return render_template('anganavadi/remarksadd.html')

@app.route('/remarksadding',methods=['post'])
def remarksadding():
    db=Db()
    x=session['e']
    date=request.form['date']
    remarks=request.form['re']
    qry="insert into checkup values(null,'"+str(x)+"','"+date+"','"+remarks+"','mother')"
    res=db.nonreturn(qry)
    return remarksadd(lid=session['e'])


@app.route('/remarkspages')
def remarkspages():
    return render_template('anganavadi/remarksadd1.html')

@app.route('/remarksadds',methods=['post'])
def remarksadds():
    db=Db()
    x=session['e']
    date=request.form['date']
    remarks=request.form['re']
    qry="insert into checkup values(null,'"+str(x)+"','"+date+"','"+remarks+"','child')"
    res=db.nonreturn(qry)
    return render_template('anganavadi/remarksadd1.html',data=res)


# @app.route('/remarksdel/<lid>')
# def remarksdel(lid):
#     db=Db()
#     qry="delete from checkup where checkup_id=='"+lid+"'"
#     res=db.nonreturn(qry)
#     return render_template('anganavadi/view_and_manage_checkup.html')




@app.route('/replys')
def replys():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from complaint where login_id='"+str(y)+"'")
    qryy=db.selectall("select reply.reply from reply,complaint where complaint.login_id='"+str(y)+"'")
    # session['mn']=qry[0]
    # y=session['m']
    # qry2=db.selectall("select * from reply where complaint_id='"+st+"'")
    return render_template('/anganavadi/replys.html',data=qry,datas=qryy)


@app.route('/sreplys/<mm>')
def sreplys(mm):
    db=Db()
    qry=db.selectone("select reply from complaint,reply where complaint.complaint_id=reply.complaint_id and complaint.complaint_id='"+mm+"'")
    return render_template("anganavadi/seereplys.html",data=qry)



@app.route('/deleting/<lid>')
def deleting(lid):
    db=Db()
    qry="delete from complaint where complaint_id='"+lid+"'"
    res=db.nonreturn(qry)
    return replys()



@app.route('/addstu')
def addstu():
    return render_template('anganavadi/student.html')

@app.route('/addingg',methods=['post'])
def addingg():
    db=Db()
    y=session['lid']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    fname = request.form['fname']
    faadhar = request.form['fid']
    hname = request.form['hname']
    post = request.form['post']
    dist = request.form['dist']
    state = request.form['state']
    pin = request.form['pin']
    gurd = request.form['gurd']
    email = request.form['em']
    phone = request.form['ph']
    img = request.files['pic']
    img.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + img.filename)
    path = '/static/pics/' + img.filename
    print(path)
    qry="insert into student values(null,'"+name+"','"+dob+"','"+gender+"','"+fname+"','"+faadhar+"','"+hname+"','"+post+"','"+dist+"','"+state+"','"+pin+"','"+gurd+"','"+email+"','"+path+"','"+phone+"','"+str(y)+"')"
    res=db.nonreturn(qry)
    return render_template('anganavadi/student.html')


@app.route('/studview')
def studview():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from student where angu_id='"+str(y)+"'")
    return render_template("anganavadi/view_and_manage_student.html",data=qry)


@app.route('/searchstudent',methods=['POST'])
def searchstudent():
    db=Db()
    b=session['lid']
    name=request.form['name']
    qry=db.selectall("select * from student where name like'%"+name+"%'and angu_id='"+str(b)+"'")
    return render_template("anganavadi/view_and_manage_student.html",data=qry)

@app.route('/edittu/<lid>')
def edittu(lid):
    db=Db()
    qry=db.selectone("select * from student where stud_id='"+lid+"'")
    session['cc']=lid
    return render_template('anganavadi/update_student.html',data=qry)


@app.route('/upstudent',methods=['post'])
def upstudent():
    db=Db()
    m=session['cc']
    name=request.form['name']
    dob=request.form['dob']
    gender=request.form['gender']
    fname=request.form['fname']
    fid=request.form['fid']
    hname=request.form['hname']
    post=request.form['post']
    dist=request.form['dist']
    state=request.form['state']
    pin=request.form['pin']
    gurd=request.form['gurd']
    phone=request.form['ph']
    email=request.form['em']
    if request.files is not None:
        print(request.files)
        print(type(request.files))
        if 'pic' in request.files:

            if request.files["pic"].filename != '':

                photo = request.files['pic']
                photo.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + photo.filename)
                path = '/static/pics/' + photo.filename
                qry = "update student set name='"+name+"',dob='"+dob+"',gender='"+gender+"',fathername='"+fname+"',fatheraadharno='"+fid+"',house='"+hname+"',post='"+post+"',dist='"+dist+"',state='"+state+"',pin='"+pin+"',localgurdian='"+gurd+"',email='"+email+"',phone='"+phone+"',photo='" + str(path) + "' where stud_id='" + str(m) + "'"
                res=db.nonreturn(qry)
                return studview()
            else:
                qry = "update student set name='" + name + "',dob='" + dob + "',gender='" + gender + "',fathername='" + fname + "',fatheraadharno='" + fid + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',state='" + state + "',pin='" + pin + "',localgurdian='" + gurd + "',email='" + email + "',phone='" + phone + "' where  stud_id='" + str(m) + "'"
                res = db.nonreturn(qry)
                return studview()

        else:
            qry = "update student set name='" + name + "',dob='" + dob + "',gender='" + gender + "',fathername='" + fname + "',fatheraadharno='" + fid + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',state='" + state + "',pin='" + pin + "',localgurdian='" + gurd + "',email='" + email + "',phone='" + phone + "' where stud_id='" + str(m) + "'"
            res = db.nonreturn(qry)
            return studview()


    else:
        qry = "update student set name='" + name + "',dob='" + dob + "',gender='" + gender + "',fathername='" + fname + "',fatheraadharno='" + fid + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',state='" + state + "',pin='" + pin + "',localgurdian='" + gurd + "',email='" + email + "',phone='" + phone + "' where stud_id='" + str(m) + "'"
        res = db.nonreturn(qry)
        return studview()





@app.route('/delstu/<lid>')
def delstu(lid):
    db=Db()
    qry="delete from student where stud_id='"+lid+"'"
    res=db.nonreturn(qry)
    return studview()

@app.route('/sendnote')
def sendnote():
    return render_template('anganavadi/Notification.html')

@app.route('/sending',methods=['post'])
def sending():
    db=Db()
    y=session['lid']
    subject=request.form['sub']
    message=request.form['msg']
    qry=" insert into notification values(null,'"+subject+"','"+message+"','"+str(y)+"',current_date )"
    res=db.nonreturn(qry)
    return sendnote()

@app.route('/viewnote')
def viewnote():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from notification where angu_id='"+str(y)+"'")
    return render_template('anganavadi/view_and_manage_mother_notification.html',data=qry)

@app.route('/deletenote/<lid>')
def deletenote(lid):
    db=Db()
    qry="delete from notification where notification_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewnote()



@app.route('/complt')
def complt():
    return render_template('anganavadi/complaint.html')


@app.route('/angusendcomplaint',methods=['post'])
def angusendcomplaint():
    db=Db()
    y=session['lid']
    complaint=request.form['comp']
    qry="insert into complaint values(null,'"+complaint+"','"+str(y)+"',current_date,'pending')"
    res=db.nonreturn(qry)
    return complt()

#------------------------------------------------------------------------------#

#-----------------------Health center section------------------------------------------#

@app.route('/healthhome')
def healthhome():
    return render_template('healthcenter/home.html')

@app.route('/addstaff')
def addstaff():
    return render_template('healthcenter/staff.html')

@app.route('/staffadding',methods=['post'])
def staffadding():
    db = Db()
    y=session['lid']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    bgroup = request.form['bg']
    qual = request.form['qual']
    hname =request.form['hname']
    post =request.form['post']
    dist= request.form['dist']
    pin= request.form['pin']
    state=request.form['state']
    phone= request.form['ph']
    email=request.form['em']
    type=request.form['type']
    desgn=request.form['desgn']
    img = request.files['pic']
    img.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + img.filename)
    path = '/static/pics/' + img.filename
    print(path)
    dt=parser.parse(dob)
    ds=datetime.datetime.now()
    print(ds)
    intm=ds-dt
    print(intm)
    dif=relativedelta(ds,dt)
    dyr=dif.years
    if dyr>18:
        qry="insert into login values(null,'"+email+"','"+phone+"','staff')"
        res=db.nonreturn(qry)
        qryy="insert into staff values(null,'"+str(res)+"','"+str(y)+"','"+name+"','"+dob+"','"+gender+"','"+bgroup+"','"+hname+"','"+post+"','"+dist+"','"+pin+"','"+state+"','"+email+"','"+phone+"','"+qual+"','"+desgn+"','"+path+"','"+type+"')"
        res1=db.nonreturn(qryy)
        return addstaff()
    else:
        return render_template('healthcenter/staff.html',m=1)


@app.route('/viewstaff')
def viewstaff():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from staff where hosp_health_id='"+str(y)+"'")
    return render_template('healthcenter/view_and_manage_staff.html',data=qry)

@app.route('/selectsta',methods=['post'])
def selectsta():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from staff where name like'%"+name+"%'" )
    return render_template('healthcenter/view_and_manage_staff.html',data=qry)

@app.route('/upstaff/<lid>')
def upstaff(lid):
    db=Db()
    qry=db.selectone("SELECT * FROM staff WHERE staff_id='"+lid+"'")
    session['bv']=lid
    return render_template('healthcenter/update_staff.html',d=qry)

@app.route('/updatesss',methods=['post'])
def updatesss():
    db=Db()
    m=session['bv']
    name=request.form['nm']
    dob=request.form['dob']
    gender=request.form['gender']
    qual=request.form['qual']
    bgp=request.form['bg']
    hm=request.form['hm']
    pt=request.form['pt']
    dt=request.form['dt']
    pin=request.form['pin']
    state=request.form['st']
    email=request.form['em']
    phone=request.form['ph']
    dg=request.form['dg']
    type=request.form['type']

    if request.files is not None:
        print(request.files)
        if 'pic' in request.files:

            if request.files["pic"].filename!='':

                    photo = request.files['pic']
                    photo.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + photo.filename)
                    path = '/static/pics/' + photo.filename
                    qry="update staff  set name='"+name+"',dob='"+dob+"',gender='"+gender+"',bloodgroup='"+bgp+"',house='"+hm+"',post='"+pt+"',dist='"+dt+"',pin='"+pin+"',state='"+state+"',email='"+email+"',phone='"+phone+"',qualn='"+qual+"',designation='"+dg+"',type='"+type+"',photo='" + str( path) + "' where staff_id='" + str(m) + "'"
                    res = db.nonreturn(qry)
                    return viewstaff()
            else:
                    qry="update staff  set name='"+name+"',dob='"+dob+"',gender='"+gender+"',bloodgroup='"+bgp+"',house='"+hm+"',post='"+pt+"',dist='"+dt+"',pin='"+pin+"',state='"+state+"',email='"+email+"',phone='"+phone+"',qualn='"+qual+"',designation='"+dg+"',type='"+type+"' where staff_id='" + str(m) + "'"
                    res = db.nonreturn(qry)
                    return viewstaff()

        else:
                qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgp + "',house='" + hm + "',post='" + pt + "',dist='" + dt + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qual + "',designation='" + dg + "',type='" + type + "' where staff_id='" + str(m) + "'"
                res = db.nonreturn(qry)
                return viewstaff()


    else:
        qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgp + "',house='" + hm + "',post='" + pt + "',dist='" + dt + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qual + "',designation='" + dg + "',type='" + type + "' where staff_id='" + str(m) + "'"
        res = db.nonreturn(qry)
        return viewstaff()




@app.route('/delostaff/<lid>')
def delostaff(lid):
    db=Db()
    qry="delete from staff where staff_id='"+lid+"'"
    res=db.nonreturn(qry)
    return  viewstaff()


@app.route('/viewvacc')
def viewvacc():
    db=Db()
    qry=db.selectall("select name,details,importance,date from vaccination inner  join vaccination_date on vaccination.vaccination_id=vaccination_date.date_id")
    return render_template('healthcenter/view vaccination.html',data=qry)


@app.route('/viewvaccdate',methods=['post'])
def viewvaccdate():
    db=Db()
    fdate=request.form['fd']
    tdate=request.form['td']
    qry=db.selectall("select name,details,importance,date from vaccination inner  join vaccination_date on vaccination.vaccination_id=vaccination_date.date_id where vaccination_date.date  between'"+fdate+"' and '"+tdate+"'")
    return render_template('healthcenter/view vaccination.html',data=qry)




@app.route('/dutyalloc')
def dutyalloc():
    db=Db()
    x=session['lid']
    qry = db.selectall("select * from anganavadi")
    qry1 = db.selectall("select * from vaccination")
    qry2 = db.selectall("select * from vaccination_date")
    qry3 = db.selectall("select * from staff where hosp_health_id='"+str(x)+"'")
    return render_template('healthcenter/dutyalloc.html',n1=qry,n2=qry1,n3=qry2,n4=qry3)

@app.route('/setdutyalloc',methods=['post'])
def setdutyalloc():
    db=Db()
    y=session['lid']
    anganavadi=request.form['select']
    vacci=request.form['select2']
    vacci_date=request.form['select4']
    staff=request.form['select3']
    qry="insert into duty_allocation values(null,'"+staff+"','"+vacci_date+"','"+anganavadi+"','"+vacci+"','"+str(y)+"')"
    res=db.nonreturn(qry)
    return dutyalloc()






@app.route('/viewvaacin')
def viewvaacin():
    db=Db()
    qry=db.selectall("select vaccination.name,vaccination.details,vaccination.importance vaccination_date.date from vaccination,vaccination_date")
    return render_template()

@app.route('/dutyallocview')
def dutyallocview():
    db=Db()
    y=session['lid']
    qry=db.selectall("select anganavadi.name,vaccination.name,vaccination_date.date ,staff.name ,duty_allocation.allocation_id from duty_allocation,staff,anganavadi,vaccination,vaccination_date where duty_allocation.staff_id=staff.staff_id and duty_allocation.angu_id=anganavadi.angu_id and duty_allocation.vaccination_id=vaccination.vaccination_id and duty_allocation.vaccination_date_id=vaccination_date.date_id and duty_allocation.health_id='"+str(y)+"'  ")
    return render_template('healthcenter/dutyallocview.html',data=qry)


@app.route('/dutyallocviewing/<lid>')
def dutyallocviewing(lid):
    db=Db()
    qry="delete from duty_allocation where allocation_id ='"+lid+"'"
    res=db.nonreturn(qry)
    return dutyallocview()

@app.route('/searchdutyallocview',methods=['post'])
def searchdutyallocview():
    db = Db()
    y=session['lid']
    fdate = request.form['date1']
    tdate = request.form['date2']
    qry = db.selectall("select anganavadi.name,vaccination.name,vaccination_date.date ,staff.name ,duty_allocation.allocation_id from duty_allocation,staff,anganavadi,vaccination,vaccination_date where duty_allocation.staff_id=staff.staff_id and duty_allocation.angu_id=anganavadi.angu_id and duty_allocation.vaccination_id=vaccination.vaccination_id and duty_allocation.vaccination_date_id=vaccination_date.date_id and duty_allocation.health_id='"+str(y)+"' and date between '" + fdate + "' AND '" + tdate + "' ")
    return render_template('healthcenter/dutyallocview.html',data=qry)


@app.route('/dutyreporting')
def dutyreporting():
    db = Db()
    x = session['lid']
    qry=db.selectall("select * from staff where hosp_health_id='"+str(x)+"'")
    return render_template('healthcenter/dutyreport.html',data=qry)


@app.route('/dutyreport',methods=['post'])
def dutyreport():
    db=Db()
    qry=db.jsonsel("select vaccination.name as vname,vaccination_entry.date,staff.name as sname,child_reg.name as cname,anganavadi.name as anguname,child_reg.child_reg_id from anganavadi,child_reg,staff,vaccination,vaccination_entry where vaccination.vaccination_id=vaccination_entry.vaccination_id and vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.staff_id=staff.staff_id and anganavadi.angu_id=vaccination_entry.venuid")
    return jsonify(qry)


@app.route('/dutyreportmore/<lid>')
def dutyreportmore(lid):
    db=Db()
    qry=db.selectone("select child_reg.name,child_reg.dob,child_reg.bloodgroup,child_reg.gender,child_reg.mothername,anganavadi.name from anganavadi,child_reg,enroll_child where child_reg.hospital_id=enroll_child.hospital_child_reg_id  and enroll_child.angu_id=anganavadi.angu_id and child_reg.child_reg_id='"+lid+"'")
    return render_template('healthcenter/reportmore.html',data=qry)

@app.route('/dutyreportmoredate',methods=['post'])
def dutyreportmoredate():
    db=Db()
    d1= request.form['d1']
    print(d1)
    d2= request.form['d2']
    qry= db.jsonsel("select vaccination.name as vname,vaccination_entry.date,staff.name as sname,child_reg.name as cname,vaccination_entry.venuetype,child_reg.child_reg_id from child_reg,staff,vaccination,vaccination_entry where vaccination.vaccination_id=vaccination_entry.vaccination_id and vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.staff_id=staff.staff_id and date  between '"+d1+"' and '"+d2+"'")
    return jsonify(qry)


@app.route('/dutyreportbystaff',methods=['post'])
def dutyreportbystaff():
    db=Db()
    name=request.form['select']
    print(name)
    qry=db.jsonsel("select vaccination.name as vname,vaccination_entry.date,staff.name as sname,child_reg.name as cname ,anganavadi.name as anguname,child_reg.child_reg_id from anganavadi,child_reg,staff,vaccination,vaccination_entry where vaccination.vaccination_id=vaccination_entry.vaccination_id and vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.staff_id=staff.staff_id and anganavadi.angu_id=vaccination_entry.venuid and staff.staff_id='"+name+"'")

    print("select vaccination.name as vname,vaccination_entry.date,staff.name as sname,child_reg.name as cname ,anganavadi.name as anguname,child_reg.child_reg_id from child_reg,staff,vaccination,vaccination_entry where vaccination.vaccination_id=vaccination_entry.vaccination_id and vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.staff_id=staff.staff_id and staff.name like'"+name+"'")
    return jsonify(qry)

#------------------------------------------------------------------------#


#----------------------hospital section----------------------------------#
@app.route('/hoshome')
def hoshome():
    return render_template("Hospital/Hospitalprofileview.html")

@app.route('/adddept')
def adddept():
    return render_template("Hospital/adddept.html")

@app.route('/adding',methods=['post'])
def adding():
    db=Db()
    x=session['lid']
    dept=request.form['dept']
    qry="insert into department values(null,'"+dept+"','"+str(x)+"')"
    res=db.nonreturn(qry)
    return adddept()

@app.route('/selectingdept',methods=['post'])
def selectingdept():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from department where name like'%"+name+"%'")
    return render_template("hospital/viewdept.html",data=qry)


@app.route('/viewdept')
def viewdept():
    db=Db()
    x=session['lid']
    qry=db.selectall("select * from department where hospital_id='"+str(x)+"'")
    return render_template("hospital/viewdept.html",data=qry)

@app.route('/editdept/<lid>')
def editdept(lid):
    db=Db()
    qry=db.selectone(" select * from department where dept_id='"+lid+"'")
    did=qry[0]
    session['id']=did
    return render_template("hospital/updatedept.html",data=qry)

@app.route('/deldept/<lid>')
def updept(lid):
    db=Db()
    qry=" delete from department where dept_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewdept()

@app.route('/updates',methods=['post'])
def updates():
    db=Db()
    y=session['id']
    name=request.form['name']
    qry="update department set name='"+name+"'where dept_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return viewdept()



@app.route('/adstaffs')
def adstaff():
    return render_template("Hospital/staff.html")
@app.route('/adds',methods=['post'])
def adds():
    db=Db()
    y=session['lid']
    name=request.form['name']
    dob=request.form['dob']
    gender=request.form['gender']
    bgroup=request.form['select2']
    hname=request.form['hname']
    post=request.form['post']
    dist=request.form['dist']
    pin=request.form['pin']
    state=request.form['state']
    email=request.form['em']
    phone=request.form['ph']
    qlm=request.form['qq']
    type=request.form['select3']
    desgn=request.form['desgn']
    img=request.files['pic']
    img.save("D:\\kikik\\ICDS - Copy\\static\\pics" + img.filename)
    path = '/static/pics/' + img.filename
    dt = parser.parse(dob)
    ds = datetime.datetime.now()
    print(ds)
    intm = ds - dt
    print(intm)
    dif = relativedelta(ds, dt)
    dyr = dif.years
    if dyr > 18:
        qryy="insert into login values(null,'"+email+"','"+phone+"','staff')"
        res=db.nonreturn(qryy)
        qry="insert into staff values(null,'"+str(res)+"','"+str(y)+"','"+name+"','"+dob+"','"+gender+"','"+bgroup+"','"+hname+"','"+post+"','"+dist+"','"+pin+"','"+state+"','"+email+"','"+phone+"','"+qlm+"','"+desgn+"','"+path+"','"+type+"')"
        res1=db.nonreturn(qry)
        return adstaff()
    else:
        return render_template("Hospital/staff.html",m=1)


@app.route('/viewtaff')
def viewtaff():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from staff where hosp_health_id='"+str(y)+"'")
    return render_template("Hospital/viewstaff.html",data=qry)

@app.route('/searchstaff',methods=['post'])
def searchstaff():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from staff where name like'%"+name+"%'" )
    return render_template("Hospital/viewstaff.html",data=qry)


@app.route('/updstaff/<lid>')
def updstaff(lid):
    db=Db()
    qry=db.selectone("select * from staff where staff_id='"+lid+"'")
    session['x']=lid
    return render_template("Hospital/updatestaff.html",data=qry)

@app.route('/updatee',methods=['post'])
def updatee():
    db=Db()
    y=session['x']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    bgroup = request.form['bg']
    hname = request.form['hname']
    post = request.form['post']
    dist = request.form['dst']
    pin = request.form['pin']
    state = request.form['state']
    email = request.form['em']
    phone = request.form['ph']
    qlm = request.form['qul']
    type = request.form['type']
    desgn = request.form['desgn']

    if request.files is not None:

        if 'pic' in request.files:

            if request.files["pic"].filename != '':

                photo = request.files['pic']
                photo.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + photo.filename)
                path = '/static/pics/' + photo.filename
                qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgroup + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qlm + "',designation='" + desgn + "',type='" + type + "',photo='" + str(path) + "' where staff_id='" + str(y) + "'"
                print(qry)
                res = db.nonreturn(qry)
                return viewtaff()
            else:
                qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgroup + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qlm + "',designation='" + desgn + "',type='" + type + "' where staff_id='" + str(y) + "'"
                res = db.nonreturn(qry)
                return viewtaff()

        else:
            qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgroup + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qlm + "',designation='" + desgn + "',type='" + type + "'where staff_id='" + str(y) + "'"
            res = db.nonreturn(qry)
            return viewtaff()

    else:
        qry = "update staff  set name='" + name + "',dob='" + dob + "',gender='" + gender + "',bloodgroup='" + bgroup + "',house='" + hname + "',post='" + post + "',dist='" + dist + "',pin='" + pin + "',state='" + state + "',email='" + email + "',phone='" + phone + "',qualn='" + qlm + "',designation='" + desgn + "',type='" + type + "' where staff_id='" + str(y) + "'"
        res = db.nonreturn(qry)
        return viewtaff()


@app.route('/delestaff/<lid>')
def delestaff(lid):
    db=Db()
    qry="delete from staff where staff_id='"+lid+"'"
    res=db.nonreturn(qry)
    return viewtaff()


@app.route('/opschedule')
def opschedule():
    db=Db()
    x=session['lid']
    qry=db.selectall("select * from staff where hosp_health_id='"+str(x)+"'")
    return render_template("Hospital/OP.html",data=qry)

@app.route('/addop',methods=['post'])
def addop():
    db=Db()
    y=session['lid']
    staff=request.form['select']
    date=request.form['date']
    fromm=request.form['ftime']
    ttime=request.form['ttime']
    qry="insert into op values(null,'"+staff+"','"+date+"','"+fromm+"','"+ttime+"','"+str(y)+"')"
    res=db.nonreturn(qry)
    return opschedule()

@app.route('/select',methods=['post'])
def select():
    db=Db()
    y=session['lid']

    name=request.form['name']
    qry=db.selectall("Select op.op_id, staff.staff_id,staff.name,op.dates,op.from_time,op.to_time from op,staff where staff.staff_id=op.staff_id and op.hospital_id='"+str(y)+"'and staff.name like'%"+name+"%'")
    return render_template("Hospital/OPVIEW.html",data=qry)


@app.route('/viewop')
def viewop():
    db=Db()
    y=session['lid']
    qry=db.selectall("select op.op_id, staff.staff_id,staff.name,op.dates,op.from_time,op.to_time from op,staff where staff.staff_id=op.staff_id and op.hospital_id='"+str(y)+"'")
    return render_template("Hospital/OPVIEW.html",data=qry)

@app.route('/editop/<lid>')
def editop(lid):
    db=Db()
    x = session['lid']
    qryy = db.selectall("select * from staff where hosp_health_id='" + str(x) + "'")
    qry=db.selectone("select op.dates,op.from_time,op.to_time,staff.name,staff.staff_id,op.op_id from staff,op where op.staff_id=staff.staff_id and op.op_id='"+lid+"'")
    session['qq']=lid
    return render_template('Hospital/upop.html',data=qry,data1=qryy)


@app.route('/updateop',methods=['post'])
def updateop():
    db=Db()
    y=session['qq']
    staff=request.form['select1']
    date=request.form['date']
    ftime=request.form['frm']
    ttime=request.form['to']
    qry="update op set staff_id='"+staff+"',dates='"+date+"',from_time='"+ftime+"',to_time='"+ttime+"' where op_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return viewop()



@app.route('/delop/<lid>')
def delop(lid):
    db=Db()

    qry="delete from op where op_id='"+lid+"' "
    res=db.nonreturn(qry)
    return viewop()

@app.route('/childreg')
def childreg():
    return render_template("Hospital/childreg.html")

@app.route('/addchildreg',methods=['post'])
def addchildreg():
    db=Db()
    y=session['lid']
    name=request.form['name']
    dob=request.form['dob']
    gender=request.form['gender']
    bgroup=request.form['bg']
    weight=request.form['wt']
    fname=request.form['fn']
    mname=request.form['mn']
    fid=request.form['fid']
    mid=request.form['mid']
    fjob=request.form['job']
    hname=request.form['hname']
    post=request.form['post']
    dist=request.form['dist']
    state=request.form['state']
    pin=request.form['pin']
    email=request.form['em']
    phone=request.form['ph']
    qry="INSERT INTO child_reg values(null,'"+name+"','"+dob+"','"+bgroup+"','"+gender+"','"+weight+"','"+fname+"','"+mname+"','"+fid+"','"+mid+"','"+fjob+"','"+hname+"','"+post+"','"+dist+"','"+state+"','"+pin+"','"+email+"','"+phone+"','"+str(y)+"')"
    res=db.nonreturn(qry)
    return childreg()


@app.route('/chilldview')
def chilldview():
    db=Db()
    y=session['lid']
    qry=db.selectall("select * from child_reg where hospital_id='"+str(y)+"'")
    return render_template("Hospital/viewchild.html",data=qry)

@app.route('/childselect',methods=['post'])
def childselect():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from child_reg where name like'%"+name+"%'")
    return render_template("Hospital/viewchild.html",data=qry)

@app.route('/childedit/<lid>')
def childupdate(lid):
    db=Db()
    qry=db.selectone("select * from child_reg where child_reg_id='"+lid+"'")
    y=qry[0]
    session['rid']=y
    return render_template("Hospital/childupdate.html",data=qry)

@app.route('/childedit1/<lid>')
def childedit1(lid):
    db=Db()
    qry=db.selectone("select * from enroll_child where hospital_child_reg_id='"+lid+"'")
    session['rid']=lid
    return render_template("anganavadi/childupdate.html",data=qry)

@app.route('/updateschilds',methods=['post'])
def updateschilds():
    db=Db()
    y=session['rid']
    photo = request.files['pic']
    photo.save("D:\\kikik\\ICDS - Copy\\static\\pics\\" + photo.filename)
    path = '/static/pics/' + photo.filename
    qry = "update enroll_child set photo='"+str(path)+"' where hospital_child_reg_id='"+str(y)+"'"
    res = db.nonreturn(qry)
    return anguviewenrollchild()


@app.route('/updateschild',methods=['post'])
def updateschild():
    db=Db()
    y=session['rid']
    name = request.form['name']
    dob = request.form['dob']
    gender = request.form['gender']
    bgroup = request.form['bg']
    weight = request.form['wt']
    fname = request.form['fn']
    mname = request.form['mn']
    fid = request.form['fid']
    mid = request.form['mid']
    fjob = request.form['job']
    hname = request.form['hname']
    post = request.form['post']
    dist = request.form['dist']
    state = request.form['state']
    pin = request.form['pin']
    email = request.form['em']
    phone = request.form['ph']
    qry="update child_reg set name='"+name+"',dob='"+dob+"',bloodgroup='"+bgroup+"',gender='"+gender+"',weight='"+weight+"',fathername='"+fname+"',mothername='"+mname+"',motheraadharno='"+mid+"',fatheraadharno='"+fid+"',fatherjob='"+fjob+"',house='"+hname+"',post='"+post+"',dist='"+dist+"',state='"+state+"',pin='"+pin+"',email='"+email+"',phone='"+phone+"' where child_reg_id='"+str(y)+"'"
    res=db.nonreturn(qry)
    return chilldview()


@app.route('/selectstudent',methods=['post'])
def selectstudent():
    db=Db()
    name=request.form['name']
    qry=db.selectall("select * from student where name like'"+name+"' ")


@app.route('/deletechild/<lid>')
def deletechild(lid):
    db=Db()
    qry="delete from child_reg where child_reg_id='"+lid+"'"
    res=db.nonreturn(qry)
    return chilldview()




#.......................................................................................................................................#

@app.route('/userprofile',methods=['post'])
def userprofile():
    db=Db()
    lid=request.form["userid"]
    qry=db.selectone("select * from enroll_mother where lid='"+lid+"'")
    if qry!=None:
        return jsonify(status='ok',mname=qry[1],dob=qry[2],bloodgroup=qry[3],height=qry[4],weight=qry[5],aadhar_no=qry[6],occupation=qry[7],hus_name=qry[8],hus_aadharno=qry[9],hus_occupation=qry[10],house=qry[11],postoffice=qry[12],pin=qry[13],state=qry[14],email=qry[15],phone=qry[16],photo=qry[17],district=qry[18])
    else:
        return 'error'


@app.route('/userlogin',methods=['post'])
def userlogin():
    db=Db()
    name=request.form['name']
    password=request.form['password']
    qry="select * from login where user_name='"+name+"' and password='"+password+"'"
    res=db.selectone(qry)
    if res!=None:
        type=res[3]
        if type=='user':
            qryy=db.selectone("select angu_id from enroll_mother where enroll_mother.lid='"+str(res[0])+"'")
            qr1=db.selectone("select aadhar_no from enroll_mother where enroll_mother.lid='"+str(res[0])+"'")
            qr2=db.selectone("select mother_id from enroll_mother where enroll_mother.lid='"+str(res[0])+"'")
            qr=db.jsonsel("select child_reg_id from child_reg,enroll_mother where enroll_mother.lid='"+str(res[0])+"'and child_reg.motheraadharno=enroll_mother.aadhar_no")
            qry4=db.jsonsel("select child_reg_id from child_reg,enroll_mother where enroll_mother.aadhar_no=child_reg.motheraadharno and enroll_mother.lid='"+str(res[0])+"'")
            qry5=db.selectone("select child_reg.* from child_reg,enroll_mother where enroll_mother.aadhar_no=child_reg.motheraadharno and enroll_mother.lid='"+str(res[0])+"'")
            print(qryy)
            print(qr2)
            print(qr)
            return jsonify(status='ok',type=res[3],loginid=res[0],mksid=qr[0],angu_id=qryy[0],ad_no=qr1[0],mid=qr2[0],childid=qry4[0],child_id=qr[0],childob=qry5[2])
        else:
            qry2=db.selectone("select staff.staff_id from staff,login where staff.login_id='"+str(res[0])+"' and staff.login_id=login.login_id")
            print(qry2)
            return jsonify(status='ok', type=res[3], loginid=res[0],sid=qry2[0])
    else:
        return 'error'

@app.route('/userviewcalender',methods=['post'])
def userviewcalender():
    db=Db()
    qry=db.jsonsel("select * from calendar")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/userviewnotification',methods=['post'])
def userviewnotification():
    db=Db()
    anguid=request.form['angu_id']
    print("hi")
    qry=db.jsonsel("SELECT notification_id,subject,massage,angu_id, DATE_FORMAT(date, '%d/%m/%Y') as date from notification where angu_id='"+anguid+"' and date>now()")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/pubviewnotification',methods=['post'])
def pubviewnotification():
    db=Db()
    qry=db.jsonsel("select * from notification where date>now()")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'



@app.route('/in_message2', methods=['POST'])
def message():
    db=Db()
    fr_id = request.form["fid"]
    to_id = request.form["toid"]
    message = request.form["msg"]
    query7 = "insert into chat(userid,recid,message,date,time) values ('" + fr_id + "' ,'" + to_id + "','" + message + "',curdate(),curtime())"
    print(query7);
    res=db.nonreturn(query7)
    return jsonify(status='send')


@app.route('/view_message2', methods=['POST'])
def msg():
    db=Db()
    fid = request.form["fid"]
    toid = request.form["toid"]
    lmid = request.form['lastmsgid'];
    query="select userid,message,date,chat_id from chat where chat_id>'"+lmid+"' AND ((recid='"+toid+"' and  userid='"+fid+"') or (recid='"+fid+"' and userid='"+toid+"')  )  order by chat_id asc"
    res=db.jsonsel(query)
    return jsonify(status='ok', res1=res)








@app.route("/view_mothers")
def view_mothers():
    d=Db()
    qry="select * from enroll_mother"
    res=d.selectall(qry)
    return render_template("admin/View mother.html",data=res)


@app.route("/admin_chat/<mid>")
def admin_chat(mid):
    session['toid']=mid
    return render_template("admin/chat.html",momid=mid)




@app.route("/emp_chat_chk",methods=['post'])        # refresh messages chatlist
def emp_chat_chk():
    # uid=session["toid"]
    uid = request.form['to_id']
    qry = "select userid,date,message from chat where (userid='1' and recid='" + uid + "') or ((userid='" + uid + "' and recid='1')) order by chat_id desc"
    c = Db()
    res = c.jsonsel(qry)
    # print((res))
    return jsonify(res)


@app.route("/emp_chat_post",methods=['POST'])
def emp_chat_post():
    try:
        idd=request.form['hid']
        session['mid']=idd
        ta=request.form["ta"]
        qry="insert into chat(userid,recid,message,date,time)values('1','"+idd+"','"+ta+"',curdate(),curtime())"
        d=Db()
        res = d.nonreturn(qry)
        return render_template("admin/chat.html",momid=session['mid'])
    except Exception as e:
        print(str(e))












@app.route('/staffviewnotification',methods=['post'])
def staffviewnotification():
    db=Db()
    qry = db.jsonsel("select * from notification")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'

@app.route('/userchangepswd',methods=['post'])
def userchangepswd():
    db=Db()
    userid=request.form['userid']
    oldpass=request.form['oldpassword']
    newpassword=request.form['newpassword']
    qry=db.selectone("select password from login where login_id='"+userid+"'")
    if qry!=None:
        qry2="update login set password='"+newpassword+"' where login_id='"+userid+"'"
        res=db.nonreturn(qry2)
    return jsonify(status='ok',data=qry)


@app.route('/userviewtheirchild',methods=['post'])
def userviewtheirchild():
    db=Db()
    adhar=request.form['ad_no']
    mkid=request.form['mksid']
    print(mkid)
    print(adhar)
    qry=db.jsonsel("select child_reg.*,enroll_child.photo from child_reg,enroll_mother,enroll_child where enroll_mother.aadhar_no='"+adhar+"' and enroll_mother.aadhar_no=child_reg.motheraadharno and child_reg.child_reg_id=enroll_child.hospital_child_reg_id")
    if len(qry)!=0:
        # qryy = db.jsonsel("select child_reg.child_reg_id from child_reg,enroll_mother,enroll_child where enroll_mother.aadhar_no='"+adhar+"' and enroll_mother.aadhar_no=child_reg.motheraadharno and child_reg.child_reg_id=enroll_child.hospital_child_reg_id and child_reg.child_reg_id='"+mkid+"'")
        return jsonify(status='ok',data=qry)
        print(qryy)
    else:
        return 'error'


@app.route('/childprofile',methods=['post'])
def childprofile():
    db=Db()
    did=request.form['did']
    qry=db.selectone("select * from child_reg,enroll_child where enroll_child.child_id=child_reg.child_reg_id and child_reg.child_reg_id='"+did+"'")
    print(qry)
    if qry!=None:
        return jsonify(status='ok',data=qry,name=qry[1],dob=qry[2],photo=qry[22])
    else:
        return 'error'




@app.route('/childnurtition',methods=['post'])
def childnurtition():
    db=Db()
    did=request.form['did']
    qry=db.jsonsel("select nutrtion_entry.date,nutrtion_entry.quantity,nutrition.name from nutrtion_entry,nutrition where child_mother_id='"+did+"' and status='child' and nutrition.nutrition_id=nutrtion_entry.type")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/childcheackup',methods=['post'])
def childcheackup():
    db=Db()
    did=request.form['did']
    qry=db.jsonsel("select * from checkup where child_mother_id='"+did+"' and status='child'")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/usernutrittion',methods=['post'])
def usernutrittion():
    db=Db()
    mid=request.form['mid']
    qry=db.jsonsel("select nutrtion_entry.date,nutrtion_entry.quantity,nutrition.name from nutrtion_entry,nutrition where nutrtion_entry.child_mother_id='"+mid+"' and status='mother' and nutrition.nutrition_id=nutrtion_entry.type")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/usercheckup',methods=['post'])
def usercheckup():
    db=Db()
    mid=request.form['mid']
    qry=db.jsonsel("select * from checkup where child_mother_id='"+mid+"' and status='mother'")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/viewvaccination',methods=['post'])
def viewvaccination():
    db=Db()
    qry=db.jsonsel("select vaccination.name,vaccination.details,vaccination.importance,vaccination_date.date from vaccination,vaccination_date  where vaccination.vaccination_id=vaccination_date.vaccination_id")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/viewdoctor',methods=['post'])
def viewdoctor():
    db=Db()
    qry=db.jsonsel("select * from staff where type='doctor'")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/viewdoctorop',methods=['post'])
def viewdoctorop():
    db=Db()
    did=request.form['did']
    qry=db.jsonsel("select staff.name,op.dates,op.from_time,op.to_time from op,staff where staff.staff_id=op.staff_id and staff.type='doctor' and staff.staff_id = '"+did+"'")
    print(qry)
    if len(qry)!=0:

        return jsonify(status='ok',data=qry)
    else:
        return 'error'

@app.route('/staffprofile',methods=['post'])
def staffprofile():
    db=Db()
    lid=request.form["userid"]
    qry=db.selectone("select * from staff where login_id='"+lid+"'")
    if qry!=0:
        return jsonify(status='ok',name=qry[3],email=qry[12],phone=qry[13],photo=qry[16])
    else:
        return 'error'



@app.route('/searchiiistaff',methods=['post'])
def searchiiistaff():
    db=Db()
    names=request.form['name']
    qry=db.jsonsel("select * from staff where type='doctor' and name  like '%"+names+"%'")
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'



@app.route('/staffduty',methods=['post'])
def staffduty():
    db=Db()
    sid=request.form['sid']
    qry=db.jsonsel("select vaccination.vaccination_id,anganavadi.angu_id,vaccination_date.date,vaccination.name as vname,anganavadi.name as aname from duty_allocation,anganavadi,vaccination,vaccination_date where duty_allocation.staff_id='"+sid+"' and duty_allocation.vaccination_date_id=vaccination_date.date_id and duty_allocation.angu_id=anganavadi.angu_id and vaccination.vaccination_id=duty_allocation.vaccination_id")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry,vaccination_id=qry[0],angu_id=qry[1])
    else:
        return 'error'






@app.route('/staffaddnutritin',methods=['post'])
def staffaddnutritin():
    db=Db()
    vaccination_id = request.form['vaccination_id']
    angu_id = request.form['angu_id']
    sid = request.form['sid']
    momid = request.form['momid']
    qry="insert into vaccination_entry (vaccination_id,child_id,staff_id,date) values('"+vaccination_id+"','"+momid+"','"+sid+"',curdate())"
    res=db.nonreturn(qry)
    return jsonify(status='ok')



@app.route('/mothervaccin',methods=['post'])
def mothervaccin():
    db=Db()
    mid=request.form['mid']
    qry=db.jsonsel("select vaccination.name as vname,vaccination_entry.date,anganavadi.name as aname from anganavadi,vaccination,vaccination_entry where vaccination_entry.vaccination_id=vaccination.vaccination_id and vaccination_entry.venuid=anganavadi.angu_id and vaccination_entry.type='mother' and vaccination_entry.child_id='"+mid+"'")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'



    # child_id = request.form['child_id']




@app.route('/childvacc',methods=['post'])
def childvacc():
    db=Db()
    did=request.form['did']
    qry=db.jsonsel("select vaccination.name as vname,vaccination_entry.date,anganavadi.name as aname from anganavadi,vaccination,vaccination_entry where vaccination_entry.vaccination_id=vaccination.vaccination_id and vaccination_entry.venuid=anganavadi.angu_id and vaccination_entry.type='child' and vaccination_entry.child_id='"+did+"'")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'


@app.route('/staffviewchild',methods=['post'])
def staffviewchild():
    db=Db()
    # lid=request.form["userid"]
    qry=db.selectone("select child_reg.name,child_reg.mothername,child_reg.post,child_reg.phone from child_reg,vaccination_entry where vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.entry_id=1")
    if qry!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'




@app.route('/childdetails',methods=['post'])
def childdetails():
    db=Db()
    did=request.form['did']
    qry=db.selectone("select child_reg.*,enroll_child.photo from child_reg,vaccination_entry,enroll_child where vaccination_entry.child_id=child_reg.child_reg_id and enroll_child.hospital_child_reg_id=child_reg.child_reg_id and vaccination_entry.entry_id=1")
    print(qry)
    if len(qry)!=0:
        return jsonify(status='ok',data=qry)
    else:
        return 'error'

@app.route('/childdetailssss', methods=['post'])
def childdetailssss():
    db = Db()
    qry = db.jsonsel("select * from enroll_mother")
    print(qry)
    if len(qry) != 0:
        return jsonify(status='ok', data=qry)
    else:
        return 'error'




@app.route('/motheralert', methods=['post'])
def motheralert():
    db = Db()
    childob=request.form['childob']
    dt = parser.parse(childob).year
    print(dt)
    ds = datetime.datetime.now().year
    print(ds)
    x = ds - dt
    print(x)
    if x==3:
        return jsonify(status='ok')
    else:
        return jsonify(status='no')




@app.route('/childserch', methods=['post'])
def childserch():
        db = Db()
        names = request.form['name']
        qry = db.jsonsel("select * from enroll_mother where aadhar_no LIKE '%" + names + "%'")
        print(qry)
        if len(qry) != 0:
            return jsonify(status='ok', data=qry)
        else:
            return 'error'

@app.route('/pubviewanganavadi', methods=['post'])
def pubviewanganavadi():
    db = Db()
    qry = db.jsonsel("select * from anganavadi")
    return jsonify(status='ok', data=qry)


@app.route('/pubviewhealthcenter', methods=['post'])
def pubviewhealthcenter():
    db = Db()
    qry = db.jsonsel("select * from healthcentre")
    return jsonify(status='ok', data=qry)

@app.route('/pubviewhospital',methods=['post'])
def pubviewhospital():
    db=Db()
    qry=db.jsonsel("select * from hospital")
    return jsonify(status='ok',data=qry)





# @app.route('/childdetails',methods=['post'])
# def childdetails():
#     db=Db()
#     did=request.form['did']
#     qry=db.selectone("select child_reg.*,enroll_child.photo from child_reg,vaccination_entry,enroll_child where vaccination_entry.child_id=child_reg.child_reg_id and enroll_child.hospital_child_reg_id=child_reg.child_reg_id and vaccination_entry.entry_id=1")
#     print(qry)
#     if len(qry)!=0:
#         return jsonify(status='ok',data=qry)
#     else:
#         return 'error'
#

@app.route('/childinfo', methods=['post'])
def childinfo():
        db = Db()
        lid = request.form["lid"]
        qry = db.jsonsel("select child_reg.*,enroll_child.photo from child_reg,enroll_child,enroll_mother where child_reg.motheraadharno=enroll_mother.aadhar_no and enroll_mother.lid='"+lid+"' and child_reg.child_reg_id=enroll_child.hospital_child_reg_id")
        print(qry)
        if len(qry) != 0:
            return jsonify(status='ok', data=qry)
        else:
            return 'error'

@app.route('/showall', methods=['post'])
def showall():
    db = Db()
    angu_id = request.form["angu_id"]
    vaccination_id = request.form["vaccination_id"]
    qry = db.jsonsel("select child_reg.name,child_reg.mothername,child_reg.email,child_reg.phone from child_reg,vaccination_entry where vaccination_entry.child_id=child_reg.child_reg_id and vaccination_entry.vaccination_id='"+vaccination_id+"' and vaccination_entry.venuid='"+angu_id+"'")
    print(qry)
    if len(qry) != 0:
        return jsonify(status='ok', data=qry)
    else:
        return 'error'



#..............................................................................................#
#..............................USER WEB........................................................#

@app.route('/motherviewnots')
def motherviewnots():
    db=Db()
    y=session['angu_id']
    qry=db.selectall("SELECT subject,massage, DATE_FORMAT(date, '%d/%m/%Y') as date from notification where angu_id='"+str(y)+"'")
    return render_template('User/view_notification.html',data=qry)


@app.route('/motherviewcalender')
def motherviewcalender():
    db=Db()
    qry=db.selectall("select * from calendar")
    return render_template('User/view_calender.html',data=qry)

@app.route('/motherviewnutri')
def motherviewnutri():
    db=Db()
    x=session['motherid']
    qry=db.selectall("select nutrtion_entry.date,nutrtion_entry.quantity,nutrition.name from nutrtion_entry,nutrition where nutrtion_entry.child_mother_id='"+str(x)+"' and status='mother' and nutrition.nutrition_id=nutrtion_entry.type")
    print(qry)
    return render_template('User/View_nutrition.html',data=qry)



@app.route('/motherviewcheckup')
def motherviewcheckup():
    db=Db()
    x=session['motherid']
    qry=db.selectall("select * from checkup where child_mother_id='"+str(x)+"' and status='mother'")
    print(qry)
    return render_template('User/View_cheackups.html',data=qry)



@app.route('/motherviewdoctor')
def motherviewdoctor():
    db = Db()
    qry = db.selectall("select * from staff where type='doctor'")
    return render_template('User/View_doctor.html',data=qry)


@app.route('/motherviewdoctorop/<ss>')
def motherviewdoctorop(ss):
    db = Db()
    qry = db.selectall("select staff.name,op.dates,op.from_time,op.to_time from op,staff where staff.staff_id=op.staff_id and staff.type='doctor' and staff.staff_id = '"+ss+"'")
    if len(qry)>0:
        return render_template('User/Doctor_OP.html',data=qry)
    else:
        return '''<script>alert('Sorry no data found');window.location='/motherviewdoctor'</script>'''

#
@app.route('/motherprofile')
def motherprofile():
    db=Db()
    x=session['lid']
    qry=db.selectone("select * from enroll_mother where lid='"+str(x)+"'")
    return render_template('User/View my profile.html',data=qry)


@app.route('/motherchangepswd')
def motherchangepswd():
    return render_template('User/Change password.html')






@app.route('/motherchangepswdd',methods=['post'])
def motherchangepswdd():
    db=Db()
    curpass=request.form['cur']
    newpass=request.form['new']
    conpass=request.form['con']
    x=session['lid']
    qry="select password from login where login_id='"+str(x)+"'"
    res=db.selectone(qry)
    print(res)
    if curpass==res[0]:
          qry1="update login set password='"+conpass+"' where login_id='"+str(x)+"'"
          res1=db.nonreturn(qry1)
          return '''<script>alert("Password changed");window.location='/motherchangepswd'</script>'''
    else:
        return '''<script>alert("Please fill your correct password");window.location='/motherchangepswd'</script>'''
if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

@app.route('/publicviewvacinatn',methods=['post'])
def publicviewvacinatn():
    db=Db()
    qry="select* from vaccination"