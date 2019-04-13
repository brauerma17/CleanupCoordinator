import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials


class Member:

    def __init__(self, first: str, last: str, phone: str, email: str, status: str, active: bool):
        """
        Holds metadata and real data for members of the fraternity.
        Stored in the hours field is the running total of cleanup hours
        the member currently has. Default to -1 for work with exception
        handling
        :param first: first name of member
        :param last: last name of member
        :param phone: phone number of member
        :param email: email address of member
        :param status: whether the member is an Associate Member,
                       a Brother, or part of the Sayonara Squad (SS)
        :param active: whether the member is and active brother
        """
        self.first = first
        self.last = last
        self.phone = phone
        self.email = email
        self.status = status
        self.active = active
        self.hours = -1

    def __str__(self):
        return """Name: """ + self.first + ' ' + self.last\
               + """\nPhone: """ + str(self.phone)\
               + """\nEmail: """ + str(self.email)\
               + """\nStatus: """ + str(self.status)\
               + """\nActive: """ + str(self.active)\
               + """\nHours: """ + str(self.hours) + '\n'

    def member_status(self) -> int:
        """
        Simple mechanism to providing a comparable interface between members
        based on status. Lower number implies greater importance. To be used
        as a key in a lambda expression to perform sorting on lists of Members
        :rtype: int
        :return: integer equivalent of the status of the brother.
        TODO: fill out AM
        """
        if self.status == 'SS':
            return 0
        elif self.status == 'NIB':
            return 2
        else:
            return 1


def generate_members() -> list:
    """
    Generates a list of Member objects from Cleanup Sheet.xlsx. Each member's
    data is extracted and stored in a Member. Running total of hours is accessed by
    calling the generate_hours method
    :rtype: list
    :return: list of Member objects
    """
    hours_dict = generate_hours()
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('cleanup_sheet').get_worksheet(2)
    col_one = sheet.col_values(1)
    max_row = len(col_one)
    members = []
    for i in range(2, max_row + 1):
        time.sleep(1.2)
        member_row = sheet.row_values(i)
        name_first = member_row[0]
        name_last = member_row[1]
        phone = member_row[2]
        email = member_row[3]
        status = member_row[4]
        active = member_row[5]
        member = Member(name_first, name_last, phone, email, status, active)
        member.hours = hours_dict.get(name_first.strip() + name_last.strip(), -1)
        members.append(member)
        print(member)
    return members


def generate_hours() -> dict:
    """
    Retrieves the running total of hours for all members from the Cleanup Sheet.xlsx
    The values are stored in a dictionary where the key is the member's last name
    :rtype: dict
    :return: dict of hours mapping value 'hours' to key 'last name'
    """
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('cleanup_sheet').get_worksheet(3)
    col_one = sheet.col_values(1)
    max_row = len(col_one)
    hours_dict = {}
    for i in range(2, max_row + 1):
        time.sleep(1.2)
        member_row = sheet.row_values(i)
        hours_dict[member_row[0].strip() + member_row[1].strip()] = member_row[2]
    return hours_dict


if __name__ == '__main__':
    # To see output, uncomment print statements in generate_members()
    generate_members()
