#!/usr/bin/env python3
import sqlite3


def create_check():
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c.execute("CREATE TABLE IF NOT EXISTS tbl_sequence(last_tweet INTEGER)")
        conn.commit()


def set_ltweet():
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c, count = count_records(c)
        if count < 1:
            c.execute("INSERT INTO tbl_sequence (last_tweet) VALUES (1)")
            conn.commit()
            return -1
        else:
            c.execute("SELECT * FROM tbl_sequence ORDER BY last_tweet DESC LIMIT 1")
            last_tweet = c.fetchone()[0]
            return last_tweet


def count_records(c):
    c.execute("SELECT COUNT(*) FROM tbl_sequence")
    count = c.fetchone()[0]
    return c, count


def log_ltweet(last_id):
    print(last_id)
    conn = sqlite3.connect("tweet_sequence.db")
    with conn:
        c = conn.cursor()
        c.execute("UPDATE tbl_sequence SET last_tweet = ?", (last_id,))
        conn.commit()
    c.close()
    conn.close()
