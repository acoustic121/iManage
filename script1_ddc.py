import pandas as pd
data1=pd.read_excel("s1_client.xlsx")
data2=pd.read_excel("s1_deepcheck_new2.xlsx")
s1=data1["client_id"]
client_list=list(s1)
s2=data2["server"]
ddc_list=list(s2)
final_list=[]
for i in client_list:
    for j in ddc_list:
        if i==j:
            final_list.append(i)
df = pd.DataFrame(final_list)
writer = pd.ExcelWriter('s1_ddc_avail.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()            
main_list=[]
main_list = list(set(ddc_list) - set(client_list))
df = pd.DataFrame(main_list)
writer = pd.ExcelWriter('not live or not Prod or both but ddc present.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
great_list=[]
great_list = list(set(client_list) - set(ddc_list))
df = pd.DataFrame(great_list)
writer = pd.ExcelWriter('live but ddc not present.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='welcome', index=False)
writer.save()
