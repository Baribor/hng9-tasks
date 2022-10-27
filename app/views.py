from django.http import JsonResponse, HttpRequest


def get_user(_: HttpRequest):
    
    bio = '''Hi, I am Baribor Saturday most people prefer calling me Barry.
I am an undergraduate in the department of Computer Engineering and I find coding a thing of interest. I am optimistic, a good team player and an avid learner.'''
    
    user_data = {'slackUsername':'saturdaybaribor', 'backend':True, 'age':24, 'bio':bio}
    
    return JsonResponse(user_data)



    