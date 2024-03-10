from app import app
@app.route("/product/categories/add")
def addNewProductCategories():
    return "I am adding your Product Categories"