# Crypto_Scraper

Here is the create table query for posts:

 Create table posts(                                                                                    
 	 post_id VARCHAR(20) not NUll key,
     text VARCHAR(2000),
     title VARCHAR(500),
     link VARCHAR(200),
     author VARCHAR(100),
     post_category VARCHAR(20),
     subreditName VARCHAR(20),
     downs INT,
     ups INT,
     score INT,
     commentsNumber INT,
     upVoteRatio float(2,2),
     timePosted DATE,
     media VARCHAR(500),
     pinned boolean);

