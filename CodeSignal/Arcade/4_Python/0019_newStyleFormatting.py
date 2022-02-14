def solution(s):
    a = re.sub('%%', '{%}', s)
    b = re.sub('%[dfFgeEGnnxXodcbs]', '{}', a)
    return re.sub('{%}','%',b)