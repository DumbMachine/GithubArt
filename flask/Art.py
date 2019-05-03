# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import datetime
import os
import subprocess
from datetime import timedelta
import sys

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image


class GithubArt:

    def __init__(self,github_email=None, github_name=None,year='2007'):

        self.years = {
            '2019': 'Apr 29 2019', 
            '2018': 'Dec 31 2018', 
            '2017': 'Jan 1 2017', 
            '2016': 'Dec 25 2015', 
            '2015': 'Dec 28 2014', 
            '2014': 'Dec 29 2013', 
            '2013': 'Dec 30 2012', 
            '2012': 'Jan 1 2012', 
            '2011': 'Dec 26 2011', 
            '2010': 'Dec 27 2009', 
            '2009': 'Dec 28 2008', 
            '2008': 'Dec 30 2007', 
            '2007': 'Dec 31 2006', 
            '2006': 'Jan 1 2006', 
            '2005': 'Dec 24 2004', 
        }
        self.year = self.years[year]
        # self.year = 'Jan 1 2017'
        self.start  = datetime.datetime.strptime(self.year, '%b %d %Y')
        # if github_email!=None and github_name!=None:    
        #     self.command = 'git commit --allow-empty --author="{} <{}>" --date="date1 14:00 +0100" -m "fake commit for tile-art"'.format(github_name,github_email)
        # else:
        self.command = 'git commit --allow-empty --date="date1 14:00 +0100" -m "fake commit for tile-art"'
        self.commit = "git push origin master"
        self.uncommit = 'git clean -f -d'
        # self.location = r'C:\Users\ratin\Downloads\69.png'
        self.location = './gay.png'


    @classmethod
    def cleanup(cls):
        '''
        Deleting the temp files
        '''
        os.remove('tmp.png')
        os.remove('tmp.png')


    @classmethod
    def cnv_channel(cls, location):
        '''
        Converts RGBA image to RBG (4 channel --> 3 channel)

        Parameters
        ----------
        None 


        Returns
        ----------
        None

        '''
        png = Image.open(location)
        png.load()

        background = Image.new("RGB", png.size, (255, 255, 255))
        background.paste(png, mask=png.split()[3]) # 3 is the alpha channel

        background.save('temp.jpg', 'JPEG', quality=90)


    @classmethod
    def cnv_rgb_bw(cls):
        from PIL import Image
        col = Image.open("temp.jpg")
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<128 else 255, '1')
        bw.save("temp.png")

    
    @classmethod
    def cnv_DataURL_image(cls,arr):
        from base64 import b64decode
        _, encoded = arr.split(",", 1)
        data = b64decode(encoded,'-_')
        with open(r"gay.png", "wb") as f:
            f.write(data)
        # from base64 import decodestring
        
        # fh = open("imageToSave.png", "wb")
        # fh.write(str(arr.split(",")[1].decode('base64')))
        # fh.close()
        # _, encoded = arr.split(",", 1)
        # data = b64decode(encoded)

        # with open("image.png", "wb") as f:
        #     f.write(data)
        # arr = "data:image/png;base64,iVBORw0KGg..."
        # print(type(arr))
        # arr = str.encode(arr)
        # print(type(arr))
        # fh = open("data.png", "wb")
        # fh.write(str(arr.split(",")[1].decode('base64')))
        # fh.close()

    def do_the_thing(self):
        '''
        Converts RGBA image to RBG (4 channel --> 3 channel)

        Parameters
        ----------
        None 


        Returns
        ----------
        None

        '''
        # return "high"
        err=None
        something = plt.imread("temp.png")
        for i in range(0,something.shape[0]):
            for j in range(0,something.shape[1]):
                if something[i][j]==0:            
                    proc = subprocess.Popen(self.command.replace('date1',(self.start+timedelta(days = i+j*7)).strftime("%Y-%m-%d")), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
                    out, err = proc.communicate()
                    out.decode()
        if err:
            return "err"
        else:
            return self.command.replace('date1',(self.start+timedelta(days = i+j*7)).strftime("%Y-%m-%d"))                                 

    def everything(self):
        self.cnv_channel(self.location)
        self.cnv_rgb_bw()
        return self.do_the_thing()

    def finish(self):
        proc = subprocess.Popen(self.commit, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, _ = proc.communicate()
        out.decode()

    # def unfinish(self):
