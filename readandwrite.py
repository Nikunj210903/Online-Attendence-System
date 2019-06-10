import json
import ast
def fun(dic,r):
    print("attendence..............",r)
    if not len(r['attendence']):
        return None
    
    #r = {'attendence':[1,45,23,76,23,56]}
    r = json.dumps(r)
    file_location=""   
   # branch="\CP"
   # year="\year-3"
    #sem="\Sem-6"
    #subject="\Java"
    #date='\date-01-01-2019'
    #time='11-00'
    branch="\\"+dic['branch']
    year="\\"+dic['year']
    sem="\\"+dic['sem']
    subject="\\"+dic['subject']
    date="\\date-"+dic['date']
    time=dic['time']
    file_location+="C:\\Users\\Nikunj\kunj\project\DE\Attendence\Attendence-2019"+""+branch+""+""+year+""+""+sem+""+subject+""+""+date+""+time+".txt"
    print(file_location)
    with open(file_location,"w") as data:
        data.write(r)


 
#dic={'branch':'CP','year':'year-3','sem':'Sem-6','subject_name':'C','date':'21-02-1019','time':'12-00'}
#fun(dic)
