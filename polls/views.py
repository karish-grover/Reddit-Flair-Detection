from django.shortcuts import render
from django.http import HttpResponse, request
from .forms import RedditForm

import praw
import pandas as pd
import csv
import os

redditObject= praw.Reddit(client_id= os.environ.get("CLIENT_ID"),client_secret=os.environ.get("CLIENT_SECRET"), user_agent=os.environ.get("USER_AGENT"),user_name=os.environ.get("USER_NAME"),password=os.environ.get("PASSWORD"))

subredditObject= redditObject.subreddit("india")  #scrapping data from subreddit --> r/india



def index(request):

	submitted=False
	if request.method=='POST':
		form=RedditForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			SUBMISSION=redditObject.submission(url=cd['url'])# Creating a submission object
			flair=SUBMISSION.link_flair_text
			form=RedditForm()
		
		arguments={'form':form ,'text':"The Flair of the above post is :", 'flair':flair}

	else:
		form=RedditForm()
		if 'submitted' in request.GET:
			submitted=True
			form=RedditForm()
		arguments={'form':form }

	return render(request,"main.html",arguments)
		





	

