
pyrebase_config = {
    # Add this file to gitignore on the addition of apiKey
    "apiKey" : None,
    "authDomain": None,
    "databaseURL" : "https://swhacksfirebase.firebaseio.com",
    "storageBucket" : None
}

pyrebase_paths = {
    "temperature"       : "Temperature/value",
    "temperature_time"  : "Temperature/time",
    "feed"              : "FeedStatus/feed",
    "feed_acknowledge"  : "FeedStatus/feed_acknowledge",
    "feed_time"         : "FeedStatus/last_feed_time",
    "last_date_fed"     : "FeedStatus/feedings_today/date",
    "feedings_today"    : "FeedStatus/feedings_today/value"

}
