# -*- coding: utf-8 -*-
# @Time : 2021-04-15
# @Author : zha0gongz1
# @File : WebSourceCodeVerificationScan.py
import os
import requests
import random
import urllib3
import time
import re
from optparse import OptionParser


def scan(url):
    ua_list = [
        "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.7113.93 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64; rv:85.0) Gecko/20100101 Firefox/85.0",
        "Mozilla/5.0 (X11; Linux i686; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4369.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; rv:11.0) like Gecko",
        "Mozilla/5.0 CK={} (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.27 Safari/537.36 OPR/74.0.3904.0 (Edition developer)",
        "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 OPR/73.0.3856.284 (Edition Yx 03)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.3538.77 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.50 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4371.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Safari/605.1.15"]
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}
    url1 = url
    respon = requests.get(url=url1, headers=headers, verify=False, timeout=5)
    if (respon.status_code != -1):
        print('[' + str(respon.status_code) + ']' + ":" + url1)


if __name__ == '__main__':
    parser = OptionParser('python CMSFloderScanner.py -u <Target URL> -f <CMS Source code folder> ]')
    parser.add_option('-u', '--url', dest='url', type='string', help='target url for scan')
    parser.add_option('-f', '--file', dest='folder_name', type='string', help='dictionary filename')
    (options, args) = parser.parse_args()
    print('''
        __          ____                               ___
 ____  / /_  ____ _/ __ \____ _____  ____  ____ _____ <  /
/_  / / __ \/ __ `/ / / / __ `/ __ \/ __ \/ __ `/_  / / / 
 / /_/ / / / /_/ / /_/ / /_/ / /_/ / / / / /_/ / / /_/ /  
/___/_/ /_/\__,_/\____/\__, /\____/_/ /_/\__, / /___/_/   
                      /____/            /____/   
    Welcome to Web CMS Source Code Verification Scan
    Version:1.0 Author:zha0gongz1@Ó°
    ''')
    start = time.time()
    try:
        multithread = []
        thread_count = options.count
        for dirpath, dirname, files in os.walk(options.folder_name):
            for file_name in files:
                tmppath = str(dirpath) + '/' + file_name
                webpath = re.search(r'(/.*)', tmppath)
                url = options.url + webpath.group()
                scan(url)
    except:
        pass

    end = time.time()
    usedtime = int(end - start)
    info = '''
    ---------- :) ----------
    The scan time£º%f s
    ---------- end --------
    ''' % (usedtime)
    print(info)
