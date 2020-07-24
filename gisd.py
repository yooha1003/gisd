#!/usr/bin/env python3
"""
Google image searching and downloading script (Ver 0.1)
"""

# import modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import argparse
import sys
import os
from tqdm import tqdm
import time
import ssl
import urllib.request
import requests
from urllib.parse import quote
import array as arr
from bs4 import BeautifulSoup


class gisd:
    def __init__(self):
        pass

    def down_url(self, keywords, limit):
        kw_search = [str(item).strip() for item in keywords.split(',')]
        i = 0
        while i < len(kw_search):
            self._create_directories(root_dir, kw_search[i])
            url = 'https://www.google.com/search?q=' + quote(
                kw_search[i].encode('utf-8')) + '&biw=1536&bih=674&tbm=isch&sxsrf=ACYBGNSXXpS6YmAKUiLKKBs6xWb4uUY5gA:1581168823770&source=lnms&sa=X&ved=0ahUKEwioj8jwiMLnAhW9AhAIHbXTBMMQ_AUI3QUoAQ'
            raw_html = self._download_page(url)
            pair_p2 = -1
            j = 0
            links = []
            while j < limit:
                ## extract pair set
                pair_p1 = raw_html.find('<img class="rg_i', pair_p2 + 1)
                pair_p2 = raw_html.find('<div class="sMi44c', pair_p1)
                source_tmp = (raw_html[pair_p1:pair_p2])
                ## extract figure
                figure_p1 = source_tmp.find('src=')
                figure_tmp = (source_tmp[figure_p1+5:pair_p2])
                figure_p2 = figure_tmp.find('"',figure_p1+6)
                figure_link = (figure_tmp[0:figure_p2])
                ## extract site
                site_p1 = source_tmp.find('href="',figure_p2)
                site_tmp = (source_tmp[site_p1:pair_p2])
                site_p2 = site_tmp.find('"',10)
                site_link = (site_tmp[6:site_p2])
                # download figure
                path = root_dir + kw_search[i]

                # figure downloads
                filename = str(kw_search[i]) + "_" + '%04d' % (j + 1) + ".jpg"
                try:
                    ### save figures
                    urllib.request.urlretrieve(figure_link, os.path.join(path, filename))
                    ### append site address
                    links.append(site_link.replace('"', '  '))
                except Exception as e:
                    print(e)
                    j -= 1
                j += 1

                # end of while-loop
                with open(os.path.join('./' + root_dir + '/', str(kw_search[i]) + '.txt'), 'w') as f:
                    pbar = enumerate(tqdm(links))
                    for item_ind, item in pbar:
                        f.write(kw_search[i] + "-" + '%04d' %(item_ind + 1) + ":   " + "%s\n" % item)
                        time.sleep(0.01)
            i += 1
        # end of while-loop


    def _create_directories(self, root_dir, name):
        try:
            if not os.path.exists(root_dir):
                os.makedirs(root_dir)
                time.sleep(0.2)
                path = (name)
                sub_directory = os.path.join(root_dir, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)
            else:
                path = (name)
                sub_directory = os.path.join(root_dir, path)
                if not os.path.exists(sub_directory):
                    os.makedirs(sub_directory)

        except OSError as e:
            if e.errno != 17:
                raise
            pass
        return

    def _download_page(self, url):

        try:
            # return respData
            ##### browser extraction part ####
            browser = webdriver.Chrome()
            browser.get(url)
            time.sleep(1)

            element = browser.find_element_by_tag_name("body")
            # Scroll down
            for i in range(30):
                element.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.3)

            try:
                browser.find_element_by_id("smb").click()
                for i in range(50):
                    element.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.3)  # bot id protection
            except:
                for i in range(10):
                    element.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.3)  # bot id protection
            browser.find_element_by_xpath('//*[@id="islmp"]/div/div/div/div/div[5]/input').click()
            # scroll down2
            for i in range(30):
                element.send_keys(Keys.PAGE_DOWN)
                time.sleep(0.3)

            try:
                browser.find_element_by_id("smb").click()
                for i in range(50):
                    element.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.3)  # bot id protection
            except:
                for i in range(10):
                    element.send_keys(Keys.PAGE_DOWN)
                    time.sleep(0.3)  # bot id protectio
                    print("End of the searching pages")
                    time.sleep(0.5)
                    respData = browser.page_source #page source
                    # close the browser
                    browser.close()
                    return respData

        except Exception as e:
            print(e)
            exit(0)

#### help
parser = argparse.ArgumentParser(description='## Search and download images using Google engine ##', formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='''\
version history:
    [ver0.10]       release of this script (2020.07.21)

++ Copyright at uschoi@nict.go.jp / qtwing@naver.com ++
''')
parser.add_argument("Keyword", help="Keywords without space",)
parser.add_argument("Item_number", help="Searching item number")
# parser.add_argument("URL_output.txt", help="URL text files")
parser.add_argument('--version', action='version', version='Version 0.1')
parser.parse_args()

# assign arguments
keyword = sys.argv[1]
itemN = int(sys.argv[2])
# outputN = sys.argv[3]
root_dir = "gisd_figures/"

######### Main Run ##############################
response = gisd
address = response().down_url(keyword, itemN)


############ for further study ###################
# # rename for the future version
# for count, filename in enumerate(sorted(os.listdir('./' + root_dir + keyword + '/'))):
#     dst = str(keyword) + "-" + '%04d' % (count + 1) + ".jpg"
#     src = str('./' + root_dir + keyword + '/') + filename
#     dst = str('./' + root_dir + keyword + '/') + dst
#     os.rename(src, dst)
