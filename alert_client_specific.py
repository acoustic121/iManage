import pandas as pd
data1=pd.read_excel("alert_list.xlsx")
s=data1["Alert Message"]
message_list=list(s)
sentence_split_list=[]
for x in message_list:
    sentence_split_list.append(x.split())
filtered_list=[]
for x in sentence_split_list:
    if "REALERT" not in x and "New,ticket" not in x:
        filtered_list.append(x)
with open("client_id.txt", "r") as f:
    keywords = f.readlines()
    keywords = [keyword.strip() for keyword in keywords]
  
# printing the data
#print(data_into_list)
my_file.close()
for i in keywords:
    for j in filtered_list:  
        if i in j:
            string3= '*'+i
            j.append(string3)
final_list=[]
for x in filtered_list:
    final_list.append(','.join(x))
df = pd.DataFrame(final_list)
writer = pd.ExcelWriter('result3.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()             
 