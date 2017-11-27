from scrap import fb_scrap

datas = fb_scrap()
p=datas['data']

def extract(x):
    return (p[x]['id'],p[x]['message']) #id<=>from

def send_data():
    return p
