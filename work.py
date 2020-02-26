import time 
import os
import datetime

def main():
    print('''
Hello my dear, it is me:) 
-----------------------------------
If you want know all about yourself
-----------------------------------
''')
doc = False
x=datetime.datetime.now()
a=str(x)
day=int(a[8:10])
month=int(a[5:7])
year=int(a[0:4])
power=0

hour1=int(a[11:13])
minut1=int(a[14:16])
sekund1=int(a[17:19])

while doc==False:
    kz=open('amir.txt','w')
    kz.write('')
    os.system('cls||clear')
    main()
    print("_____This is the time when you started_____")
    print('        ',x)
    print('\n')
    time.sleep(5)
    os.system('cls')
    f=open('amir.txt','a')
    def name():
        boc=False
        while boc==False:
            print("Please enter your name") 
            name=input('\t\t\t')
            if len(name)>2:
                break
            else:
                os.system('cls||clear')
                print('__PLease Enter \'YOUR\' name__\n')
        return name
    name=name()
    def age():
        boc=False
        while boc==False:
            print("Amir please enter: Your age")
            age=int(input('\t\t\t'))
            x=0
            if age>5 and age<112:
                x=5
            else:
                os.system('cls||clear')
                print('__PLease Enter \'YOUR\' age__\n')
            if x==5:
                return age      
    age=age()
    f.write(str(age))
    f.write('\n')

    def months():
        boc=False
        while boc==False:
            print("Please enter: in which month you was born(number of month)")
            print('For example (MAY=5)')
            months=int(input('\t\t\t'))
            x=0
            if months>0 and months<13:
                x=5
            else:
                os.system('cls||clear')
                print('__PLease Enter \'Existing\' month__\n')
            if x==5:
                return months      
    months=months()
    f.write(str(months))
    f.write('\n')

    namemonths=''
    if months==1:
        namemonths="January"
    elif months==2:
        namemonths="Febuary"
    elif months==3:
        namemonths="April"
    elif months==4:
        namemonths="March"
    elif months==5:
        namemonths="May"
    elif months==6:
        namemonths='June'
    elif months==7:
        namemonths="July"
    elif months==8:
        namemonths="August"
    elif months==9:
        namemonths="September"
    elif months==10:
        namemonths="October"
    elif months==11:
        namemonths="November"
    elif months==12:
        namemonths="December"

    def days():
        boc=False
        while boc==False:
            print("Please enter: What is the day of " +namemonths+" you was born")
            print("For example (1,2,3,4....,31)")
            days=int(input('\t\t\t'))
            x=0
            if days>0 and days<32:
                x=5
            else:
                os.system('cls||clear')
                print('__PLease Enter \'Existing\' days__\n')
            if x==5:
                return days      
    days=days()
    f.write(str(days))
    f.write('\n')

    os.system('cls')
    
    if months<=month:
        
        if months==month:
            
            if days<=day:
                print('\n\n\n\n\t\tYOUR YEAR '+str(year-age))
                print('\n\n\n')
                f.write(str(year-age))
                f.write('\n')  
            else:
                print('\n\n\n\n\t\tYOUR YEAR '+ str(year-age-1))
                print('\n\n\n')
                f.write(str(year-age-1))
                f.write('\n')   
        elif months<month:
            print('\n\n\n\n\t\tYOUR YEAR '+str(year-age))
            print('\n\n\n')
            f.write(str(year-age))
            f.write('\n')
    else:
        print('\n\n\n\n\t\tYOUR YEAR '+ str(year-age-1))
        print('\n\n\n')
        f.write(str(year-age-1))
        f.write('\n')

    time.sleep(4)
    os.system('cls')
    doc==True
    break
def menu():
    print('''------------------------------------
1.In which day of week you was born?
2.Year of whom?
3.Horoscope
4.EXIT
------------------------------------
''')

f=open('amir.txt','r')
p=f.readlines()
a=int(p[2])
b=int(p[1])
c=int(p[3])
def visokos(x):
    cnt=0
    p=[2020,2016,2012,2008,2004,2000,1996,1992,1988,1984,1980,1976,1972,1968,1964,1960,1956,1952]
    for i in range(len(p)):
        if p[i]==x:
            cnt+=1
        else:
            cnt+=0
    if cnt==0:
        return 0
    else:
        return 1
docs=False

while docs==False:
    os.system('cls||clear')
    menu()
    men=int(input('\n\n'))
    def zhanuar(x):
        p1=[1956,1968,1980,1992,2004,2016]
        p2=[1957,1969,1981,1993,2005,2017]
        p3=[1958,1970,1982,1994,2006,2018]
        p4=[1959,1971,1983,1995,2007,2019]
        p5=[1960,1972,1984,1996,2008,2020]
        p6=[1961,1973,1985,1997,2009,2021]
        p7=[1962,1974,1986,1998,2010,2022]
        p8=[1963,1975,1987,1999,2011,2023]
        p9=[1964,1976,1988,2000,2012,2024]
        p10=[1965,1977,1989,2001,2013,2025]
        p11=[1966,1978,1990,2002,2014,2026]
        p12=[1967,1979,1991,2003,2015,2027]
        for i in range(len(p1)):
            if p1[i]==x:
                return int(1)
            elif p2[i]==x:
                return int(2)
            elif p3[i]==x:
                return int(3)
            elif p4[i]==x:
                return int(4)
            elif p5[i]==x:
                return int(5)
            elif p6[i]==x:
                return int(6)
            elif p7[i]==x:
                return int(7)
            elif p8[i]==x:
                return int(8)
            elif p9[i]==x:
                return int(9)
            elif p10[i]==x:
                return int(10)
            elif p11[i]==x:
                return int(11)
            elif p12[i]==x:
                return int(12)
    if men==1:
        p=datetime.datetime(c,b,a)
        os.system('cls||clear')
        print('-------------------------YOU WAS BORN IN----------------------------')
        print('-----------------------------',end='')
        print(p.strftime('%A'),end='')
        print('--------------------------------')
        print('\n\n\n\n\n\n')
        time.sleep(4)
        os.system('cls||clear')
    
    elif men==2:
        vi = zhanuar(c)
        os.system('cls||clear')
        if vi==1:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t    You have a year ___MONKEY___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==2:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t    You have a year ___HEN___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==3:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t    You have a year ___DOG___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==4:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___PIG___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==5:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___MONKEY___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==6:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___COW___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==7:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___TIGER___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==8:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___RABBIT___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==9:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___DRAGON___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==10:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___SNAKE___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==11:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___HORSE___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        elif vi==12:
            print('''---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------
\t   You have a year ___SHEEP___
---------------------------------------------------------
---------------------------------------------------------
---------------------------------------------------------''')
        print('\n')
        time.sleep(4)
    elif men==3:
        x=visokos(c)
        if x==0:
            x1,x2,x3,x4,x5,x6=20,49,79,110,140,172
            x7,x8,x9,x10,x11,x12,x13=203,235,266,296,326,355,365
            if b==1:
                goros=a
            elif b==2:
                goros=31+a
            elif b==3:
                goros=59+a
            elif b==4:
                goros=90+a
            elif b==5:
                goros=120+a
            elif b==6:
                goros=151+a
            elif b==7:
                goros=181+a
            elif b==8:
                goros=212+a
            elif b==9:
                goros=243+a
            elif b==10:
                goros=273+a
            elif b==11:
                goros=304+a
            elif b==12:
                goros=334+a
            os.system('cls||clear')
            if goros<=20:
                print('\n\n\n\n-------------------You are on the horoscope CAPRICORN-------------------')
            elif goros>20 and goros<=49:
                print('\n\n\n\n-------------------You are on the horoscope of AQUARIUS-------------------')
            elif goros>49 and goros<=79:
                print('\n\n\n\n-------------------You are on the horoscope of FISH-------------------')
            elif goros>79 and goros<=110:
                print('\n\n\n\n-------------------You are on the horoscope ARIES-------------------')
            elif goros>110 and goros<=140:
                print('\n\n\n\n-------------------You are on the horoscope TAURUS-------------------')
            elif goros>140 and goros<=172:
                print('\n\n\n\n-------------------You are on the horoscope TWINS-------------------')
            elif goros>172 and goros<=203:
                print('\n\n\n\n-------------------You are on the horoscope CANCER-------------------')
            elif goros>203 and goros<=235:
                print('\n\n\n\n-------------------You are on the horoscope LION-------------------')
            elif goros>235 and goros<=266:
                print('\n\n\n\n-------------------You are on the horoscope VIRGO-------------------')
            elif goros>266 and goros<=296:
                print('\n\n\n\n-------------------You are on the horoscope of LIBRA-------------------')
            elif goros>296 and goros<=326:
                print('\n\n\n\n-------------------You are on the horoscope SCORPIO-------------------')
            elif goros>326 and goros<=355:
                print('\n\n\n\n-------------------You are on the horoscope of SAGITARRIUS-------------------')
            elif goros>355:
                print('\n\n\n\n-------------------You are on the horoscope of CAPRICORN-------------------')
            print('\n\n\n\n')
            time.sleep(4)
        elif x==1:
            if b==1:
                goros=a
            elif b==2:
                goros=31+a
            elif b==3:
                goros=60+a
            elif b==4:
                goros=91+a
            elif b==5:
                goros=121+a
            elif b==6:
                goros=152+a
            elif b==7:
                goros=182+a
            elif b==8:
                goros=213+a
            elif b==9:
                goros=244+a
            elif b==10:
                goros=274+a
            elif b==11:
                goros=305+a
            elif b==12:
                goros=335+a
            os.system('cls||clear')
            if goros<=20:
                print('\n\n\n\n-------------------You are on the horoscope CAPRICORN-------------------')
            elif goros>20 and goros<=49:
                print('\n\n\n\n-------------------You are on the horoscope of AQUARIUS-------------------')
            elif goros>49 and goros<=80:
                print('\n\n\n\n-------------------You are on the horoscope of FISH-------------------')
            elif goros>80 and goros<=111:
                print('\n\n\n\n-------------------You are on the horoscope ARIES-------------------')
            elif goros>111 and goros<=141:
                print('\n\n\n\n-------------------You are on the horoscope TAURUS-------------------')
            elif goros>140 and goros<=172:
                print('\n\n\n\n-------------------You are on the horoscope TWINS-------------------')
            elif goros>173 and goros<=204:
                print('\n\n\n\n-------------------You are on the horoscope CANCER-------------------')
            elif goros>204 and goros<=236:
                print('\n\n\n\n-------------------You are on the horoscope LION-------------------')
            elif goros>236 and goros<=267:
                print('\n\n\n\n-------------------You are on the horoscope VIRGO-------------------')
            elif goros>267 and goros<=297:
                print('\n\n\n\n-------------------You are on the horoscope of LIBRA-------------------')
            elif goros>297 and goros<=327:
                print('\n\n\n\n-------------------You are on the horoscope SCORPIO-------------------')
            elif goros>327 and goros<=356:
                print('\n\n\n\n-------------------You are on the horoscope of SAGITARRIUS-------------------')
            elif goros>356:
                print('\n\n\n\n-------------------You are on the horoscope of CAPRICORN-------------------')
            print('\n\n\n\n')
            time.sleep(4)
    elif men==4:
        os.system('cls||clear')
        kkk=datetime.datetime.now()
        pirt=str(kkk)
        print('''\n\n\n\n\t\t_____This is the time when you finished_____''')
        print('\t\t\t'+str(kkk)+'\n\n\n')
        time.sleep(5)
        os.system('cls||clear')
        print('\n\n\n\t\t\t\tYou worked with my program ')
        hour2=int(pirt[11:13])
        minut2=int(pirt[14:16])
        sekund2=int(pirt[17:19])
        total1=hour1*3600+minut1*60+sekund1
        total2=hour2*3600+minut2*60+sekund2
        total=total2-total1
        fi1=str(int(total/3600))
        poooo=int(total/3600)
        fi2=str(int((total-poooo*3600)/60))
        fi3=str(total%60)
        print('\t\t\t\t     '+fi1+':h  '+fi2+':m  '+fi3+':sec  '+'\n\n\n')
        time.sleep(5)
        print("\n\n\n\n\n\n------------------------------Thank you MY DEAR!!!------------------------------\n\n\n\n\n")
        time.sleep(3)
        os.system('cls||clear')
        break
    else:
        os.system('cls||clear')
        print('\n\n\nPlease choose one from following options\n\n\n')
        time.sleep(2)