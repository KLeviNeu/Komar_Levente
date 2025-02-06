from github import Github
access_token = "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"
g = Github(access_token)
user = g.get_user()
print(user.login)
