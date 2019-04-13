import gspread
from oauth2client.service_account import ServiceAccountCredentials

import CleanupHourScheduler
import MemberGenerator


def log_task(task_tup):

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)

    sheet = client.open('assignment_log').sheet1
    name_col = sheet.col_values(1)
    last_cell = len(name_col) + 1
    phone = task_tup[1].phone
    phone_new = '+1' + ''.join([char for char in phone if char != '-'])
    sheet.update_cell(last_cell, 1, phone_new)
    sheet.update_cell(last_cell, 2, task_tup[1].first + ' ' + task_tup[1].last)
    sheet.update_cell(last_cell, 3, task_tup[0].name)


if __name__ == '__main__':
    tasks = CleanupHourScheduler.schedule_hours()
    task1 = tasks[0]
    member1 = MemberGenerator.Member('John', 'Miles', '470-263-7816', 'j.austinmiles@outlook.com', 'Brother', True)
    log_task((task1, member1))
