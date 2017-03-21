# -*- coding: utf-8 -*-

'''
Created on 2017年3月12日

@author: Sccc
'''


class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()   #待爬取的URL列表
        self.old_urls = set()   #已爬取的URL列表
    
    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
            
    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)
    
    def has_new_url(self):
        return len(self.new_urls) != 0  #如果长度不为0就说明有待爬取的URL

    
    def get_new_url(self):
        new_url = self.new_urls.pop()   #用删除的方式删除掉列表最后一个URL并返回
        self.old_urls.add(new_url)
        return new_url

    
    
    
    
    
    
    
    
    



