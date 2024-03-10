#python -m venv venv
#.\venv\Scripts\activate
#pip install flask
#python.exe -m pip install --upgrade pip
#DECORATOR STARTS WITH @app.name()
#$env:FLASK_ENV="development"
# flask --app example_app.py --debug run
# This will enable auto-reload whenever 
# changes are made to your code and saved. 
# It will also enable an interactive debugger 
# in the browser if any errors occur during a request.

#FOR PREVENTING FOR CREATING PYCACHE $env:PYTHONDONTWRITEBYTECODE=1


# $ flask shell
# Connection Is SuccessFull
# Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
# App: app
# Instance: E:\pyhton projects\Flask_Application\instance
# >>> db.create_all()
# >>> 

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1 : : 2])

from copy import copy, deepcopy
list_1 = [1, 2, [3, 5], 4]
## shallow copy
list_2 = copy(list_1) 
list_2[3] = 7
list_2[2].append(6)
print(list_2)    # output => [1, 2, [3, 5, 6], 7]
print(list_1)  # output => [1, 2, [3, 5, 6], 4]
## deep copy
list_3 = deepcopy(list_1)
list_3[3] = 8
list_3[2].append(7)
print(list_3)    # output => [1, 2, [3, 5, 6, 7], 8]
print(list_1)    # output => [1, 2, [3, 5, 6], 4]