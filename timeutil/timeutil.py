# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 11:28:50 2019

@author: Administrator
"""
import time
import datetime




class TimeUtil(object):
    
    def __init__(self, yearPara, monthPara, dayPara, HourPara, minPara, secondPara = 0):
        
        yearPara  = int(yearPara)
        monthPara = int(monthPara)
        dayPara   = int(dayPara)
        HourPara  = int(HourPara)
        minPara   = int(minPara)   
        secondPara   = int(secondPara)      
        
        self.parameter = [yearPara, monthPara, dayPara, HourPara, minPara]

        self.datetime =  datetime.datetime(yearPara, monthPara, dayPara, HourPara, minPara, secondPara)
        self.timetuple =  self.datetime.timetuple()
        self.timetupleInt = time.mktime(self.timetuple)

    @staticmethod
    def getMonthList(yearPara, monthPara):
        yearPara  = int(yearPara)
        monthPara = int(monthPara)

        requiredDatetime = datetime.datetime(yearPara, monthPara, 1)

        
        
        returnedList = []

        

        


    @staticmethod
    def currentTimeUtilObj():

        currentDatetime = datetime.datetime.now()
        tupleInt = time.mktime(currentDatetime.timetuple())
        return TimeUtil.getObjFromTimetupleint(tupleInt)

    @staticmethod
    def getObjFromTimetupleint(ctimePara):
        return TimeUtil(*TimeUtil.getStaticParameterFromTimeint(ctimePara))    

    @staticmethod
    def getStaticParameterFromTimeint(timeintPara):

        strList = time.strftime('%Y,%m,%d,%H,%M,%S',time.localtime(timeintPara))
        return strList.split(",")


    def addDay(self, dayPara):
        self.timetupleInt = self.timetupleInt + 86400 * dayPara
    
    def getChinese(self):
        return time.strftime('%Y年%m月%d日',time.localtime(self.timetupleInt))

    def getChineseHour(self):
        return time.strftime('%Y年%m月%d日  %H:%M',time.localtime(self.timetupleInt))

    def getDashTime(self):
        return time.strftime('%Y-%m-%d',time.localtime(self.timetupleInt))

    def getSlashTime(self):
        return time.strftime('%Y/%m/%d',time.localtime(self.timetupleInt))
    
    def getUnderDashTime(self):
        return time.strftime('%Y_%m_%d',time.localtime(self.timetupleInt))    
    
    def get(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(self.timetupleInt))        

    def getYMDParametersForDate(self):
        string =  time.strftime('%Y, %m, %d, %H, %M, %S',time.localtime(self.timetupleInt))   
        return string.split(",")

    def getYMDParametersForDateComa(self):
        string =  time.strftime('%Y, %m, %d, %H, %M, %S',time.localtime(self.timetupleInt))   
        return string



    def getWorkDay(self):
        
        a  = self.parameter[0]
        b  = self.parameter[1]
        c  = self.parameter[2]
    
        dayTime=('{}-{}-{} 12:00:00'.format(a, b, c))
        whatday= datetime.datetime.strptime(dayTime,'%Y-%m-%d %H:%M:%S').strftime("%w")
        print whatday
        print type(whatday)
        if whatday == "0":
            return 7
        elif whatday == "6":
            return 6
        else:
            return 0    
    
    @staticmethod
    def fromString(strPara):
        strPara = str(strPara)
        yearPara = strPara[0:4]
        monthPara = strPara[4:6] 
        dayPara = strPara[6:8]
        HourPara = "1"
        minPara = "1"
        print (yearPara, monthPara, dayPara, HourPara, minPara)
        t = TimeUtil(yearPara, monthPara, dayPara, HourPara, minPara)
        return t

    def getParameter(self):
        return self.parameter
        
    @staticmethod
    def test():
        test = TimeUtil(2014, 8, 15, 9, 0)
        
        print test.timetupleInt
        print "This is a datetime type", test.datetime

        test.currentTimeUtilObj()

        print test.getChinese()
        
        print test.getChineseHour()
        print test.getDashTime()
        print test.getSlashTime()
        #print test.fromString(20180503)
        
if __name__ == "__main__":
    TimeUtil.test()
