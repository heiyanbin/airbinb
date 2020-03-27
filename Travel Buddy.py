def buddyList(myList, friendList):
    ans = []
    similar = {}
    for friend, hisList in friendList.iteritems():
        intersect = myList & hisList
        similar[friend] = float(len(intersect)) / len(hisList)
        if similar[friend] >= 0.5:
            ans.append(friend)

    return sorted(ans, key=lambda x: similar[x], reverse=True)

myList = set(['a', 'b', 'c', 'd'])
friendList = {
    'tom': set(['a', 'c', 'x']),
    'kate': set(['c', 'd', 'y', 'a']),
    'mary': set(['a', 'x', 'z'])
}

print buddyList(myList, friendList);




