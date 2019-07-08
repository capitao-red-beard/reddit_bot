import praw

reddit = praw.Reddit(client_id='',
                     client_secret='',
                     username='',
                     password='',
                     user_agent='')

subreddit = reddit.subreddit('python')

hot_python = subreddit.hot(limit=3)

conversedict = {}

for submission in hot_python:
    if not submission.stickied:
        print(f'TITLE: {submission.title}\n'
              f'UPS: {submission.ups}\n'
              f'DOWNS: {submission.downs}\n'
              f'VISITED: {submission.visited}\n'
              f'ID: {submission.id}\n\n')

        submission.comments.replace_more(limit=0)
        for comment in submission.comments.list():

            if comment.id not in conversedict:
                conversedict[comment.id] = [comment.body, {}]

                if comment.parent() != submission.id:
                    parent = str(comment.parent())
                    conversedict[parent][1][comment.id] = [comment.ups, comment.body]

                    for post_id in conversedict:
                        message = conversedict[post_id][0]
                        replies = conversedict[post_id][1]

                        if len(replies):
                            print(50 * '-')
                            print(f'ORIGINAL MESSAGE : {message}')

                            count = 0
                            for reply in replies:
                                count += 1
                                print(f'REPLY {count} : {replies[reply][1][:200]}')
