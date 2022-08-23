#
# INPUT : userID type string
# OUTPUT: a List of Dictionnaries containing jobID and jobTitle
#
#  DESC: This functions takes a userId and outputs the jobs that the user has applied to
import csv

def applications_per_user(userId):

    # This could probably be removed [but better safe than sorry]
    userId = str(userId) 

    path_applications = "files/user_job_cand.csv"
    path_jobs = "files/jobs.csv"

    # the newline argument is to get rid of OS related newlines problems
    # the encoding arg seems necessary for windows 10 (not so much for linux dunno why)

    file_applications = open(path_applications, newline='', encoding="utf-8")
    file_jobs = open(path_jobs, newline='', encoding="utf-8")

    reader_applications = csv.reader(file_applications)
    reader_jobs = csv.reader(file_jobs)

    # pop the headers of the csv files off
    header_applications = next(reader_applications)
    header_jobs = next(reader_jobs)

    # Collecting the job-IDs associated with the input user-ID in a list
    # While ignoring  duplicates
    jobs = []

    for row in reader_applications:
        if row[0] == userId and row[1] not in jobs:
            jobs.append(row[1])
    # Associating each job-ID to a Title description
    # and storing them as a pair of dictionary values ready to output
    returnList = []

    for row in reader_jobs:
        # Break : if the list is empty wether due to the userID not having any matching jobs
        # or that we have associated every job with its title
        if jobs == []:
            break

        if row[0] == jobs[0]:
            returnList.append({"JobId": int(row[0]), "Title": row[1]})
            jobs.pop(0)

    file_applications.close()
    file_jobs.close()

    return returnList