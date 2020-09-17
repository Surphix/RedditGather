import praw, os
from dotenv import load_dotenv
from .produce import produce_k
from .analysis import analysis_s
from .map import submission_to_dict, comment_to_dict, reddit_to_json

def display_author(comment):
    if comment.author:
        return comment.body

class gather(produce_k, analysis_s):
    def __init__(self, args):  
        load_dotenv()
        produce_k.__init__(self, int(os.getenv("FLUSH_LIMIT")),
                                 os.getenv("BOOTSTRAP_SERVER"))
        analysis_s.__init__(self, 'en')
        self.keyword = args.k
        self.limit = args.l
        self.reddit = praw.Reddit(client_id=os.getenv("C_ID"),
                                  client_secret=os.getenv("C_SECRET"),
                                  user_agent=os.getenv("U_AGENT"),
                                  username=os.getenv("USERNAME"),
                                  password=os.getenv("PASSWORD"))

    def post_metadata(self, post):
        
        obj = {}

        obj["post_score"] = self.analyze(post.title)
        submission_to_dict(obj, post)

        post.comments.replace_more(limit=10)
        for comment in post.comments.list():
            if comment.body:
                obj["comment_score"] = self.analyze(comment.body)

            comment_to_dict(obj, comment)
            self.send('reddit', reddit_to_json(obj))
            
    def get_posts(self, search):
        return self.reddit.subreddit("all").search(search, limit=self.limit)

    def launch(self):
        submission = self.get_posts(self.keyword)
        for p in submission:
            self.post_metadata(p)
