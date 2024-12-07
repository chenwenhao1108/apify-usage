from apify_client import ApifyClient

# Initialize the ApifyClient with your API token
client = ApifyClient("TOKEN")

# Prepare the Actor input
run_input = {
  "customMapFunction": "(object) => { return {...object} }",
  "duration": "all",
  "features": "all",
  "getTrending": True,
  "gl": "ru",
  "hl": "ru",
  "includeShorts": False,
  "keywords": [
    "Владимир Владимирович Путин"
  ],
  "maxItems": 2,
  "sort": "r",
  "uploadDate": "all"
}

# Run the Actor and wait for it to finish
run = client.actor("1p1aa7gcSydPkAE0d").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)