import praw
import config
import time
import os
import requests
import random
print("not deporting the flares")


def login():
    print("haxing the webs")
    r = praw.Reddit(username = config.username,
                password = config.password,
                client_id = config.client_id,
                client_secret = config.client_secret,
                user_agent = 'Upvote and fighter bot for r/kickdownthedoor.',
                )
    print("logged on")
    return r

def run(r, saved_list, some_list):
    for comment in r.subreddit(easy).comments(limit=500):
        if "gimme class" in comment.body and comment.id not in replied_list and comment.author != r.user.me():
            print("making sure this isn't deja vu...")
            print("giving flairs")
            r.subreddit(easy).flair.set(comment.author, some_list[random.randint(0,3)])
            print("flairs gimmied")
            comment.reply("class gimmied")
            print("replied, id is" + comment.id)

            replied_list.append(comment.id)


            with open ("list.txt", "a") as f:
                f.write(comment.id + "\n")
                print("do not call list updated")


            print("not getting ratelimited...")
            time.sleep(3)


def post_recog(easy, upv1):
    for submission in r.subreddit(easy).new(limit=20):
        if upv2 in submission.title and submission.id not in post_list:

            if submission.score >= 55:
                print("removing the post")
                submission.mod.flair('Complete!')
                submission.mod.remove()

                r.subreddit(easy).submit('We have been saved by your upvotes once again!', url = img_today)
                post_list.append(submission.id)
                with open ("list2.txt", "a") as f:
                    f.write(submission.id + "\n")
                    print("submission filter updated")
            else:
                submission.mod.flair('You\'re nearly there. Keep upvoting!')


        if upv1 in submission.title and submission.id not in post_list:

            if submission.score >= 60:
                print("removing the post")
                submission.mod.flair('Complete!')
                submission.mod.remove()
                print('posting...')
                r.subreddit(easy).submit('We have been saved by your upvotes once again!', url = img_today)
                post_list.append(submission.id)
                with open ("list2.txt", "a") as f:
                    f.write(submission.id + "\n")
                    print("submission filter updated")  
            else:
                submission.mod.flair('You\'re nearly there. Keep upvoting!')


            

            
            


def saved_list():
    with open("list.txt", "r") as f:
        replied_list = f.read()
        replied_list = replied_list.split()
    return replied_list


def list2():
    with open("list2.txt", "r") as f:
        post_list = f.read()
        post_list = post_list.split()
    return post_list


some_list = ['Halfling', 'Dwarf', 'Elf', 'Orc']


easy = 'kickopenthedoor'


img_today = "https://i.redd.it/wopzm2sdi9l11.jpg"
upv1 = "60"
upv2 = "55"

r = login()
replied_list = saved_list()
post_list = list2()
while True:
   run(r, saved_list,  some_list)
   post_recog(easy, upv1)

subreddit = r.subreddit(easy)









