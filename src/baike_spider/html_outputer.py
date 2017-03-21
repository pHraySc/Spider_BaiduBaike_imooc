# -*- coding: utf-8 -*-
'''
Created on 2017年3月12日

@author: Sccc
'''
from encodings.utf_8 import encode


class HtmlOutPuter(object):
    
    def __init__(self):
        self.datas = []
        
    def collect_data(self, data): #收集数据
        if data is None:
            return
        self.datas.append(data) #将data添加到列表的尾部
    
    def output_html(self):  #将收集好的数据写出到一个HTML页面当中
        fileOP = open('output.html', 'w')   #建立一个 '文件' 输出对象    写模式
        
        fileOP.write('<html>')
        #在html和body标签之间加上meta charset字符集设定为utf-8即可
        fileOP.write(r'<meta charset=utf-8>')
        fileOP.write('<body>')
        fileOP.write('<table>')
        
        for data in self.datas:
            fileOP.write('<tr>')
            fileOP.write('<td>%s</td>' % data['url'])
            fileOP.write('<td>%s</td>' % data['title'])
            fileOP.write('<td>%s</td>' % data['summary'])
            fileOP.write('</tr>')
        
        fileOP.write('</table>')
        fileOP.write('</body>')
        fileOP.write('</html>')
    
    
    
    



