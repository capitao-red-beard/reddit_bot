import praw

reddit = praw.Reddit(client_id='CmBIwUSAgeM9cg',
                     client_secret='kYfOAuiyjkjf2t-sm5LkTgLIb4M',
                     username='_2147483647',
                     password='!Fr441j314#',
                     user_agent='reddit_bot')

subreddit = reddit.subreddit('python')

for comment in subreddit.stream.comments():
    try:
        parent_id = str(comment.parent())
        original = reddit.comment(parent_id)
        print('PARENT:')
        print(original.body)

        print('REPLY:')
        print(comment.body)

    except praw.exceptions.PRAWException as e:
        print(str(e))
