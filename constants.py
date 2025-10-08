import tweepy

API_KEY="AIzaSyDlkxxjJmbjAHLF3_rfb4NgNiksbMrm2yc"
API_SECRET_KEY="181hPlUZWDRVZjYRrkHEQhZqGRv1P7PAs7G16lRuBdISsuLeZ1"
ACCESS_TOKEN="1463363707254177792-zaRTjxD2nHAZHFOGKNiVLxTgUffcza"
ACCESS_TOKEN_SECRET="8H1SoLzcO35rupu0JhMwyX9an0Iy22JaJK1Fm3cnW6KEq"
BEARER_TOKEN="AAAAAAAAAAAAAAAAAAAAANqM3gEAAAAAinuS5A1QvQGy%2Bq3RTjz4XEf%2BkDI%3D8pemVGrHZsMo6aaCoqP3cpxUboOZdYuF34waGCehquVmcA6al9"

twitterClient=tweepy.Client(
    bearer_token=BEARER_TOKEN,
    consumer_key=API_KEY,
    consumer_secret=API_SECRET_KEY,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET,
    wait_on_rate_limit=True,
)

