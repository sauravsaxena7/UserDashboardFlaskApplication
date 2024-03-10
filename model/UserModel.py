#import mysql.connector
import json
from flask import make_response
from app import db,Userss
 
#from app import engine
class UserModel():
    def __init__(self):
        #constructor 
        try:
            # self.conn=mysql.connector.connect(host="localhost",user="root",password="Lola@121",database="flask_tutorial")
            # self.conn.autocommit=True 
            # self.cur=self.conn.cursor(dictionary=True)

            #self.conn=engine.connect()
            # self.conn.autocommit=True
            # self.cur=self.conn.cursor(dictionary=True)
            print("Connection Is SuccessFull")
        except Exception as e:
            print('some error')
            print(e)
        
    def UserSignUpModel(self):
        return "This is signUp model"

    def GetAllUserModel(self):
        # self.cur.execute("select * from users")
        # result=self.cur.fetchall()
        #print(result)
        #json.dumps(result)
        # query = sqlalchemy.select(book)
        # result = Users.query.first()
        # res=make_response({"payload": result},200)
        # res.headers['Access-Control-Allow-Origin']="*"
        return "Nothing"
    def addNewUser(self,data):
        #self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        user = Userss.query.filter_by(email=data['email']).first()
        message="User Already Exist"
        code=200
        if user is None:
            user=Userss(name=data['name'],password=data['password'],role=data['role'],email=data['email'],phone=data['phone'])
            db.session.add(user)
            db.session.commit()
            message="User Added SuccessFully!"
            code=201
        print(data)
        res=make_response({"message":message},code)
        res.headers['Access-Control-Allow-Origin']="*"
        return res; 
    def UpdateUserById(self,data):
        #self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        print(data)
        user = Userss.query.filter_by(id=int(data['id'])).first()
        code=200
        if user is not None:
            u=db.session.query(Userss).filter(Userss.id == int(data['id'])).one()
            u.name=data['name']
            u.email=data['email']
            u.password=user.password
            u.phone=data['phone']
            u.role=user.role
            db.session.commit()
            message="User Updated SuccessFully!"
            code=200
        
        res=make_response({"message":message,"name":user.name},code)
        res.headers['Access-Control-Allow-Origin']="*"
        return res;     
    def getSingleUserById(self,id):
        #self.cur.execute(f"INSERT INTO users(name,email,phone,role,password) VALUES ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        user = Userss.query.filter_by(id=int(id)).first()
        code=200
        res=make_response({"user":{"name":user.name,"email":user.email,"phone":user.phone,"role":user.role,"id":user.id,"password":user.password}},code)
        res.headers['Access-Control-Allow-Origin']="*"
        return res;     

    def updateUser(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}' , email='{data['email']}' , role='{data['role']}' , password='{data['password']}' WHERE id={data['id']} ")
        print(data)
        if self.cur.rowcount>0:
            return "user update successfully"
        else:
            return "Nothing to update"; 

    def deleteUser(self,id):
        # self.cur.execute(f"DELETE FROM users WHERE id={id}")
        user = Userss.query.filter_by(id=int(id)).first()
        message="User Not Found"
        print(id)
        code=404
        if user is not None:
            db.session.delete(user)
            db.session.commit()
            message="User DELETED SuccessFully!"
            code=200
        res=make_response({"message":message},code)
        res.headers['Access-Control-Allow-Origin']="*"
        return res

    def patchUser(self,id,data):
        qry="UPDATE users SET "
        for key in data:
            print(f"{key}={data[key]}")
            qry=qry+f"{key}='{data[key]}',"
        qry=qry[:-1]  +f" WHERE id={id}"

        self.cur.execute(qry)
        
        if self.cur.rowcount>0:
            return "user update successfully"
        else:
            return "Nothing to update";  
    def GetAllUserWithPagination(self,limit,pagee) :
        limit=int(limit)
        pagee=int(pagee)
        # start=(page*limit)-limit
        # qry=f"SELECT * FROM users LIMIT {start},{limit}"
        # self.cur.execute(qry)
        # result=self.cur.fetchall()
        res=Userss.query.all()
        result =Userss.query.order_by(Userss.date_added.desc()).paginate(page=pagee, per_page=limit,error_out=True)
        ii=[]
        for u in result.items:
            ii.append({"name":u.name,"phone":u.phone,"email":u.email,"role":u.role,"id":u.id,"UserCreatedAt":u.date_added})
            
        #json.dumps(result)
        res=make_response({"payload": ii,"totalCount":len(res)},200)
        res.headers['Access-Control-Allow-Origin']="*"
        return res


        
               
                          
