import json
from requests import get


def cadidates_json():
  url = "https://pastebin.com/raw/DrBxQQBw"
  response = get(url).text
  json_load = json.loads(response)
  return json_load


candidates = cadidates_json()


