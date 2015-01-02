import math

def railFence ( msg, height):
    partsize= height * 2-2
    parts= math.ceil( len(msg)/ partsize)
    res = ''

    #fisrt line

    for part in range(parts):
        res += msg[part * partsize + height -1]

    
    #middle line

    for line in range (height -2 ):
        for part in range (parts):
            res += msg[(height-2-line) + (part * partsize)]
            if height + line + part * partsize < len(msg):
                res += msg[ height + line + part *partsize]

    #last line

    for part in range(parts):
        res += msg[ part * partsize]
    return res

print("railFence", railFence\
      ('Send more reinforcements for the monkey-catching operation', 4))

