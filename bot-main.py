import praw
import config
import time
import os
import requests
import random
import datetime
import json
import re
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
    time.sleep(2)
    return r

def run(r, saved_list, some_list):
    for comment in r.subreddit(easy).comments(limit=500):
        if "gimme" in comment.body and comment.id not in replied_list and comment.author != r.user.me():
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


# main body


def post_recog(easy, upv1, n, switch):
    for submission in r.subreddit(easy).top(limit=10):
        if submission.id in post_list:
            continue
        while True:
            title_digits = re.findall('\\d+', submission.title)
            all_title_digits.extend(title_digits)

            if all_title_digits == '':
                switch = 1
                continue
            if switch == 1:
                switch = 0
                break
            else:
                combined_digits = ''.join(str(e) for e in all_title_digits[-1])
                ints = int(combined_digits)
                time.sleep(20)
                break

        if bool(re.search('\\d+', submission.title)):
            if submission.score >= ints:
                img_today = submission.url
                submission.mod.flair('Slain!')

                # r.subreddit(easy).submit(title_names[random.randint(0,9)], url = img_today)
                post_list.append(submission.id)
                # n = n + 1
                with open ("list2.txt", "a") as f:
                    f.write(submission.id + "\n")
                    print("submission filter updated")
            if submission.score != ints and submission.id not in post_list:
                submission.mod.flair(f'{submission.score}/{ints} You\'re nearly there. Keep upvoting!')
                print('challenge flair assigned')

            time.sleep(25)
                
# timer

            
# divider

def replymesg():
    for message in r.inbox.messages(limit=50):
        if "halfling" in message.subject.lower() and message.id not in mesg_list:
            for flair in r.subreddit(easy).flair(redditor=message.author):
                
                if 'Halfling' in str(flair):
                    print(message.id)
                    r.redditor(message.author.name).message('Hello Halfing! You\'ll be added soon.', 'Dumb, slow mods amirite?')
                    r.redditor('VirtuousVermin').message(message.author, f'u/{message.author} is a halfling')
                    r.redditor('blokkiesam').message(message.author, f'u/{message.author} is a halfling')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")  
                
                if 'Halfling' not in str(flair):
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
                    r.redditor('VirtuousVermin').message(message.author, f'u/{message.author} is an orc')
                    r.redditor('blokkiesam').message(message.author, f'u/{message.author} is an orc')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                
                if 'Orc' not in str(flair):
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
                    r.redditor('VirtuousVermin').message(message.author, f'u/{message.author} is an elf')
                    r.redditor('blokkiesam').message(message.author, f'u/{message.author} is an elf')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                
                if 'Elf' not in str(flair):
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
                    r.redditor('VirtuousVermin').message(message.author, f'u/{message.author} is a dwarf')
                    r.redditor('blokkiesam').message(message.author, f'u/{message.author} is a dwarf')
                    mesg_list.append(message.id)
                    with open ("list3.txt", "a") as f:
                        f.write(message.id + "\n")
                        print("message filter updated")
                
                if 'Dwarf' not in str(flair):
                    r.redditor(message.author.name).message('Liar!', f'You\'re not an Dwarf!')
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
title_names = ['We have been saved by your upvotes once again!', 'Never fear, the valiant warriors of r/kickopenthedoor have saved us!', 'Congratulations. Take a vacation, you deserve it', 'Sponsored by Audible', 'Begone, thot!', 'You can never break us!', 'yeet you did it', 'who the hell downvoted it', 'these look like genuine posts but its all the government', 'good']

easy = 'kickopenthedoor'


img_today = "https://i.redd.it/wr880nydoiw11.jpg"
upv1 = "40"
upv2 = "60"
all_title_digits = []
n = 1
switch = 0

r = login()
replied_list = saved_list()
post_list = list2()
mesg_list = list3()
while True:
   run(r, saved_list,  some_list)
   post_recog(easy, upv1, n, switch)
   replymesg()
   time.sleep(7)

subreddit = r.subreddit(easy)
