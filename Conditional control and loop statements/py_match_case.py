"""
The object after match will be matched with the content after case in turn,
if the match is successful, the matched expression is executed, otherwise skip directly,
_ can match everything

case _: Similar to default: in C and Java, when other cases cannot be matched,
match this one, and it is guaranteed that the match will always succeed
"""

'''
match object:
    case <pattern_1>:
        action_1
    case <pattern_2>:
        action_2
    case _:
        action_3
'''
def http_error(status):
    match status:
        case 400:
            return 'Bad request'
        case 404:
            return 'Not found'
        case 418:
            return 'I am a teapot'
        case _:
            return 'Something is wrong with the internet'
my_status=400
print(http_error(my_status))
# The above is an example of outputting an HTTP status code
# A case can also set multiple match conditions, separated by a | space, for example:
'''case 400|404|418:
      return 'Not found'
'''