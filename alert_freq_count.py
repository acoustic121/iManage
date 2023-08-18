import pandas as pd
data=pd.read_excel("week13,14.xlsx")
s=data['Ticket subject']#taking only the alert message column into consideration  
lst = list(s)#making a new list and converting the object s into a list

lkd=[]
for x in lst:
    lkd.append(x.split()[0:11]) #taking only the first 5 words from each row of the column

lmn=[]
for x in lkd:
    lmn.append(','.join(x))#removing the extra brackets from each row

newword2=[]
for x in lmn:
    if 'REALERT' not in x and 'New,ticket:' not in x:#removing all the realerts and new tickets
        newword2.append(x)

#making  a dictionary freq        
freq = {} 
for item in newword2: 
    if (item in freq): 
        freq[item] += 1
    else: 
        freq[item] = 1
for key,value in freq.items(): 
    print ("% s : % s"%(key, value)) //counting using dictionary
            
        
df = pd.DataFrame(data=freq,index=[0])
df = (df.T)
print(df)
df.to_excel('week13,14list.xlsx') 
