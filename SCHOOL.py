import csv
def wcsv(z):
    with open('student_info.csv','a',newline='')as csv_file:
        
        writer=csv.writer(csv_file)
        if csv_file.tell()==0:
            writer.writerow("Name","Age","Contact number","Email ID")
        writer.writerow(m)
        
if __name__=='__main__':
    c=True
    student_num=1
    while(c):
        info=input("#{} Student data: ".format(student_num)) #Name(Space)Age(Space)Contact_number(Space)Email_ID
        print("Entered information : "+info)
        ql=info.split()
        q=("Split info: "+str(ql))
        print("Split information: "+q)
        print("Entered information - \n Name :{},\n Age : {},\n Contact number :{},\n Email ID :{}".format(ql[0],ql[1],ql[2],ql[3]))
        check=input("Enter if the entered value is corrected(y/n) : ")
        if check==y:
            wcsv(q)
            status=input("Would you like to enter more data(y/n) : ")
            if status==y:
                c=True
                student_num+=1
            else:
                c=False
        elif check==n:
            print("Please re-enter the values!")
