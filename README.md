# google_trend_downloader
Download CSV from Google Trend with providing keywords

1. Idea.
<u>Main Idea</u>

There is a download CSV button on the Google Trend page: Use Chrome Developer Tools to observe the request URL, following is an example of a download CSV request after decoding the URL:
<code>
/trends/api/widgetdata/multiline/csv?req={"time":"2015-01-01 2022-09-20","resolution":"MONTH","locale":"en-US","comparisonItem":[{"geo":{"country":"CA"},"complexKeywordsRestriction":{"keyword":[{"type":"BROAD","value":"bitcoin"}]}}],"requestOptions":{"property":"","backend":"IZG","category":0},"userConfig":{"userType":"USER_TYPE_LEGIT_USER"}}&token=APP6_UEAAAAAYytS4CECwnCcR55-V7JHz5v5FxtfmVwj&tz=420
</code>

Some useful parameters need to pay attention such as: 
+ tz: for timezone
+ time: for time frame, format: YYYY-MM-DD YYYY-MM-DD
+ geo: for providing country.
...

From now, just make a request with the above parameters then we can download the CSV. But there is a problem with the query parameter `token`. Is it changed every we visit the website or a fixed token? Does the `token` has to be provided or can be skip? I need to solve the problem before can build a download API.

<u>Secondary Solution: Don't try to reinvent the wheel</u>
Search around the Internet for an open-source and free-to-use library. And of course, there are many of them already available. Including `pytrends` provided in Python: homepage and download: <a>https://pypi.org/project/pytrends/</a>

See the source code for my demo using this library to download the trend of keyword 'bitcoin' from Jan 1, 2015 to Sep 20, 2020.

2. the amount of time you spent on finishing the program code (or pseudo code),
Around 30 minutes to inspect then Google Trend website and underlying HTTP request. And less then 15 minutes to write a demo using `pytrends` package

3. the different ways you have tried to approach the TECH ASSESSMENT, 

4. the reasons of settling on the current approach, and finally, 
Saving time to get the first output to archive the task enough to satisfy the business. Then we will have more time to improve and become a solid solution for long-term using
5. how to execute your program.
- Need to install python in the system
- Then run the main.py file: python3 main.py