"""
List of Users with UserId and Name
List of Logins with UserId and timestamp
Return leaderboard - Name and unique(login),

Example:
Users - [{1,"qw"},{2,"er"}]
Logins - [{1,1},{1,1},{1,3},{2,4},{2,5},{1,7}]
output (Print in descending order based on login attempts)
"qw" : 3
"er" : 2

User "qw" logged 4 times in total, unique attempts - 3. you can assume any input type (either 2d array or List).
"""
from collections import defaultdict

def leaderboard(users, logins):
	users_by_id = {}
	for uid, name in users:
		users_by_id[uid] = name

	logins_by_user = defaultdict(lambda: set())
	login_counts_by_user = defaultdict(lambda: 0)
	for user, time in logins:
		if time in logins_by_user[user]:	# dupe
			continue

		logins_by_user[user].add(time)
		login_counts_by_user[user] = login_counts_by_user[user] + 1

	counts = [(users_by_id[uid], count) for uid, count in login_counts_by_user.items()]
	counts.sort(key=lambda x: x[1], reverse=True)
	return counts

print(leaderboard([[1,"qw"],[2,"er"]], [[1,1],[1,1],[1,3],[2,4],[2,5],[1,7]]))
