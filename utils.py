import json


def load_candidates() -> list[dict]:
    """загрузка данных из файла"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates = json.load(file)
        return candidates


def load_candidates_from_json() -> list[dict]:
    """покажет всех кандидатов"""
    return load_candidates()


def get_candidate_by_pk(pk: int) -> dict | None:
    """вернет кандидата по id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if candidate['id'] == pk:
            return candidate
    return None


def get_candidates_by_name(name: str) -> list[dict]:
    """вернет кандидатов по навыку"""
    result = []
    for candidate in load_candidates_from_json():
        if name.lower() in candidate['name'].lower():
            result.append(candidate)

    return result


def get_candidates_by_skill(skill: str) -> list[dict]:
    """вернет кандидатов по навыку"""
    candidates = load_candidates_from_json()
    result = []
    for candidate in candidates:
        if skill in candidate['skills'].lower().split(', '):
            result.append(candidate)

    return result
