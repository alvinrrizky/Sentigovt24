from datetime import datetime, timedelta
import pytz

timezone = pytz.timezone('Asia/Jakarta')
today = datetime.now(timezone).replace(hour=23, minute=59, second=59, microsecond=59)
last_seven_days = today.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=6)

class DateHelper:

    def getTodayDate(self):
        return datetime.now(timezone).replace(hour=23, minute=59, second=59, microsecond=59)
    
    def getLastSevenDays(self):
        today = self.getTodayDate()
        return today.replace(hour=0, minute=0, second=0, microsecond=0) - timedelta(days=6)
    
    def convertStartDate(date): # function to format hour ins start date to 00:00:00
        date = datetime.strptime((datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')),('%Y-%m-%d'))
        date = date.replace(tzinfo=pytz.utc).astimezone(timezone)
        date = date.replace(hour=0, minute=0, second=0, microsecond=0)
        return date

    def convertEndDate(date): # function to format hour ins start date to 23:59:59
        date = datetime.strptime((datetime.strptime(date, '%d/%m/%Y').strftime('%Y-%m-%d')),('%Y-%m-%d'))
        date = date.replace(tzinfo=pytz.utc).astimezone(timezone)
        date = date.replace(hour=23, minute=59, second=59, microsecond=59)
        return date

    def getDates(start, end):
        dates = []
        i = 0

        cur_date = start
        while cur_date <= end:
            date = cur_date.strftime('%Y-%m-%d')
            # print(date) 
            dates.append(date)
            cur_date += timedelta(days=1)

        return dates