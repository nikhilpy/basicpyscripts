import pprint
lead = {'EmailID':'','Name':'','Number':'' ,'Location':'','Remark':''}
leadinfo = []
count = 0
while True:
    print('Enter the Email ID:')
    info = input()
    lead['EmailID'] = info
    print('Enter the Name:')
    info = input()
    lead['Name'] = info
    print('Enter the Number')
    info = input()
    while len(info)> 10 or len(info)< 9:
        print('Please enter valid mobile number')
        info=input()
    lead['Number']=info
    print('Enter the location')
    info=input()
    lead['Location']=info
    print('Enter the remarks:')
    info = input()
    lead['Remark']=info
    leads=list(lead.values())
    leadinfo.append(leads)
    print('Do you want to add a new entry?Y/N')
    conf=input()
    conf=conf.upper()
    if conf == 'Y':
        print('You selected option ' +conf)
        count+=1
        if count==10:
            print('You have done '+count+' calling today') 
            break
    elif conf == 'N':
        break
pprint.pprint(leadinfo)
    





        
        
    
