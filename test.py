from json_load_info_candidates import candidates


def skill_conditations(skill="No"):
    candidate_skills = []
    for candidates_skill in candidates:
        list_skill = candidates_skill.get("skills").lower().split(",")
        if skill in list_skill:
            candidate_skills.append(candidates[candidates_skill["id"] - 1])
    return candidate_skills
