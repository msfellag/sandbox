# INPUT  : jobId
# OUTPUT : A List of dictionaries, {UserId: value1, FirstName: value2, LastName: value3}
# 
# DESC: 
import csv

def users_per_application(jobId):

    #jobId = str(jobId)

    path_applications = "files/user_job_cand.csv"
    path_users = "files/users.csv"

    # the newline arg is to get rid of OS related newlines problems CR/LF
    file_applications = open(path_applications, newline='', encoding="utf-8")
    file_users = open(path_users, newline='', encoding="utf-8")

    reader_applications = csv.reader(file_applications)
    reader_users = csv.reader(file_users)

    # pop the headers of the csv files off
    header_applications = next(reader_applications)
    header_users = next(reader_users)

    # load and format the users.csv data in a dictionary of dictionaries
    # for ease of retrieval 
    # {'ID' : { 'fname' : first_name,
    #           'lname' : last_name    }}
    data_users = {row[0] : { 'fname': row[1], 'lname': row[2]} for row in reader_users}

    # Find all the users-IDs associated to the input jobID
    users = []
    for row in reader_applications:
        if row[1] == jobId and row[0] not in users:
            users.append(row[0])

    # Associate each user-ID with it's first and last name
    returnList = []
    for userId in users:
        returnList.append({'UserId': userId, 'FirsName': data_users[userId]['fname'], 'LastName': data_users[userId]['lname']})

    file_applications.close()
    file_users.close()

    return returnList