# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: Sccc

爬虫主体
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    
    def __init__(self):     #构造函数中进行初始化
        self.urls = url_manager.UrlManager()    #URL管理器
        self.downloader = html_downloader.HtmlDownLoader()      #URL下载器
        self.parser = html_parser.HtmlParser()      #解析器
        self.outputer = html_outputer.HtmlOutPuter()    #输出
        
    def craw(self, root_url):
        count = 1 #记录当前爬取的URL
        #将入口URL添加进管理器
        self.urls.add_new_url(root_url)
        #启动爬虫循环
        while self.urls.has_new_url():  #当URL管理器中有待爬取的URL时，取出一个URL
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s'%(count, new_url)
                #拿到URL后启动URL下载器下载网页并存储在html_content
                html_content = self.downloader.download(new_url)
                #调用解析器来解析这个页面，得到页面数据，传入当前爬取的URL和下载好的URL数据内容
                new_urls, new_data = self.parser.parse(new_url, html_content)   #得到获得的URL列表，和新的数据
                #将新获得的URL列表添加进URL管理器
                self.urls.add_new_urls(new_urls)    #上面是添加单个的URL，这里是批量添加URL到管理器
                self.outputer.collect_data(new_data)    #收集数据到outputer中
                
                #这里判断count，超过1000循环结束
                if count == 1000:
                    break
                
                count += 1
            except:
                print 'craw failed' #标记此URL爬取失败
            
            '''
                1.如果有待爬取的URL，取出一个；
                2.下载对应的页面；
                3.下载之后进行页面的解析；
                4.解析后得到新的URL和数据；
                5.将新的URL补充进管理器，并收集这个循环过程中获得到的数据。
            '''
        #调用outputer的方法来输出收集好的数据
        self.outputer.output_html()
        
    
    



if __name__ == '__main__':
    root_url = 'http://baike.baidu.com/item/Python?sefr=ps'     #入口URL
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)       #craw方法来启动爬虫
