import gspread
from time import time

from oauth2client.service_account import ServiceAccountCredentials


class CleanupHour:

    def __init__(self, name: str, task_id: int, day: str, due_time: time, worth: int, difficulty: int, link: str):
        """
        A CleanupHour holds the metadata and values for a cleanup task
        :param name: name of the task
        :param task_id: id to identify the task, used to load task descriptions
        :param day: due date of the task
        :param due_time: due time of the task
        :param worth: the cleanup-hour worth of completion of the task
        :param difficulty: estimated difficulty (scale of 1-5) of the task
        """
        self.name = name
        self.task_id = task_id
        self.day = day
        self.due_time = due_time
        self.worth = worth
        self.difficulty = difficulty
        self.link = link

    def __str__(self):
        return """Name: """ + self.name\
               + """\nDue Date: """ + str(self.day)\
               + """\nDue Time: """ + str(self.due_time)\
               + """\nWorth: """ + str(self.worth)\
               + """\nLink: """ + str(self.link)
        # + """\nDifficulty: """ + str(self.difficulty) + '\n'
        # + """\nId: """ + str(self.task_id)\


def schedule_hours() -> list:
    """
    Retrieves the weekly cleanup-hour schedule from the Cleanup Sheet.xlsx
    and formats the table into a list of CleanupHour objects
    :rtype: list
    :return: list of CleanupHour objects
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('cleanup_sheet').get_worksheet(1)
    col_one = sheet.col_values(1)
    max_row = len(col_one)
    hours_list = []
    for i in range(2, max_row + 1):
        row = sheet.row_values(i)
        name = row[0]
        task_id = row[1]
        day = row[2]
        due_time = row[3]
        worth = row[4]
        difficulty = row[5]
        link = row[6]
        hour = CleanupHour(name, task_id, day, due_time, worth, difficulty, link)
        print(hour)
        hours_list.append(hour)
    return hours_list


if __name__ == '__main__':
    # To see output, uncomment statement in schedule_hours()
    schedule_hours()
