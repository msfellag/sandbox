# INPUT  : jobId
# OUTPUT : List of dictionaries, {UserId, FirstName, LastName}
# 
# STATUS : Work in progress...
import csv

def users_per_appl(jobId):

    jobId = str(jobId)
    path_applications = "files/user_job_cand.csv"
    path_users = "files/users.csv"

    # the newline arg is to get rid of OS related newlines problems CR/LF
    file_applications = open(path_applications, newline='')
    file_users = open(path_users, newline='')

    reader_applications = csv.reader(file_applications)
    reader_users = csv.reader(file_users)

    # pop the headers of the csv files off
    header_applications = next(reader_applications)
    header_users = next(reader_users)

    data_users = {row[0] : { 'fname': row[1], 'lname': row[2]} for row in reader_users}

    #jobId = str(input("JobId : "))

    users = []
    for row in reader_applications:
        if row[1] == jobId and row[0] not in users:
            users.append(row[0])

    returnList = []
    for userId in users:
        returnList.append({'UserId': userId, 'FirsName': data_users[userId]['fname'], 'LastName': data_users[userId]['lname']})

    #print(returnList)
    # for i in returnList:
    #     print('{')
    #     for x, y in i.items():
    #         print(x, y)
    #     print('}')

    file_applications.close()
    file_users.close()

    return returnList