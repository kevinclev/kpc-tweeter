# kpc-tweeter
The P Stands For Python!

# What is this?
A simple Python script that will tweet out what the **P** stands for in `Kevin P Cleveland` based on a list of definitions in `definitions.txt`.

# How does this work?
Right now I have the script running on a cronjob for every three hours. The script uses the Python module `tweepy` to interact with the twitter api to send tweets to the [Kevin P Cleveland](https://twitter.com/KevinPCleveland) twitter account.

# Contributing
I encourage anyone to add a definition to `definitions.txt` as long as it meets the following requirements.
* Word must start with a P.
* Word must not be a duplicate.

Submit a PR and I'll review it and decide if it is worthy or not to be what the **P** stands for.

As for code changes and such, just make sure you follow Python best practices and test your code (will probably add automated tests in the future). Submit a PR and I will review it accordingly.

# Why?
Idk. I wanted to make something that interacted with the Twitter API and thought that an old inside joke would make a good use case for this.
