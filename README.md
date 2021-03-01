****Reddit Flair Detection using Reddit API****

**Problems - Reddit Flare Detection**

**Part I - Reddit Data Collection**
Wrote a script to collect data from r/india subreddit. This data would be used in future parts of the problem to build the classifier. 

**Part II - Exploratory Data Analysis (EDA)**
Performed EDA on the data collected in Part I. This is helpful for understanding the data you have collected. Explain in detail about the analysis you did, intuition behind doing it, output of the analysis (in terms of graphs or tables), your inference from the output and how it shapes your future system decisions.

**Part III - Building a Flare Detector**
Posts in r/india can be corresponding to multiple topics. Each post is tagged for filtering purposes. These tags are called a flares in the reddit world. r/india has flairs like Politics, AskIndia, Science/Technology etc. Built a classifier which can predict the flare of a reddit post. Used data collected in Part I as training and validation data. 

(Detailed steps are present in the Jupyter Notebooks)

**Part IV - Building a Web Application**
Built a web application which can be used to detect Flare of a r/india post. The Application has an input field which expects a link to a reddit post from r/india. On submission it scrapes out the flare of the post.

**Part V - Deployment**
Deployed the web application built in Part IV on Heroku.

Web Application deployed on Heroku: https://cherryflair.herokuapp.com/

**Working of the Web Application:**
- Put in the URL of a subreddit post.
- The Web Application will return the flair of the subreddit post, by scraping the web using Reddit API.
