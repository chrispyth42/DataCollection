# DataCollection
Contains scripts that collect/aggregate data from various places across the internet


### getNews.py
Reads from multiple news outlets' RSS feeds, and places the news stories into a local SQLite database file. Created due to the absolute state of the news nowadays, with the election season coming up


### TwtterArchiver.py
Accepts a username for a twitter account, and archives as far back as ~3,200 tweets into an SQLite database file (As far back as twitter's mobile site allows apparently). It turns out, twitter's mobile site is surprisingly unrestricted; having all of the tweet data neatly stored in the HTML, a link to the next page of tweets at the bottom of each page, and seemingly no limit on the amount of requests they allow you to make per second (I did put a 1 second delay between requests though just to be sure). The database file schema is (OP TEXT, tweet TEXT, replyingTo TEXT, url TEXT, time TEXT).

This was created when I was less experienced with SQL, and I'll likely improve it if I ever come back to it
