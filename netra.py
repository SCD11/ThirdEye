import os
import io
import praw

class Netra:
    def __init__(self):
        self.keywords = open("./data/keywords.txt",'r')
        self.comments_db = open("./data/comments_db.txt",'r')
        self.reddit = praw.Reddit(client_id='_iYVx0uUOjcC4Q',
                     client_secret="77Ecib9fqsMXiADU8OnA5L0KVJc",
                     user_agent='MY USER AGENT')
        self.temp_comments_db = open("./data/temp_comments_db.txt","w")

    def get_info(self):
        self.subreddit_name = input("Enter the name of the subreddit : ")
        self.subreddit = self.reddit.subreddit(self.subreddit_name)
        self.submission_limit = int(input("Enter the number of posts you want to fetch : "))
        self.category = input("hot/rising/controversial/new ? ").lower()
        if self.category == "hot":
            self.hot_submissions()
        elif self.category == "new":
            self.new_submissions()
        elif self.category == "rising":
            self.rising_submissions()
        elif self.category == "controversial":
            self.controversial_submissions()
        else:
            print("Wrong Input")
            
    def hot_submissions(self):
        with io.open("./output/hot/hot.txt","w",encoding="utf-8") as f:
            for submission in self.subreddit.hot(limit=self.submission_limit):
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if self.comment_present(str(comment)):
                        print("true")
                        continue
                    else:
                        # print("1 and half truth")
                        if self.check_comment(comment.body):
                            # print("mega true")
                            self.temp_comments_db.write((str)(comment)+"\n")
                            f.write('COMMENT : "' + comment.body + '"\n')
                            f.write('LINK : "' + submission.url+str(comment)+'"\n\n\n' + '='*165+'\n\n\n' )
    
    def new_submissions(self):
         with io.open("./output/new/new.txt","w",encoding="utf-8") as f:
            for submission in self.subreddit.new(limit=self.submission_limit):
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if self.comment_present(str(comment)):
                        print("true")
                        continue
                    else:
                        # print("1 and half truth")
                        if self.check_comment(comment.body):
                            # print("mega true")
                            self.temp_comments_db.write((str)(comment)+"\n")
                            f.write('COMMENT : "' + comment.body + '"\n')
                            f.write('LINK : "' + submission.url+str(comment)+'"\n\n\n' + '='*165+'\n\n\n' )

    def rising_submissions(self):
         with io.open("./output/rising/rising.txt","w",encoding="utf-8") as f:
            for submission in self.subreddit.rising(limit=self.submission_limit):
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if self.comment_present(str(comment)):
                        print("true")
                        continue
                    else:
                        # print("1 and half truth")
                        if self.check_comment(comment.body):
                            # print("mega true")
                            self.temp_comments_db.write((str)(comment)+"\n")
                            f.write('COMMENT : "' + comment.body + '"\n')
                            f.write('LINK : "' + submission.url+str(comment)+'"\n\n\n' + '='*165+'\n\n\n' )

    def controversial_submissions(self):
         with io.open("./output/controversial/controversial.txt","w",encoding="utf-8") as f:
            for submission in self.subreddit.hot(limit=self.submission_limit):
                submission.comments.replace_more(limit=None)
                for comment in submission.comments.list():
                    if self.comment_present(str(comment)):
                        print("true")
                        continue
                    else:
                        # print("1 and half truth")
                        if self.check_comment(comment.body):
                            # print("mega true")
                            self.temp_comments_db.write((str)(comment)+"\n")
                            f.write('COMMENT : "' + comment.body + '"\n')
                            f.write('LINK : "' + submission.url+str(comment)+'"\n\n\n' + '='*165+'\n\n\n' )

    def comment_present(self,comment_str_id):
        comment_str_id = comment_str_id.lower()
        self.comments_db.seek(0)
        while(True):
            comment_id = self.comments_db.readline()
            comment_id = comment_id.strip()
            if comment_str_id == comment_id:
                return True
            if comment_id == "":
                break
        return False
            

    def check_comment(self,comment_val):
        self.keywords.seek(0)
        comment_val = comment_val.lower()
        while True:
            keyword = self.keywords.readline()
            keyword = keyword.strip()
            keyword = keyword.lower()
            if comment_val.find(keyword)>=0 and keyword!="":
                return True
            if keyword =="":
                break
        return False


    def close_All(self):
        self.keywords.close()
        self.comments_db.close()
        self.temp_comments_db.close()
        self.doTheNeedFull()

    def doTheNeedFull(self):
        temp_comments_db = open("./data/temp_comments_db.txt","r")
        comments_db = open("./data/comments_db.txt",'a')
        while True:
            data_line = temp_comments_db.readline()
            if data_line =="":
                break
            comments_db.write(data_line)
        temp_comments_db.close()
        comments_db.close()   

def main():
    thirdEye = Netra()
    thirdEye.get_info()
    thirdEye.close_All()


if __name__ == "__main__":
    main()