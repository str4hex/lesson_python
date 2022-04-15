from json_load_info_candidates import candidates


def skill_conditations(skill="No"):
    candidate_skills = []
    for candidates_skill in candidates:
        if skill in candidates_skill["skills"].lower():
            candidate_skills.append(candidates[candidates_skill["id"] - 1])
    return candidate_skills
