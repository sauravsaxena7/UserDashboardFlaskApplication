from app import app

from model.UserModel import UserModel
from flask import request

obj = UserModel()
@app.route("/user/signup")
def signup():
    return obj.UserSignUpModel()

@app.route("/user/GetAllUser")
def GetAllUser():
    return obj.GetAllUserModel()    

@app.route("/user/newUser",methods=["POST"])
def addNewUser():
    return obj.addNewUser(request.form)        
@app.route("/user/UpdateUserById",methods=["PUT"])
def UpdateUserById():
    return obj.UpdateUserById(request.form)        

@app.route("/user/updateUser",methods=["PUT"])
def updateUser():
    return obj.updateUser(request.form)   

@app.route("/user/deleteUser/<id>",methods=["DELETE"])
def deleteUser(id):
    return obj.deleteUser(id)                
@app.route("/user/getSingleUserById/<id>",methods=["GET"])
def getSingleUserById(id):
    print('ss')
    return obj.getSingleUserById(id)                

@app.route("/user/patchUser/<id>",methods=["PATCH"])
def patchUser(id):
    return obj.patchUser(id,request.form) 
@app.route("/user/GetAllUser/limit/<limit>/pageNumber/<page>")
def GetAllUserWithPagination(limit,page):
    return obj.GetAllUserWithPagination(limit,page)                         