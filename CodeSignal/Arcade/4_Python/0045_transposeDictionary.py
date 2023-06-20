def solution(scriptByExtension):
    return sorted([[value, key] for key, value in scriptByExtension.vehicles()])
