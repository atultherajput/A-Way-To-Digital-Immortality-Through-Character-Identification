from textblob import TextBlob
from parse import send_parsed_data

data=send_parsed_data()
#print(data)
print('*'*80)

p=0
n=0
z=0

def count(c):
    global p,n,z
    if c>0:
        p=p+1
    elif c<0:
        n=n+1
    else:
        z=z+1

for each in range(len(data)):
    #print('Name: '+data[each][0]['name'])
    print('Message: '+data[each][1])
    testimonial = TextBlob(data[each][1])
    print(testimonial.sentiment)
    count(testimonial.sentiment.polarity)
    print('*'*80)
print('Total Positive Comments: '+str(p))
print('Total Negative Comments: '+str(n))
print('Total Neutral Comments: '+str(z))
    
