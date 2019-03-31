import openpyxl
from time import time


class CleanupHour:

    def __init__(self, name: str, task_id: int, day: str, due_time: time, worth: int, difficulty: int):
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

    def __str__(self):
        return """Name: """ + self.name\
               + """\nDue Date: """ + str(self.day)\
               + """\nDue Time: """ + str(self.due_time)\
               + """\nWorth: """ + str(self.worth)
        # + """\nDifficulty: """ + str(self.difficulty) + '\n'
        # + """\nId: """ + str(self.task_id)\


def schedule_hours() -> list:
    """
    Retrieves the weekly cleanup-hour schedule from the Cleanup Sheet.xlsx
    and formats the table into a list of CleanupHour objects
    :rtype: list
    :return: list of CleanupHour objects
    """
    excel_document = openpyxl.load_workbook('Cleanup Sheet.xlsx')
    cleanup_hours_sheet = excel_document['Weekly Schedule']
    hours_list = []
    for i in range(2, cleanup_hours_sheet.max_row + 1):
        cleanup_row = cleanup_hours_sheet[i]
        name = cleanup_row[0].value
        task_id = cleanup_row[1].value
        day = cleanup_row[2].value
        due_time = cleanup_row[3].value
        worth = cleanup_row[4].value
        difficulty = cleanup_row[5].value
        hour = CleanupHour(name, task_id, day, due_time, worth, difficulty)
        # print(hour)
        hours_list.append(hour)
    return hours_list


if __name__ == '__main__':
    # To see output, uncomment statement in schedule_hours()
    schedule_hours()
