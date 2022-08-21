join_date=[2019,12,1,'SUN']
jyear,jmonth,jday,jweek=join_date
week=['MON','TUE','WED','THU','FRI','SAT','SUN']

resign_date=[2019,12,31]
ryear,rmonth,rday=resign_date

holidays=['12/25']


#계산해야 될 연도
years=[i for i in range(jyear,ryear+1)]

#윤년만 골라내기
yun_years=[y for y in years if (y%400==0) or (y%4==0 and y%100!=0)]

#윤년체크해서 모드 변경
month_day=[0,31,28,31,30,31,30,31,31,30,31,30,31]
yun_month_day=[0,31,29,31,30,31,30,31,31,30,31,30,31]
def checkY(year):
  global mdays
  if year in yun_years:
    mdays=yun_month_day
  else:
    mdays=month_day



#윤년1개당 요일 1개씩 뒤로 밀림 

#연도별 총 날짜list 구하기#
days_year=[]
days=0
f=mdays[jmonth]-jday
e=rday
#같은 연도 2019,2019
if len(years)==1:
  checkY(jyear)
  if jmonth==rmonth:
    days=rday-jday
  elif jmonth-rmonth==1:
    days=f+e
  else:
    days=f+e
    for m in range(jmonth+1,rmonth):
      days+=mdays[m]
  days_year.append(days)
#다른 연도 2019, 2021 
else:
  fd=

#총일수-주말-공휴일(주말x)
