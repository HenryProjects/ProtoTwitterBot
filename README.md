# ProtoTwitterBot
First ever Twitterbot for Henry Projects--keeping it simple!
***
## Dependencies:
*tweepy

### Build history:
*The first build simply posted a random insult to its own wall, directing it @realdonaldtrump. This was the minimum viable product, and it was mainly so we could get something up and running on Heroku.

*The second build used a very simple (1 column, 1 row) Sqlite database to store the ID of Trump's last post. When it scraped, it would check the ID of the newest post against the one stored in the db, then if the newest post was different, it would reply to that with a random insult. Finally, it would replace the contents of the db with the new post. If the scraped post was not new, it would go back to sleep.

*For the third build, we discovered that Heroku does not play nicely with Sqlite (who knew?), and our db was getting wiped at least once every 24 hours. Our first inclination was to use PostgreSQL to store our 1-column, 1-row db, but this was a little overkill. Our second idea was to use the pickle library to create a small text file containing just the ID of the last post that Bard had replied to. The final, and more elegant, solution, was to simply do two scrapes: one to determine the ID of Bard's last post, and one to determine the ID of Trump's last post. If Trump's last post is newer than Bard's, then Bard replies to it.

