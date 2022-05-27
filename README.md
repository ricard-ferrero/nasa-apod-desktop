# NASA APOD

A dekstop application in Python connected with a NASA's API named [APOD (Astronomy Picture of the Day).](https://apod.nasa.gov/apod/astropix.html)

Everyday is published an amazing photograph about the universe and our precious sky. This app connects directly with APOD and shows you his picture quickly without having to open the browser.

I recommend to use the app as a startup application: everyday when you turn on your computer you will start with the Astronomy Picture of the Day before your routine work.

Enjoy it!

## About API Key

When working with [NASA Open APIs](https://api.nasa.gov/) it is essential to use an API Key. To get one es free and really easey (only needs to send your name and your email adress), but also can use the "DEMO_KEY" if you prefer.

This is the [original stract from the web](https://api.nasa.gov/#authentication):
> ### Authentication
> You do not need to authenticate in order to explore the NASA data. However, if you will be intensively using the APIs to, say, support a mobile application, then you should sign up for a NASA developer key.
> #### DEMO_KEY Rate Limits
> In documentation examples, the special DEMO_KEY api key is used. This API key can be used for initially exploring APIs prior to signing up, but it has much lower rate limits, so you’re encouraged to signup for your own API key if you plan to use the API (signup is quick and easy). The rate limits for the DEMO_KEY are:
> * Hourly Limit: 30 requests per IP address per hour
> * Daily Limit: 50 requests per IP address per day

In this repository I used the DEMO_KEY (app.py, line 6): `arg = {'api_key': 'DEMO_KEY'}`. Feel free to change it if you need it!
