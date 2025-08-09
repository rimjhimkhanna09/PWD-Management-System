#SOURCE CODE FOR PUBLIC WORK DEPARTMENT ROAD CONSTRUCTION MANAGEMENT SYSTEM

print("****************************************************************************")
print("*                                                                                                      *")
print("*                Welcome to PWD Road  Management System               *")
print("*                                                                                                     *")
print("****************************************************************************\n\n")

import pickle
import os

def gap():
    print("\n"*5)

        
def main_menu():
    while True:
       
        print("             _MAIN__MENU_\n\n")
        print("1. Projects of ROAD CONSTRUCTION")
        print("2. Tenders Released")        
        print("3. Tenders Alloted")
        print("4. Exit\n\n")
        sec = int(input("On which section would you like to work upon :"))
        print("\n\n")
        if sec==1:
            projects()
        elif sec==2:
             tenders()
        elif sec==3:
               alloted()
        elif sec==4:
                main_exit()
                break
        else:
            print("Please enter a valid choice:)")
     
def main_exit():
    gap()
    gap()
    gap()
    gap()
    print("                        THANKS FOR VISITING :)")
    gap()
    gap()
    gap()
   


def projects():
    while True:
        print("             _PROJECTS_\n\n")
        print("1. Add a New Project")
        print("2. View All Projects ")
        print("3. Search for a particular Project(s) ")
        print("4. Modify any Existing Project")
        print("5. Delete a particular Project")
        print("6. Exit\n\n")
        s= int(input("Which action would you like to perform :"))
        print("\n\n")

        if s==1:
            proadd()
        elif s==2:
             proview()
        elif s==3:
              prosearch()
        elif s==4:
              promod()
        elif s==5:
              prodel()
        elif s==6:
              break
        else:
            print("\n\nPlease enter a valid choice:)")

def proadd():
    p={}
    f=open("project.dat","ab")
    while True:
        pno=int(input("Enter project no.: "))
        pnm=input("Enter project name :")
        plen=float(input("Enter length of road(in meters):"))
        pty=input("Enter type of road:")
        pest=float(input("Enter estimated cost(in lakhs):"))
        pst=input("Enter status of project(not started/under construction/completed) :")
        p["pno"]=pno
        p["pnm"]=pnm
        p["plen"]=plen
        p["pty"]=pty
        p["pest"]=pest
        p["pst"]=pst
        pickle.dump(p,f)
        gap()
        w=input("want to add more records?(yes or no)\t:")
        if w=='n' or w=='N':
            break
    f.close()
    
    

   
def proview():
    f=open("project.dat","rb")
    p={}
    try:
        while True:
            p=pickle.load(f)
            print("Project No.\t:",p["pno"],"\n","Project Name\t:",p["pnm"])
            print("Road Length\t:",p["plen"])
            print("Type of Road\t:",p["pty"],"\n","Estimated Cost\t:",p["pest"])
            print("Status \t:",p["pst"])
            gap()
            l=input("Press enter to continue :)")
    except EOFError :
        f.close()
        E=input("Press enter to exit")
          
def pro_search_no():
    f=open("project.dat","rb")
    fl=0
    pno=int(input("Enter project number to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            print(p["pno"])
            if p["pno"]==pno:
                print("Project No.\t:",p["pno"])
                print("Project name\t:",p["pnm"])
                print("Road Length\t:",p["plen"])
                print("Type of road\t:",p["pty"])
                print("Estimated Cost\t:",p["pest"])
                print("Status\t:",p["pst"])
                gap()
                fl=1
                break
    except EOFError:
        f.close()
        if fl ==0:
            print("INVALID Project No. :)")
            print("Please Try Again !!!")

def pro_search_nm():
    f=open("project.dat","rb")
    fl=0
    pnm=input("Enter project name to be searched: ")
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if pnm in p["pnm"]:
                print("Project No.\t:",p["pno"])
                print("Project name\t:",p["pnm"])
                print("Road Length\t:",p["plen"])
                print("Type of road\t:",p["pty"])
                print("Estimated Cost\t:",p["pest"])
                print("Status\t:",p["pst"])
                gap()
                fl=1
                break
    except EOFError:
        f.close()
        if fl ==0:
            print("INVALID Project Name :)")
            print("Please Try Again !!!")

def pro_search_len():
    f=open("project.dat","rb")
    fl=0
    plen=float(input("Enter length of project to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if p["plen"]==plen:
                print("Project No.\t:",p["pno"])
                print("Project name\t:",p["pnm"])
                print("Road Length\t:",p["plen"])
                print("Type of road\t:",p["pty"])
                print("Estimated Cost\t:",p["pest"])
                print("Status\t:",p["pst"])
                gap()
                fl=1
                break
    except EOFError:
        f.close()
        if fl ==0:
            print("No Project of this length is avaiable :)")
            print("Please Try Again !!!")

def pro_search_cost():
    f=open("project.dat","rb")
    fl=0
    pc=float(input("Enter cost of project to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if p["pest"]==pc:
                print("Project No.\t:",p["pno"])
                print("Project name\t:",p["pnm"])
                print("Road Length\t:",p["plen"])
                print("Type of road\t:",p["pty"])
                print("Estimated Cost\t:",p["pest"])
                print("Status\t:",p["pst"])
                gap()
                fl=1
                break
    except EOFError:
        f.close()
        if fl ==0:
            print("No Project of this cost is avaiable :)")
            print("Please Try Again !!!")

def pro_search_status():
    f=open("project.dat","rb")
    fl=0
    pst=input("Enter status of project to be searched: ")
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if pst in p["pst"]:
                print("Project No.\t:",p["pno"])
                print("Project name\t:",p["pnm"])
                print("Road Length\t:",p["plen"])
                print("Type of road\t:",p["pty"])
                print("Estimated Cost\t:",p["pest"])
                print("Status\t:",p["pst"])
                gap()
                fl=1
                break
    except EOFError:
        f.close()
        if fl ==0:
            print("No Project of this status is avaiable :)")
            print("Please Try Again !!!")

            
def prosearch():
    f=open("project.dat","rb")
    while True:
        print("             _SEARCH BY:_\n\n")
        print("1. Project Number")
        print("2. Project Name ")
        print("3. Length of Project ")
        print("4. Cost of Project")
        print("5. Status of Project")
        print("6. Exit\n\n")
        ch= int(input("Which action would you like to perform :"))
        print("\n\n")
        if ch==1:
            pro_search_no()               
        elif ch==2:
            pro_search_nm()                
        elif ch==3:
            pro_search_len()                 
        elif ch==4:
            pro_search_cost()               
        elif ch==5:
             pro_search_status()                
        elif ch==6:
              break
        else:
            print("Please enter a valid choice:)")
        

def promod():     
        while True:
            f=open("project.dat","rb")
            t=open("temp.dat","wb")
            fl=0
            pno=int(input("Enter project no. to be modified  :"))
            f.seek(0)
            try:
                while True:
                    p=pickle.load(f)
                    gap()
                    if p["pno"]==pno:
                        print("The original values are :\n\n")
                        print("Project No.\t:",p["pno"])
                        print("Project name\t:",p["pnm"])
                        print("Road Length\t:",p["plen"])
                        print("Type of road\t:",p["pty"])
                        print("Estimated Cost\t:",p["pest"])
                        print("Status\t:",p["pst"],"\n\n\n")
                        print("ENTER THE NEW MODIFIED RECORDS :\n\n ")
                        pno=int(input("Enter project no.: "))
                        pnm=input("Enter project name :")
                        plen=float(input("Enter length of road(in meters):"))
                        pty=input("Enter type of road:")
                        pest=float(input("Enter estimated cost(in lakhs):"))
                        pst=input("Enter status of project(not started/under construction/completed) :")
                        p["pno"]=pno
                        p["pnm"]=pnm
                        p["plen"]=plen
                        p["pty"]=pty
                        p["pest"]=pest
                        p["pst"]=pst
                        fl=1
                    pickle.dump(p,t)
                    gap()                      
                    
            except EOFError:
                f.close()
                t.close()
                os.remove("project.dat")
                os.rename("temp.dat","project.dat")
                if fl==0:
                    print("Project not found.")
                else:
                    print("Record(s) successfully modified :)")
             
            c=input("want to modify more records?(y/n)")
            if c=="n"or c=="N":
                break

def prodel():
    f=open("project.dat","rb")
    t=open("temp.dat","wb")
    fl=0
    pno=int(input("Enter project number to be deleted  : "))
    print("\n\n")
    try:
        while True:
            p=pickle.load(f)
            if p["pno"]==pno:
                print("The deleted record is :\n")
                print("Project No.\t:",p["pno"],"\n","Project Name\t:",p["pnm"],"\n","Road Length\t:",p["plen"],"\n","Type of Road\t:",p["pty"],"\n","Estimated Cost\t:",p["pest"],"\n","Status \t:",p["pst"])
                fl=1
            else:
                pickle.dump(p,t)
    except EOFError:
        f.close()
        t.close()
    os.remove("project.dat")
    os.rename("temp.dat","project.dat")
    if fl==0:
        print("Project not found !!")
        E=input("Press enter to continue")
        projects()

    else:
        print("Record deleted successfully :)")
        E=input("Press enter to continue")
        projects()


def tenders():
    while True:
        print("             _TENDERS_\n\n")
        print("1. Add a Newly Released Tender")
        print("2. View All Tenders ")
        print("3. Search for a particular Tender(s) ")
        print("4. Modify any Existing Tender")
        print("5. Delete a particular Tender")
        print("6. Exit\n\n")
        s= int(input("Which action would you like to perform :"))
        print("\n\n")
        if s==1:
            tenadd()
        elif s==2:
             tenview()
        elif s==3:
              tensearch()
        elif s==4:
              tenmod()
        elif s==5:
              tendel()
        elif s==6:
              break
        else:
            print("\n\nPlease enter a valid choice:)")

def tenadd():
    p={}
    f=open("tender.dat","ab")
    while True:
        tno=int(input("Enter tender no.: "))
        tnm=input("Enter tender name :")
        tlen=float(input("Enter length of road(in meters):"))
        test=float(input("Enter budget for this tender(in lakhs):"))
        tpb=float(input("Cost spend in publishing tender(for office use only) :"))
        p["tno"]=tno
        p["tnm"]=tnm
        p["tlen"]=tlen
        p["test"]=test
        p["tpb"]=tpb
        pickle.dump(p,f)
        gap()
        w=input("want to add more records?(yes or no)\t:")
        if w in ["n","N"]:
            f.close()
            break
   
def tenview():
    f=open("tender.dat","rb")
    try:
        while True:
           p=pickle.load(f)
           print("Tender No.\t:",p["tno"],"\n","Tender Name\t:",p["tnm"],"\n","Road Length\t:",p["tlen"],"\n","Budget released for Tender\t:",p["test"],"\n","Cost of publishing tender(for office use only)\t:",p["tpb"])
           gap()
    except EOFError :
          f.close()
          
def ten_search_no():
    f=open("tender.dat","rb")
    fl=0
    tno=int(input("Enter tender number to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if p["tno"]==tno:
                print("Tender No.\t:",p["tno"])
                print("Tender name\t:",p["tnm"])
                print("Road Length\t:",p["tlen"])                  
                print("Budget released for Tender\t:",p["test"])                    
                gap()
                fl=1
                break
    except EOFError:
        if fl ==0:
           print("INVALID Tender No. :)")
           print("Please Try Again !!!")
        f.close()
        
def ten_search_nm():
    f=open("tender.dat","rb")
    fl=0
    tnm=input("Enter tender name to be searched: ")
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if tnm in p["tnm"]:
                print("Tender No.\t:",p["tno"])
                print("Tender name\t:",p["tnm"])
                print("Road Length\t:",p["tlen"])                  
                print("Budget released for Tender\t:",p["test"])                    
                gap()
                fl=1
                break
    except EOFError:
        if fl ==0:
           print("INVALID Tender No. :)")
           print("Please Try Again !!!")
        f.close()

def ten_search_len():
    f=open("tender.dat","rb")
    fl=0
    plen=float(input("Enter length of project to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if p["tlen"]==plen:
                print("Tender No.\t:",p["tno"])
                print("Tender name\t:",p["tnm"])
                print("Road Length\t:",p["tlen"])                  
                print("Budget released for Tender\t:",p["test"])                    
                gap()
                fl=1
                break
    except EOFError:
        if fl ==0:
           print("No tender of this length is avaiable :)")
           print("Please Try Again !!!")
        f.close()
        
def ten_search_budget():
    f=open("tender.dat","rb")
    fl=0
    pc=float(input("Enter budget of tender to be searched: "))
    f.seek(0)
    try:
        while True:
            p=pickle.load(f)
            if p["test"]==pc:
                print("Tender No.\t:",p["tno"])
                print("Tender name\t:",p["tnm"])
                print("Road Length\t:",p["tlen"])                  
                print("Budget released for Tender\t:",p["test"])                    
                gap()
                fl=1
                break
    except EOFError:
        if fl ==0:
           print("No tender of this budget is avaiable :)")
           print("Please Try Again !!!")
        f.close()
                
def tensearch():
    while True:        
        f=open("tender.dat","rb")
        print("             _SEARCH BY:_\n\n")
        print("1. Tender Number")
        print("2. Tender Name ")
        print("3. Length of Project ")
        print("4. Budget of Tender")
        print("5. Exit\n\n")
        ch= int(input("Which action would you like to perform :"))
        print("\n\n")
        if ch==1:
            ten_search_no()
        elif ch==2:
            ten_search_nm()       
        elif ch==3:
            ten_search_len()
        elif ch==4:
            ten_search_budget()        
        elif ch==5:
              break
        else:
            print("Please enter a valid choice:)")

def tenmod():
    while True:
        f=open("tender.dat","rb")
        t=open("temp.dat","wb")
        fl=0
        try:
            while True:
                p=pickle.load(f)
                tno=int(input("Enter tender no. to be modified  :"))
                gap()
   
                if p["tno"]==tno:
                    print("The original values are :\n\n")
                    print("Tender No.\t:",p["tno"])
                    print("Tender name\t:",p["tnm"])
                    print("Road Length\t:",p["tlen"])                
                    print("Budget released for tender\t:",p["test"])
                    print("Cost of publishing\t:",p["tpb"])
                
                    print("ENTER THE NEW MODIFIED RECORDS :\n\n ")
                    tno=int(input("Enter tender no.: "))
                    tnm=input("Enter tender name :")
                    tlen=float(input("Enter length of road(in meters):"))                
                    test=float(input("Enter budget of tender(in lakhs):"))
                    tpb=float(input("Enter cost of publishing tender(for office use only) :"))
                
                    p["tno"]=tno
                    p["tnm"]=tnm
                    p["tlen"]=tlen                
                    p["test"]=test
                    p["tpb"]=tpb
                
                    fl=1
                
                pickle.dump(p,t)
                gap()
        

        except EOFError:
            if fl==0:
                print("Tender not found.")
            else:
                print("Tender found and updated")
            f.close()
            t.close()
            os.remove("tender.dat")
            os.rename("temp.dat","tender.dat")
            
        
        c=input("want to modify more records?(y/n)")
        if c=="n"or c=="N":
            break




             

def tendel():
    f=open("tender.dat","rb")
    t=open("temp.dat","wb")
    fl=0
    tno=int(input("Enter tender number to be deleted  : "))
    print("\n\n")
    try:
        while True:
            p=pickle.load(f)
            if p["tno"]==tno:
                print("The deleted record is :\n")
                print("Tender No.\t:",p["tno"],"\n","Tender Name\t:",p["tnm"],"\n","Road Length\t:",p["tlen"],"\n","Budget released for Tender\t:",p["test"],"\n","Cost of publishing tender(for office use only)\t:",p["tpb"])
                fl=1
            else:
                pickle.dump(p,t)
    except EOFError:
        f.close()
        t.close()
    os.remove("tender.dat")
    os.rename("temp.dat","tender.dat")
    if fl==0:
        print("Tender not found !!")
        E=input("Press enter to continue")
    else:
        print("Record deleted successfully :)")
        E=input("Press enter to continue")

        
def alloted():
    print("             _TENDERS Alloted_\n\n")
    print("1. Add a New Tender Allotment")
    print("2. View All Tenders Allotments")
    print("3. Search for a particular Allotment(s) ")
    print("4. Modify any Existing Tender Allotement")
    print("5. Delete a particular Allotment")
    print("6. Exit\n\n")
    s= int(input("Which action would you like to perform :"))
    print("\n\n")

    if s==1:
        alladd()
    elif s==2:
         allview()
    elif s==3:
          allsearch()
    elif s==4:
          allmod()
    elif s==5:
          alldel()
    elif s==6:
          allexit()
    else:
        print("\n\nPlease enter a valid choice:)")

def alladd():
    p={}
    f=open("alloted.dat","ab")
    while True:
        ano=int(input("Enter allotment no.: "))
        anm=input("Enter name of constructer :")
        alen=float(input("Enter quality & stability guarenteed for road(in years):"))
        
        aest=float(input("Enter discount given for this tender(in %):"))
        apb=float(input("Time bond to complete tender(in months) :"))
        p["ano"]=ano
        p["anm"]=anm
        p["alen"]=alen
        
        p["aest"]=aest
        p["apb"]=apb
        pickle.dump(p,f)
        gap()
        w = input("want to add more records?(yes or no)\t:")
        if w in ("yes", "Yes", "YES", "y", "Y", "YEs",):
           continue
        else:
            break
    f.close()
    j=input ("Press enter to exit.")
    alloted()

   
def allview():
    f=open("alloted.dat","rb")
    try:
        while True:
           p=pickle.load(f)
           print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])
           gap()
    except EOFError :
          f.close()
          E=input("Press enter to exit")
          alloted()

def allsearch():
    f=open("alloted.dat","rb")
    print("             _SEARCH BY:_\n\n")
    print("1. Allotment Number")
    print("2. Constructer Name ")
    print("3. Discount given ")
    print("4. Time bond to complete project")
    
    print("5. Exit\n\n")
    ch= int(input("Which action would you like to perform :"))
    print("\n\n")
    if ch==1:
        fl=0
        ano=int(input("Enter allotment number to be searched: "))
        f.seek(0)
        try:
            while True:
                p=pickle.load(f)
                if p["ano"]==ano:
                   print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])  
                   gap()
                   fl=1
                   break
        except EOFError:
                pass
        if fl ==0:
           print("INVALID Allotment No. :)")
           print("Please Try Again !!!")
           allsearch()
    elif ch==2:
        fl=0
        anm=input("Enter constructer name to be searched: ")
        f.seek(0)
        try:
            while True:
                p=pickle.load(f)
                if anm in p["anm"]:
                    print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])   
                    gap()
                    fl=1
                    break
        except EOFError:
                pass
        if fl ==0:
           print("INVALID Constructer Name :)")
           print("Please Try Again !!!")
           allsearch() 
    elif ch==3:
        fl=0
        aest=float(input("Enter discount given to be searched: "))
        f.seek(0)
        try:
            while True:
                p=pickle.load(f)
                if p["aest"]==aest:
                   print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])  
                   
                   gap()
                   fl=1
                   break
        except EOFError:
                pass
        if fl ==0:
           print("No allotment with this discount is avaiable :)")
           print("Please Try Again !!!")
           allsearch()  
    elif ch==4:
        fl=0
        pc=float(input("Enter time bond to be searched: "))
        f.seek(0)
        try:
            while True:
                p=pickle.load(f)
                if p["apb"]==pc:
                    print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])   
                     
                    gap()
                    fl=1
                    break
        except EOFError:
                pass
        if fl ==0:
           print("No tender with this time bond is avaiable :)")
           print("Please Try Again !!!")
           allsearch()
    
    elif ch==5:
          alloted()
    else:
        print("Please enter a valid choice:)")

def allexit():
    main_menu()

def allmod():
    f=open("alloted.dat","rb+")
    fl=0
    try:
        while True:
            A=f.tell()
            p=pickle.load(f)
            ano=int(input("Enter allotment no. to be modified  :"))
            gap()
   
            if p["ano"]==ano:
                print("The original values are :\n\n")
                print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])      
                print("ENTER THE NEW MODIFIED RECORDS :\n\n ")
                ano=int(input("Enter allotment no.: "))
                anm=input("Enter name of constructer :")
                alen=float(input("Enter quality & stability guarenteed for road(in years):"))
        
                aest=float(input("Enter discount given for this tender(in %):"))
                apb=float(input("Time bond to complete tender(in months) :"))
         
                p["ano"]=ano
                p["anm"]=anm
                p["alen"]=alen
                
                p["aest"]=aest
                p["apb"]=apb
                fl=1
                f.seek(p)
                pickle.dump(p,f)
                gap()
                w=input("want to modify more records? (yes or no)\t:")
                if w=="yes"or"Yes"or"YES"or"y"or"Y":
                   continue
                else:
                    f.close()
                    break

    except EOFError:
         if fl==0:
             print("Allotment not found.")
             v=input("want to try again ?? (yes/no) ")
             if v=="yes"or"Yes"or"YES"or"y"or"Y":
                gap()
                gap()
                allmod()
             else:
                 gap()
                 #allders()
         else:
             print("Record(s) successfully modified :)")
             alloted()



             

def alldel():
    f=open("alloted.dat","rb")
    t=open("temp.dat","wb")
    fl=0
    ano=int(input("Enter alloted number to be deleted  : "))
    print("\n\n")
    try:
        while True:
            p=pickle.load(f)
            if p["ano"]==ano:
                print("The deleted record is :\n")
                print("Allotment No.\t:",p["ano"],"\n","Constructer Name\t:",p["anm"],"\n","Quality & stability guarenteed(in years)\t:",p["alen"],"\n","Discount given\t:",p["aest"],"\n","Time bond to complete project\t:",p["apb"])       
                fl=1
            else:
                pickle.dump(p,t)
    except EOFError:
        f.close()
        t.close()
    os.remove("alloted.dat")
    os.rename("temp.dat","alloted.dat")
    if fl==0:
        print("Tender Allotment not found !!")
        E=input("Press enter to continue")
        alloted()

    else:
        print("Record deleted successfully :)")
        E=input("Press enter to continue")
        alloted()
    

main_menu()
