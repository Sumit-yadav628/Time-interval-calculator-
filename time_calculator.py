#for entering the time 
time1=input("Enter your time interval 1 HH:MM:SS\n")
time2=input("Enter your time interval 2 HH:MM:SS\n")

# time interval first
HH1=int(time1[0:2])
MM1=int(time1[3:5])
SS1=int(time1[6:len(time1)])

#time interval second 
HH2=int(time2[0:2])
MM2=int(time2[3:5])
SS2=int(time2[6:len(time2)])

print(f"Your given time_1 is {HH1}:{MM1}:{SS1} \n")
print(f"Your given time_2 is {HH2}:{MM2}:{SS2} \n")

if HH1>=24 or HH2>=24 or MM1>=60 or MM2>=60 or SS1>=60 or SS2>=60:
    print("Please enter a valid time:\n")
    print(f"Your time_1 is {HH1}:{MM1}:{SS1} and time_2 is {HH2}:{MM2}:{SS2} \n")
    print("And this is not a valid time.\n")

elif MM1>MM2:
    MM=MM2+60-MM1
    HH=HH2-HH1-1
    if SS1==SS2:
        SS=0
    elif SS1>SS2:
        SS=SS2+60-SS1
        MM=MM2+60-MM1-1
    elif SS1<SS2:
        SS=SS2-SS1
    print(f"The interval is {HH} hours {MM} minutes and {SS} seconds.\n")

elif MM1<MM2:
    if SS1==SS2:
        HH=HH2-HH1
        MM=MM2-MM1
        SS=0
    elif SS1>SS2:
        HH=HH2-HH1
        MM=MM2-MM1-1
        SS=SS2+60-SS1
    elif SS1<SS2:
        SS=SS2-SS1
        MM=MM2-MM1
        HH=HH2-HH1
    print(f"The interval is {HH} hours {MM} minutes and {SS} seconds.\n")

elif MM1==MM2:
    if SS1==SS2:
        HH=HH2-HH1  
        MM=0        
        SS=0
    elif SS1>SS2:
        SS=SS2+60-SS1
        MM=59       
        HH=HH2-HH1-1  
    elif SS1<SS2:
        SS=SS2-SS1
        MM=0         
        HH=HH2-HH1 
    print(f"The interval is {HH} hours {MM} minutes and {SS} seconds.\n")