from data_extract import extract, send_data

p = send_data()
x=0
info=[]
for i in p:
    user,msg=extract(x)
    #print(str(user),msg)
    info.append((user,msg))
    #print(type(user)) <class 'dict'>
    #print(type(msg)) <class 'str'>
    x = x+1

def send_parsed_data():
    return info