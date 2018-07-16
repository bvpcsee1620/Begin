from io import BytesIO
def fill_data(approval_date='', name='', msg='', designation='', dept='', hod_name='', date=''):
	import os
	from docxtpl import DocxTemplate, RichText
	from datetime import datetime
	import sys

	sys.path.insert(0, '.')
	tpl = DocxTemplate(os.path.abspath('./scripts/approvals/shortleave.docx'))
	data = {
	    "approval_date": date,
	    "c_name": name,
	    "msg": msg,
	    "time": "2pm-5pm",
	    "designation": designation,
	    "requested_date": date,
	    "date": date,
	    "department": dept,
	    "hod_name": hod_name,
	    "date_approval": date
	    }
	f = BytesIO()
	tpl.render(data)
	tpl.save(f)
	f.seek(0)
	return f
