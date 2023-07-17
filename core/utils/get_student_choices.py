def get_student_choices(post):
    choices = []
    choice = {}
    for obj in post:
        if 'question' in obj:
            choice['question'] = post[obj]
        if 'choosen' in obj:
            choice['choosen'] = post.getlist(obj)
            choices.append(choice)
            choice = {}
    return choices