import string

daysInYear = 100
daysInMonth = 10
daysInWeek = 10
date = "0001-01-01"

def Week():
    dayOfTheWeek =[]
    for i in string.ascii_uppercase:
        dayOfTheWeek.append(i)

    return dayOfTheWeek

def y_m(daysInYear,daysInMonth):
    one_Yesr = daysInYear / daysInMonth
    Day_excess = daysInYear % daysInMonth
    
    return one_Yesr,Day_excess

def date_factor(date): 
    date_YMW = date.split('-')
    date_Year = int(date_YMW[0])
    date_Month = int(date_YMW[1])
    date_Day = int(date_YMW[2])
    return(date_Year, date_Month, date_Day)

def main (Day_excess,date_Day,daysInWeek):
    if date_Day <= int(daysInMonth) and date_Month <= one_Yesr:
        if Day_excess == 0:
            while(date_Day > daysInWeek):
                date_Day = date_Day - daysInWeek   
            #print(date_Day)
            print(dayOfTheWeek[date_Day-1])

    #elif date_Day > int(daysInMonth) or date_Month > one_Yesr:
    else:
        print(-1)

#def youbi():



if __name__ == '__main__':
    #lines = []
    daysInYear, daysInMonth, daysInWeek, date = input().split()
    #for l in sys.stdin:
    #    lines.append(l.rstrip('\r\n'))
    #main(lines)
    #print(lines)
    dayOfTheWeek = Week()
    #print(dayOfTheWeek)
    one_Yesr,Day_excess = (y_m(int(daysInYear),int(daysInMonth)))
    #print(one_Yesr,Day_excess)
    date_Year, date_Month, date_Day = date_factor(date)
    #print(date_Year)
    main(int(Day_excess),int(date_Day),int(daysInWeek))