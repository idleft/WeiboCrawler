# -*- coding: utf-8 -*-

import weiboLogin
import urllib
import urllib2
import time

def keyWordCrawler():
    filename = './config/account'#保存微博账号的用户名和密码，第一行为用户名，第二行为密码
    qYear = 2013 

    username,passwd = get_account(filename)

    # WBLogin = weiboLogin.weiboLogin()
    # if WBLogin.login(filename)==1:
    #   print 'Login success!'
    # else:
    #   print 'Login error!'
    #   exit()

    #url = 'http://s.weibo.com/weibo/%25E6%2588%2591%25E5%2588%2586%25E6%2589%258B&xsort=time&scope=ori&timescope=custom:2013-05-01:2013-05-01&Refer=g'
    #print urllib.urlopen(url).read()  

    for iter1 in range(5,6):
        if iter1 ==2 and (qYear%4==0 and qYear%100!=0 or (qYear%400)==0):
            maxDay = 29
        elif iter1 == 2:
            maxDay = 28
        elif iter1<8 and iter1%2==0 or iter1>=8 and iter1%2==1:
            maxDay = 30
        else:
            maxDay = 31
        # url = http://s.weibo.com/weibo/%%25E6%2588%2591%25E5%2588%2586%25E6%2589%258B&xsort=time&scope=ori&timescope=custom:2013-
        for iter2 in range(1,1+1):

            url = 'http://s.weibo.com/weibo/%%25E5%%2588%%2586%%25E6%%2589%%258B&xsort=time&scope=ori&timescope=custom:2013-%02d-%02d:2013-%02d-%02d&Refer=g'\
            % (iter1,iter2,iter1,iter2)
            data = urllib.urlopen(url)
            text = data.read()
            # write the page result to file
            fileHandle = open('pages/page-'+str(iter1)+' '+str(iter2)+'.txt','w')
            fileHandle.write(text+'\n')
            fileHandle.close()
            # get the weibo count of certain day
            weiboCnt = getCount(data)
            print weiboCnt
            fileHandle = open('result.txt','a')
            fileHandle.write(str(weiboCnt)+'\n')
            fileHandle.close()

def get_account(filename):
    f=file(filename)
    flag = 0
    for line in f:
        if flag == 0:
            username = line.strip()
            flag +=1
        else:
            pwd = line.strip()
    f.close()
    return username,pwd


def getCount(data):
    
    return 10


if __name__ == '__main__':
    keyWordCrawler()