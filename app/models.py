from app.routes import db


class Item(db.Model):
    __tablename__ = "Item"
    item_id = db.Column(db.Integer, primary_key=True)
    image_web = db.Column(db.Text)
    image_local = db.Column(db.Text)
    image_public = db.Column(db.LargeBinary)


class List(db.Model):
    __tablename__ = "List"
    list_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    description = db.Column(db.Text)


class User(db.Model):
    __tablename__ = "User"
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text)
    hash = db.Column(db.Text)
    salt = db.Column(db.Text)
