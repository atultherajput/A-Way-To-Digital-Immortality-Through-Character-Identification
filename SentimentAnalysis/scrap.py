from fb_con import get_con

def fb_scrap():
    graph=get_con()
    i = input('Enter id of photo: ')
    r = input('Stream Comments(y/n): ')
    if r=='y':
        s='/stream'
    else:
        s=''
    x=graph.get('/'+i+'/comments'+s)
    return x
