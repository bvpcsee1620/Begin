from server import app,db,User, Tasks, Role, Department
from datetime import datetime, timedelta

import os
import pytest
import base64

## Credentials for testing

valid_admin_credentials = base64.b64encode(b'aniket965.as@gmail.com:pythonani').decode('utf-8')
valid_Tte_credentials = base64.b64encode(b'ujjwalupadhyay8@gmail.com:pythonujj').decode('utf-8')
valid_principal_credentials = base64.b64encode(b'principalbvcoedelhi@bharatividyapeeth.edu:pythonpri').decode('utf-8')
valid_hod_credentials = base64.b64encode(b'narina.thakur@bharatividyapeeth.edu:pythonsan').decode('utf-8')
valid_faculty_credentials = base64.b64encode(b'mohit.tiwari@bharatividyapeeth.edu:pythonmoh').decode('utf-8')


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

@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['TEST_DATABASE_URL']
    client = app.test_client()
    with app.app_context():
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
    yield client
