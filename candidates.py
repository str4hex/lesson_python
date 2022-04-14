import json

from requests import get


def cadidates_json():
    url = "https://pastebin.com/raw/DrBxQQBw"
    response = get(url).text
    json_load = json.loads(response)
    return json_load


json_candidates = cadidates_json()


def candidates_all(id):
    return "candidates all"


def candidates(id):
    for id_candidates in json_candidates:
        if id_candidates.get("id") == id:
            return f"<img src='{id_candidates.get('picture')}'> \n<pre>\nИмя кандидата -{id_candidates.get('name')} " \
                   f"\nПозиция кандидата - {id_candidates.get('position')} \nНавыки через запятую - " \
                   f"{id_candidates.get('skills')} \n</pre>"
        elif id > len(json_candidates):
            return "Пользователь не найден"


def candidates_skills(skill):
    for id_candidates in json_candidates:
        if skill.lower() in id_candidates.get("skills").lower():
            return f"<img src='{id_candidates.get('picture')}'> \n<pre>\nИмя кандидата -{id_candidates.get('name')} " \
                   f"\nПозиция кандидата - {id_candidates.get('position')} \nНавыки через запятую - " \
                   f"{id_candidates.get('skills')} \n</pre>"
        else:
            return "Пользователь не найден"
