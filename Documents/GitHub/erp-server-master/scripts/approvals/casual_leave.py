import os
from docxtpl import DocxTemplate, RichText
from datetime import datetime
tpl = DocxTemplate(os.path.abspath('casualleave.docx'))
date = datetime.now().strftime('%d-%m-%Y')
data = {
    "to_date":"29-06-2018",
    "c_name":"Manoj Sharma",
    "r_name":"Mohit Tiwari",
    "r_department":"CSE",
    "msg": "Need to go Urgent Family Function",
    "time" :"2pm-5pm",
    "designation":"Assistant Prof",
    "requested_date": date,
    "date":date,
    "department":"ECE",
    "hod_name":"Dr. Anuradha Basu",
    "date_approval":date,
    "num_leaves":"2",
    "created_date":date,
    }
tpl.render(data)
tpl.save('{}1.docx'.format(date))