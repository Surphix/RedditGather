import json
import datetime

frmt = "%Y-%m-%d %H:%M:%S"

def to_utc(epoch):
    t_utc = datetime.datetime.utcfromtimestamp(epoch)
    return t_utc.strftime(frmt)

def submission_to_dict(d, submission):
    p = {}
    
    if hasattr(submission, 'id'):
        p["id"] = submission.id
    if hasattr(submission, 'title'):
        p["title"] = submission.title
    if hasattr(submission, 'created_utc'):
        p["created"] = to_utc(submission.created_utc)
    if hasattr(submission, 'name'):
        p["name"] = submission.name
    if hasattr(submission, 'url'):
        p["url"] = submission.url
    if hasattr(submission, 'selftext'):
        p["text"] = submission.selftext

    d["post_info"] = p

def comment_to_dict(d, comment):
    c = {}
    a = {}

    if hasattr(comment, 'author') and comment.author:       
        if hasattr(comment.author, 'id'):
            a["id"] = comment.author.id
        if hasattr(comment.author, 'name'):
            a["name"] = comment.author.name
        if hasattr(comment.author, 'created_utc'):
            a["user_created"] = to_utc(comment.author.created_utc)
        if hasattr(comment.author, 'has_verified_email'):
            a["verified"] = str(comment.author.has_verified_email)
        if hasattr(comment.author, 'is_employee'):
            a["employee"] = str(comment.author.is_employee)
        if hasattr(comment.author, 'is_mod'):
            a["mod"] = str(comment.author.is_mod)

    c["comment_author"] = a

    if hasattr(comment, 'id'):
        c["id"] = comment.id
    if hasattr(comment, 'comment_created'):
        c["comment_created"] = to_utc(comment.created_utc)
        print(c["comment_created"])
    if hasattr(comment, 'body'):
        c["comment"] = comment.body
    if hasattr(comment, 'post_author'):
        c["post_author"] = str(comment.is_submitter)
    if hasattr(comment, 'comment_link'):
        c["comment_link"] = comment.permalink
    if hasattr(comment, 'subreddit_id'):
        c["subreddit_id"] = comment.subreddit_id

    d["comment_info"] = c

def reddit_to_json(d):
    if d:
        return json.dumps(d)
    return None