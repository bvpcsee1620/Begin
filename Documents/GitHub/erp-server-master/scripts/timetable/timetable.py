import os
from docxtpl import DocxTemplate, RichText
import sys
sys.path.insert(0, '../../')
import format as f
from datetime import datetime
from io import BytesIO

def time_(x):
    return datetime.strptime(str(x), '%I:%M%p').replace(second=0, microsecond=0).time()


slots = {
  'slot1': [time_('10:30AM'), time_('11:25AM')],
  'slot2': [time_('11:25AM'), time_('12:20PM')],
  'slot3': [time_('12:50PM'), time_('01:45PM')],
  'slot4': [time_('01:45PM'), time_('02:40PM')],
  'slot5': [time_('02:40PM'), time_('03:35PM')],
  'slot6': [time_('03:35PM'), time_('04:30PM')],
  'slot7': [time_('04:30PM'), time_('05:35PM')],
  'slot8': [time_('05:35PM'), time_('06:30PM')]
}





def time(x):
    return datetime.strptime(str(x), '%Y-%m-%d %H:%M:%S').replace(second=0, microsecond=0).time()


def room_timetable(info, room):
  date = datetime.now().strftime('%d-%m-%Y')
  context = {
      'date': date,
      'rows': [{'day': 'mon',}, {'day': 'tue',}, {'day': 'wed',}, {'day': 'thu',}, {'day': 'fri',}]
  }
  print("start")
  # print(info)
  sys.path.insert(0, '.')
  # tpl = DocxTemplate('timetable/format.docx')
  tpl = DocxTemplate(os.path.abspath('scripts/timetable/room.docx'))
  date = datetime.now().strftime('%d-%m-%Y')
  context['room'] = room
  for data in info:
    for slot in slots.keys():
      if (time(data['start_time']) < slots[slot][1]) and (time(data['end_time']) > slots[slot][0]):
        for i,j in enumerate(context['rows']):
          if j['day'] == data['day']:
            # print(data)
            context['rows'][i][slot] = {
              'name': data['lec_name'],
              't_name': data['t_name'],
              'batch_name': data['batch_name']
            }

  for data in context['rows']:
    for slot in slots.keys():
      if slot not in data.keys():
        data[slot] = {
          'name': ' ',
          't_name': ' ',
          'batch_name': ' '
        }
  f = BytesIO()
  tpl.render(context)
  tpl.save(f)
  f.seek(0)
  return f

#####################################################FORMAT TO BE MADE FOR THEM###########################################################
def faculty_timetable(info, faculty,department):
  date = datetime.now().strftime('%d-%m-%Y')
  context = {
      'date': date,
      'rows': [{'day': 'mon',}, {'day': 'tue',}, {'day': 'wed',}, {'day': 'thu',}, {'day': 'fri',}]
  }
  print("start")
  # print(info)
  sys.path.insert(0, '.')
  # tpl = DocxTemplate('timetable/format.docx')
  tpl = DocxTemplate(os.path.abspath('scripts/timetable/faculty.docx'))
  date = datetime.now().strftime('%d-%m-%Y')
  context['faculty'] = faculty
  context['department'] = department
  for data in info:
    for slot in slots.keys():
      if (time(data['start_time']) < slots[slot][1]) and (time(data['end_time']) > slots[slot][0]):
        for i,j in enumerate(context['rows']):
          if j['day'] == data['day']:
            # print(data)
            context['rows'][i][slot] = {
              'name': data['lec_name'],
              'batch_name': data['batch_name'],
              'batch_part': data['batch_part']
            }

  for data in context['rows']:
    for slot in slots.keys():
      if slot not in data.keys():
        data[slot] = {
          'name': ' ',
          'batch_name': ' ',
          'batch_part': ' '
        }
  f = BytesIO()
  tpl.render(context)
  tpl.save(f)
  f.seek(0)
  return f


def batch_timetable(info, batch):
  date = datetime.now().strftime('%d-%m-%Y')
  context = {
      'date': date,
      'rows': [{'day': 'mon',}, {'day': 'tue',}, {'day': 'wed',}, {'day': 'thu',}, {'day': 'fri',}]
  }
  print("start")
  # print(info)
  sys.path.insert(0, '.')
  # tpl = DocxTemplate('timetable/format.docx')
  tpl = DocxTemplate(os.path.abspath('scripts/timetable/batch.docx'))
  date = datetime.now().strftime('%d-%m-%Y')
  context['batch'] = batch
  for data in info:
    for slot in slots.keys():
      if (time(data['start_time']) < slots[slot][1]) and (time(data['end_time']) > slots[slot][0]):
        for i,j in enumerate(context['rows']):
          if j['day'] == data['day']:
            # print(data)
            context['rows'][i][slot] = {
              'name': data['lec_name'],
              't_name': data['t_name'],
              'batch_part': data['batch_part']
            }

  for data in context['rows']:
    for slot in slots.keys():
      if slot not in data.keys():
        data[slot] = {
          'name': ' ',
          't_name': ' ',
          'batch_part': ' '
        }
  f = BytesIO()
  tpl.render(context)
  tpl.save(f)
  f.seek(0)
  return f
##########################################################################################################################################


############################################################For Testing###################################################################
# if __name__ == '__main__':
#   room_timetable()
#   # faculty_timetable()
#   # batch_timetable