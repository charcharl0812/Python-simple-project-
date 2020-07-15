from urllib import request
import re

class Spider():     
        
    root_pattern = '<div class="content__list--item--main">([\s\S]*?)</div>'
    name_pattern = 'html">([\s\S]*?)</a>'
    price_pattern = '<em>([\s\S]*?)</span>'

    def fetch_content(self):
        r = request.urlopen(web)
        htmls = r.read()
        htmls = str(htmls,encoding = 'utf-8')
        return htmls

    def analysis(self,htmls):
        root_html = re.findall(Spider.root_pattern,htmls)
        anchors=[]
        for html in root_html:
            name = re.findall(Spider.name_pattern,html)
            price = re.findall(Spider.price_pattern,html)
            anchor = {'name':name,'price':price}
            anchors.append(anchor)
        #print(anchors[0])
        return anchors

    def refine(self,anchors):
        l = lambda anchor: {
            'name':anchor['name'][0].strip(),
            'price':anchor['price'][0].replace('</em>','')
            }
        return map(l,anchors)

    def sort(self,anchors):
        anchors = sorted(anchors,key = self.sort_seed,reverse = True)
        return anchors

    def sort_seed(self,anchor):
        r = re.findall('\d*',anchor['price'])
        price1 = int(r[0])
        return price1


    def show(self,anchors):
        for num in range(0,len(anchors)):
            print('No.'+ str(num+1)+ ':'
            +anchors[num]['name']+ '--'
            +anchors[num]['price'])

        """ for anchor in anchors:
            print(anchor['name']+ '----'+ anchor['price']) """

    def go(self):
        htmls = self.fetch_content()
        anchors = self.analysis(htmls)
        anchors = list(self.refine(anchors))
        anchors = self.sort(anchors)
        self.show(anchors)

        
 #   def analysis(self,htmls):
       #root_html = re.findall(Spider.root_pattern,htmls)


url = []
for i in range (1,5):
    i += 1
    r = 'https://tj.zu.ke.com/zufang/nankai/pg'+ str(i) + '/#contentList' 
    url.append(r)  
print (url)
""" for web in url:
    spider = Spider()
    spider.go()   """      
