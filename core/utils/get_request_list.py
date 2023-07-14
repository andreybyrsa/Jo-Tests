def get_request_list(post):
    d = {
        'questions': [],
        'points': [],
        'answers': [],
        'rightAnwers':[],
        'max_points': 0,
        'count': 0
    }
    for key in post.keys():
        if 'question' in key:
            d['questions'].append(post.getlist(key)[0])
            d['count'] += 1
        elif 'points' in key:
            d['points'].append(int(post.getlist(key)[0]) if post.getlist(key)[0] != '' else 0)
            d['max_points'] += int(post.getlist(key)[0]) if post.getlist(key)[0] != '' else 0
        elif 'answer' in key:
            d['answers'].append(post.getlist(key))
        elif 'right' in key:
            d['rightAnwers'].append(post.getlist(key))
    print(d)
    return d