
import json
import requests

def getUserRepos(user):
    """
    We are getting a list of all the repository names for a given user here
    """
    userLink = 'https://api.github.com/users/'+user+'/repos'
    resp = requests.get(userLink)
    repoJson = resp.text
    repoList = json.loads(repoJson)
    finalList = []
    #print(repoJson)
    for entry in repoList:
        finalList.append(entry['name'])
    #print(repoJson)
    return finalList


def getTotalCommits(user, repo):
    """
        We are getting a count of the repository commits for a given user here
    """
    commitsLink = 'https://api.github.com/repos/'+user+'/'+repo+'/commits'
    resp = requests.get(commitsLink)
    repoJson = resp.text
    repoList = json.loads(repoJson)
    finalList = []
    for entry in repoList:
        finalList.append(entry['sha'])
    count = len(finalList)
    return count

if __name__ == "__main__":
    user = 'celestesakhile'
    list=  getUserRepos(user)
    print("User: %s " %(user))
    for item in list:
        listCount = getTotalCommits(user,item)
        print ("Repo: %s and Number of commits : %2d" % (item, listCount))


""" 
a list of users on GitHub used for testing
akshya672222
celestesakhile
rafif353
Malidrisi
hydrodog
jtraweek
kenpuluma
MaryamAlMansour
"""