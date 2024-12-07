# apify doc: https://docs.apify.com/api/client/python/docs
# actor doc: https://apify.com/apidojo/tweet-scraper

from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("TOKEN")

# Prepare the Actor input
run_input = {
    "customMapFunction": "(object) => { return {...object} }",
    "end": "2024-12-07",
    "includeSearchTerms": False,
    "maxItems": 20,
    "minimumFavorites": 0,
    "minimumReplies": 0,
    "minimumRetweets": 0,
    "onlyImage": False,
    "onlyQuote": False,
    "onlyTwitterBlue": False,
    "onlyVerifiedUsers": False,
    "onlyVideo": False,
    "sort": "Latest",
    "start": "2020-12-01",
    "tweetLanguage": "ru"
}

# Run the Actor and wait for it to finish
run = client.actor("61RPP7dywgiy0JPD0").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)