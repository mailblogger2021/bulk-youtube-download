from TikTokApi import TikTokApi

# Starts TikTokApi
api = TikTokApi.get_instance()

# The Number of trending TikToks you want to be displayed
results = 30

# Returns a list of dictionaries of the trending object
trending = api.by_trending(results)

# Loops over every tiktok
for tiktok in trending:
    # Prints the text of the tiktok
    print(tiktok["desc"])

print(len(trending))