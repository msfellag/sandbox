# This program takes an userId and outputs the jobs that the user has applied to
# input: userID type int
# output: a List of Dictionnaries containing jobID and jobTitle
#
# STATUS : it works ! to integrate into main solution.
import csv

def appl_per_user(userId):

    userId = str(userId) # check later if this can be removed?

    path_applications = "files/user_job_cand.csv"
    path_jobs = "files/jobs.csv"

    # the newline arg is to get rid of OS related newlines problems
    file_applications = open(path_applications, newline='')
    file_jobs = open(path_jobs, newline='')

    reader_applications = csv.reader(file_applications)
    reader_jobs = csv.reader(file_jobs)

    # pop the headers of the csv files off
    header_applications = next(reader_applications)
    header_jobs = next(reader_jobs)

    #userId = str(input("Enter a userId :"))

    # i will use a dictionary to avoid dealing with duplicates
    dict = {}

    for row in reader_applications:
        if row[0] == userId:
            dict[row[1]] = None

    for key in dict.keys():
        for row in reader_jobs:
            if row[0] == key:
                dict[key] = row[1]
                break


    # this last loop was a deliberate choice to avoid type casting inside the bigger loop
    # for the JobId from string to int and also making everything conforms to the requirements
    returnList = []
    for key, value in dict.items():
        returnList.append({"JobId": int(key), "Title": value})

    #print(returnList)
    # for i in returnList:
    #     print(i)

    file_applications.close()
    file_jobs.close()

    return returnList