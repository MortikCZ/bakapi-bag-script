from datetime import datetime, timedelta
from bakapiv2 import BakapiUser

BAKALARI_URL = 'url'
BAKALARI_USERNAME = 'username' 
BAKALARI_PASSWORD = 'password'

api = BakapiUser(url=BAKALARI_URL, username=BAKALARI_USERNAME, password=BAKALARI_PASSWORD)

current_date = datetime.now().date()
formatted_date = current_date.strftime("%d.%m.")
print("Dnešní datum:", formatted_date)

def get_subjects_for_today_and_tomorrow(api):
    today = datetime.now().date()
    weekday = today.weekday()
    
    if weekday == 4:  
        tomorrow = today + timedelta(days=3)  
        timetable_today = api.get_timetable_actual(date=today)
        timetable_tomorrow = api.get_timetable_actual(date=tomorrow)
    elif weekday == 5 or weekday == 6:
        last_friday = today - timedelta(days=(weekday - 4))  
        next_monday = today + timedelta(days=(7 - weekday))  
        timetable_today = api.get_timetable_actual(date=last_friday)  
        timetable_tomorrow = api.get_timetable_actual(date=next_monday)  
        today = last_friday
        tomorrow = next_monday
    else:
        tomorrow = today + timedelta(days=1)  
        timetable_today = api.get_timetable_actual(date=today)
        timetable_tomorrow = api.get_timetable_actual(date=tomorrow)

    subjects_today = []
    subjects_tomorrow = []
    subject_id_to_name_today = {subject['Id']: subject['Name'] for subject in timetable_today['Subjects']}
    subject_id_to_name_tomorrow = {subject['Id']: subject['Name'] for subject in timetable_tomorrow['Subjects']}
        
    for day in timetable_today['Days']:
        day_date = datetime.fromisoformat(day['Date']).date()
        if day_date == today:
            subjects_today.extend(day['Atoms'])
    
    for day in timetable_tomorrow['Days']:
        day_date = datetime.fromisoformat(day['Date']).date()
        if day_date == tomorrow:
            subjects_tomorrow.extend(day['Atoms'])
        
    return {
        'today': subjects_today,
        'tomorrow': subjects_tomorrow,
        'subject_id_to_name_today': subject_id_to_name_today,
        'subject_id_to_name_tomorrow': subject_id_to_name_tomorrow
    }

def compare_subjects(today_subjects, tomorrow_subjects, subject_id_to_name_today, subject_id_to_name_tomorrow):
    today_subject_ids = {atom['SubjectId'] for atom in today_subjects if 'SubjectId' in atom and atom['SubjectId']}
    tomorrow_subject_ids = {atom['SubjectId'] for atom in tomorrow_subjects if 'SubjectId' in atom and atom['SubjectId']}

    subjects_to_take = tomorrow_subject_ids - today_subject_ids
    subjects_to_remove = today_subject_ids - tomorrow_subject_ids

    items_to_take = [subject_id_to_name_tomorrow.get(subject_id, f"Unknown Subject {subject_id}") for subject_id in subjects_to_take]
    items_to_remove = [subject_id_to_name_today.get(subject_id, f"Unknown Subject {subject_id}") for subject_id in subjects_to_remove]

    return items_to_take, items_to_remove

subjects = get_subjects_for_today_and_tomorrow(api)

items_to_take, items_to_remove = compare_subjects(subjects['today'], subjects['tomorrow'], subjects['subject_id_to_name_today'], subjects['subject_id_to_name_tomorrow'])

print("\nZ tašky si vyndej:")
for item in items_to_remove:
    print(item)
    
print("\nA do tašky si naopak dej:")
for item in items_to_take:
    print(item)

print("\nPřeji krásný den :)")