# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: Sccc
'''
import urllib2


class HtmlDownLoader(object):
    
    
    def download(self, url):#只有一个参数就是要下载的URL
        if url is None:
            return None
        
        response = urllib2.urlopen(url)
        
        if response.getcode() != 200:
            #不等于200说明请求失败
            return None
        
        return response.read()
    
    



