import praw
import config
import time
import os
import requests
import random
import datetime
import json
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
        if "gimme" in comment.body and comment.id not in replied_list and comment.author != r.user.me():
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

            if submission.score >= 100:
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

                
            date = datetime.datetime.fromtimestamp(submission.created_utc)
            dif = datetime.datetime.utcnow() - date
            if dif >= datetime.timedelta(days=1):
                print('ran out of time')
                submission.mod.flair('C\'mon guys! We failed!')
                submission.mod.remove()
               
 # divider

        if upv1 in submission.title and submission.id not in post_list:

            if submission.score >= 70:
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
                submission.mod.flair('You\'re nearly there. Keep upvoting! {submission.score}/{upv1}')
                
                
            if dif >= datetime.timedelta(days=1):
                print('ran out of time')
                submission.mod.flair('C\'mon guys! We failed!')
                submission.mod.remove()

# divider

def replymesg():
    for message in r.inbox.messages(limit=50):
        if "halfling" in message.subject.lower() and message.id not in mesg_list:
            for flair in r.subreddit(easy).flair(redditor=message.author):
                
                if 'Halfling' in str(flair):
                    print(message.id)
                    r.redditor(message.author.name).message('Hello Halfing! You\'ll be added soon.', 'Dumb, slow mods amirite?')
                    r.redditor('VirtuousVermin').message(message.author, 'u/{message.author} is a halfling')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  
                else:
                    r.redditor(message.author.name).message('Liar!', 'You\'re not an Halfling!')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  


        if "orc" in message.subject.lower() and message.id not in mesg_list:
            for flair in r.subreddit(easy).flair(redditor=message.author):
                
                if 'Orc' in str(flair):
                    print(message.id)
                    r.redditor(message.author.name).message('Hello Orc! You\'ll be added soon.', 'Dumb, slow mods amirite?')
                    r.redditor('VirtuousVermin').message(message.author, 'u/{message.author} is an orc')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                else:
                    r.redditor(message.author.name).message('Liar!', 'You\'re not an Orc!')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  

        if "elf" in message.subject.lower() and message.id not in mesg_list:
            for flair in r.subreddit(easy).flair(redditor=message.author):
                
                if 'Elf' in str(flair):
                    print(message.id)
                    r.redditor(message.author.name).message('Hello Elf! You\'ll be added soon.', 'Dumb, slow mods amirite?')
                    r.redditor('VirtuousVermin').message(message.author, 'u/{message.author} is an elf')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                else:
                    r.redditor(message.author.name).message('Liar!', 'You\'re not an Elf!')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  

        if "dwarf" in message.subject.lower() and message.id not in mesg_list:
            for flair in r.subreddit(easy).flair(redditor=message.author):
                
                if 'Dwarf' in str(flair):
                    print(message.id)
                    r.redditor(message.author.name).message('Hello Dwarf! You\'ll be added soon.', 'Dumb, slow mods amirite?')
                    r.redditor('VirtuousVermin').message(message.author, 'u/{message.author} is a dwarf')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                else:
                    r.redditor(message.author.name).message('Liar!', 'You\'re not an Dwarf!')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  


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


def list3():
    with open("list3.txt", "r") as f:
        mesg_list = f.read()
        mesg_list = mesg_list.split()
    return mesg_list



some_list = ['Halfling', 'Dwarf', 'Elf', 'Orc']

easy = 'kickopenthedoor'


img_today = "https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwj-qZSG97DdAhVI7qwKHW4RAhYQjRx6BAgBEAU&url=https%3A%2F%2Fsteamcommunity.com%2Fsharedfiles%2Ffiledetails%2F%3Fid%3D952828429&psig=AOvVaw0r0iDJCGUPMIG_QanKfz28&ust=1536685853042357"
upv1 = "70"
upv2 = "101"

r = login()
replied_list = saved_list()
post_list = list2()
mesg_list = list3()
while True:
   run(r, saved_list,  some_list)
   post_recog(easy, upv1)
   replymesg()
   time.sleep(3)

subreddit = r.subreddit(easy)
