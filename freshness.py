#!/usr/bin/env python3

import sqlite3


def createCheck():
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tbl_sequence(last_tweet INTEGER)")
        conn.commit()
    c.close()
    conn.close()
    setLtweet()


def setLtweet():
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c, count = countRecords(c)
        if count < 1:
            # lTweet = id
            # c.execute("INSERT INTO tbl_sequence (last_tweet) VALUES (?)", (id,))
            # conn.commit()
            return -1
        else:
            c.execute("SELECT * FROM tbl_sequence ORDER BY last_tweet DESC LIMIT 1")
            lTweet = c.fetchone()[0]
            return lTweet
    c.close()
    conn.close()


def countRecords(c):
    count = ""
    c.execute("SELECT COUNT(*) FROM tbl_sequence")
    count = c.fetchone()[0]
    return c, count


def logLtweet(id):
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c.execute("UPDATE tbl_sequence SET last_tweet = (?)", (id,))
        conn.commit()
    c.close()
    conn.close()

