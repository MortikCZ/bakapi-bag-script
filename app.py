from datetime import datetime, timedelta
from bakapiv2 import BakapiUser

BAKALARI_URL = 'url'
BAKALARI_USERNAME = 'username' 
BAKALARI_PASSWORD = 'password'

api = BakapiUser(url=BAKALARI_URL, username=BAKALARI_USERNAME, password=BAKALARI_PASSWORD)

current_date = datetime.now().date()
formatted_date = current_date.strftime("%d.%m.")
print("Dnešní datum:", formatted_date)

timetable = api.get_timetable_actual(date=current_date)

subject_id_to_name = {subject['Id']: subject['Name'] for subject in timetable['Subjects']}

def get_subjects_for_today_and_tomorrow(timetable):
    today = datetime.now().date()
    tomorrow = today + timedelta(days=1)
        
    subjects_today = []
    subjects_tomorrow = []
        
    for day in timetable['Days']:
        day_date = datetime.fromisoformat(day['Date']).date()
        if day_date == today:
            subjects_today.extend(day['Atoms'])
        elif day_date == tomorrow:
            subjects_tomorrow.extend(day['Atoms'])
        
    return {
        'today': subjects_today,
        'tomorrow': subjects_tomorrow
    }

def compare_subjects(today_subjects, tomorrow_subjects):
    today_subject_ids = {atom['SubjectId'] for atom in today_subjects if 'SubjectId' in atom and atom['SubjectId']}
    tomorrow_subject_ids = {atom['SubjectId'] for atom in tomorrow_subjects if 'SubjectId' in atom and atom['SubjectId']}

    subjects_to_take = tomorrow_subject_ids - today_subject_ids
    subjects_to_remove = today_subject_ids - tomorrow_subject_ids

    items_to_take = [subject_id_to_name[subject_id] for subject_id in subjects_to_take if subject_id in subject_id_to_name]
    items_to_remove = [subject_id_to_name[subject_id] for subject_id in subjects_to_remove if subject_id in subject_id_to_name]

    return items_to_take, items_to_remove

subjects = get_subjects_for_today_and_tomorrow(timetable)

items_to_take, items_to_remove = compare_subjects(subjects['today'], subjects['tomorrow'])

print("\nZ tašky si vyndej:")
for item in items_to_remove:
    print(item)
    
print("\nA do tašky si naopak dej:")
for item in items_to_take:
    print(item)

print("\nPřeji krásný den :)")