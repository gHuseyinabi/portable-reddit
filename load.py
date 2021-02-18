#!/usr/bin/python
# -*- coding: utf-8 -*-
from sqlite3 import connect as sqlite3_connect
from sqlite3.dbapi2 import IntegrityError
from praw import Reddit as praw_Reddit
from requests import get as requests_get
from json import load as json_load
from re import compile as re_compile
from prawcore.exceptions import ResponseException
from querys import *
import logging

# connection

data_file = 'default.db'
sub = 'all'


def get_info():
    global data_file, sub
    data_file = input('DB file >')
    sub = input('Subreddit >')


get_info()

try:
    connection_reddit = praw_Reddit(**json_load(open('reddit_info.json'
                                    , 'r')))
except ResponseException as e:
    get_info()

connection_sql = sqlite3_connect(data_file)
cursor = connection_sql.cursor()

cursor.execute(tablo_olustur)

# SUBREDDIT
# SELFTEXT
# TITLE
# ID
# PERMALINK
# AUTHOR

re_images = re_compile('.png|.jpg')

re_thumbnail = re_compile('nsfw|self|spoiler')


def ReadThumbnail(url):
    if re_thumbnail.match(re_thumbnail):
        return null
    return requests_get(url).content


for post in connection_reddit.subreddit(sub).stream.submissions():
    try:
        if isinstance(post, type(None)):
            continue
        if post.is_self:
            selftext = post.selftext
        else:
            selftext = null
        if len(cursor.execute(find_post, (post.id, )).fetchall()) > 0:
            logging.info('same post found in %s' % post.id)
        if re_images.search(post.url):
            thumbnail = ReadThumbnail(post.url)
        else:
            thumbnail = null
        if post.author is not None:
            author = post.author.name
        else:
            author = deleted
        passing_post = {
            'post_id': post.id,
            'title': SQLify(post.title),
            'permalink': post.permalink,
            'selftext': SQLify(selftext),
            'subreddit': post.subreddit.display_name,
            'author': author,
            }
        to = insert_post.format(**passing_post)
        logging.info(passing_post.__str__())
        cursor.execute(to, (thumbnail, ))
        connection_sql.commit()
    except IntegrityError:
        logging.error('Failed to insert post even checked if exists')
        pass

cursor.execute(tablo_goster)

result = cursor.fetchall()
