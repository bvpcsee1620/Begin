from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from server import app, db, User, Tasks, Role, Department
from datetime import datetime
from datetime import timedelta


manager = Manager(app)
migrate = Migrate(app, db)

manager.add_command('db', MigrateCommand)


def create_user(email, imgurl, number, link, name, db, password, role, d,desig):
    user = User(email, imgurl, number, link, name, "", desig, "", "")
    _date1 = datetime.now().date()
    _date2 = _date1 + timedelta(days=1)
    _t1 = Tasks("bvcoe.erp@gmail.com", user.username, "vansifysecret", _date1,
                'https://vignette.wikia.nocookie.net/monstergirlencyclopedia/images/d/d0/Discord_logo.png/revision/latest?cb=20160622232221', _date1)
    _t2 = Tasks("bvcoe.erp@gmail.com", user.username, "vansifysecret", _date2,
                'https://vignette.wikia.nocookie.net/monstergirlencyclopedia/images/d/d0/Discord_logo.png/revision/latest?cb=20160622232221', _date2)

    user.set_password(password)
    user.roles = role
    user.department_id = [d]
    db.session.add(_t1)
    db.session.add(_t2)
    db.session.add(user)

@manager.command
def setup_production():
    """ Sets Production server
    """


@manager.command
def recreate_db():
    """
    Recreates a local database. You probably should not use this on
    production.
    """
    db.drop_all()
    db.create_all()
    # Create Roles
    Admin_role = Role(name='Admin')
    Principal_role = Role(name='Principal')
    Faculty_role = Role(name='Faculty')
    Hod_role = Role(name='Hod')
    TimeTableEditor_role = Role(name='Tte')
    cse = Department("cse")

    # create test users for server
    create_user("aniket965.as@gmail.com", "https://avatars2.githubusercontent.com/u/22680912?s=460&v=4.jpg",
                "9899023974", "https://github.com/Aniket965", "Aniket Sharma", db, "pythonani", [Admin_role], cse,"Creater")
    create_user("ujjwalupadhyay8@gmail.com", "https://avatars1.githubusercontent.com/u/24938377?s=400&v=4.jpg",
                "8800752205", "https://github.com/Ujjwal-9", "Ujjwal", db, "pythonujj", [TimeTableEditor_role], cse,"Creater")
    create_user("oberoivansh01@gmail.com", "https://avatars3.githubusercontent.com/u/25277821?s=460&v=4.jpg",
                "9811988890", "https://github.com/vanshoberoi", "Vansh Oberoi", db, "pythonvan", [Admin_role], cse,"Creater")
    create_user("manojs11@gmail.com", "http://bvcoend.ac.in/images/upload/BVP_Bharati_Vidyapeeths_College_of_Engineering_,New_Delhi_73838283118880FILE79505UPLOAD44466301482223859.jpg",
                "9873077961", "http://ece.bvcoend.ac.in/site/home/index/319", "Manoj Sharma", db, "pythonman", [Faculty_role, TimeTableEditor_role], cse,"Creater")
    create_user("mohit.tiwari@bharatividyapeeth.edu", "http://bvcoend.ac.in/images/upload/BVP_Bharati_Vidyapeeths_College_of_Engineering_,New_Delhi_25208891009222FILE57806UPLOAD56345011453378454.jpg",
                "9810161203", "http://cse.bvcoend.ac.in/site/home/index/235", "Mohit Tiwari", db, "pythonmoh", [Faculty_role, TimeTableEditor_role], cse,"Creater")
    create_user("bvcoe.erp@gmail.com", "https://vignette.wikia.nocookie.net/monstergirlencyclopedia/images/d/d0/Discord_logo.png/revision/latest?cb=20160622232221.jpg",
                "0000000000", "http://cse.bvcoend.ac.in/site/home/", "ERP Bot", db, "pythonerp", [Admin_role], cse,"Creater")
    create_user("principalbvcoedelhi@bharatividyapeeth.edu", "http://bvcoend.ac.in/images/upload/BVP_Bharati_Vidyapeeths_College_of_Engineering_,New_Delhi_49380433071343FILE19550UPLOAD48612691425921280.jpg",
                "9818195362", "http://cse.bvcoend.ac.in/site/home/", "Dr. Dharmendar Saini", db, "pythonpri", [Principal_role], cse,"Creater")
    create_user("sandeep.d.patil@bharatividyapeeth.edu", "https://raw.githubusercontent.com/Aniket965/react-native-truth-and-dare/master/img.jpg",
                "9999007020", "http://cse.bvcoend.ac.in/site/home/", "Mr. Sandeep Patil", db, "pythonsan", [Admin_role], cse,"Creater")
    create_user("narina.thakur@bharatividyapeeth.edu", "http://bvcoend.ac.in/images/upload/BVP_Bharati_Vidyapeeths_College_of_Engineering_,New_Delhi_43653538063998FILE63752UPLOAD75612601425921342.jpg",
                "9999007021", "http://cse.bvcoend.ac.in/site/home/", "Mrs. Narina Thakur", db, "pythonsan", [Hod_role], cse,"Creater")
    db.session.commit()


if __name__ == '__main__':
    manager.run()
