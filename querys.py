#!/usr/bin/python
# -*- coding: utf-8 -*-
tablo_olustur = \
    '''CREATE TABLE IF NOT EXISTS 
posts(post_id VARCHAR(6) NOT NULL UNIQUE PRIMARY KEY,selftext TEXT,thumbnail BLOB,title TEXT,author TEXT,permalink TEXT)'''

null = 'NULL'

tablo_goster = 'SELECT * FROM posts'

insert_post = \
    '''INSERT INTO posts VALUES('{post_id}','{selftext}',?,'{title}','{author}','{permalink}')'''

deleted = 'u/[deleted]'

tablo_goster = 'SELECT * FROM posts'


def SQLify(query):
    return query.replace("'", "' + char(39) + '")


insert_post = \
    '''INSERT INTO posts VALUES('{post_id}','{selftext}',?,'{title}','{author}','{permalink}')'''

find_post = 'SELECT * FROM posts WHERE post_id=?'
