# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: Sccc
'''
from bs4 import BeautifulSoup  # @UnresolvedImport
import re
import urlparse

class HtmlParser(object):
    
    
    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        #/view/123.htm
        links = soup.find_all('a', href = re.compile(r'/view/\d+\.htm'))
        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)  #将new_url按照page_url的格式进阶成一个完全URL
            new_urls.add(new_full_url)
        return new_urls
    
    def _get_new_data(self, page_url, soup):
        res_data = {}
        
        #url
        res_data['url'] = page_url
        
        #<dd class="lemmaWgt-lemmaTitle-title">    <h1>Python</h1>
        title_node = soup.find('dd', class_ = 'lemmaWgt-lemmaTitle-title').find('h1')
        res_data['title'] = title_node.get_text()
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div', class_ = 'lemma-summary')
        res_data['summary'] = summary_node.get_text()
        
        return res_data
    
    def parse(self, page_url, html_content):
        #此方法需要我们从content中解析出新的URL列表和新的数据
        if page_url is None or html_content is None:
            return
        
        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data
    
    



