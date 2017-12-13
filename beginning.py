
import urllib.request


url_general = 'http://city.imd.gov.in/citywx/menu.php'

url = url_general.format()
print(url)
request = urllib.request.urlopen( url )
content = request.read().decode()
link=url

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
       for attr in attrs:
            if ('href' in attr):
               self.link=str(attr[1])



    # def handle_endtag(self, tag):
        # print ("Encountered an end tag :", tag)

    def handle_data(self, data):
        s=data
        s=s.lower().strip()
        # s=str(s)
        p="Bengaluru"
        p=p.lower()

        if s != '' and len(s) < 20:
            print("data",s)
            print("length",len(s))





        # if s == p :
        #     print ("s:",s)
        #     url = "http://city.imd.gov.in/citywx/"+self.link
        #     print(url)
        #     print(self.link)
        #     request = urllib.request.urlopen( url )
        #     content = request.read().decode()
        #     # print(content)
        #     # print(url)
        #     import webbrowser as webbrowser
        #     webbrowser.open(url, new=0, autoraise=True)




parser = MyHTMLParser()
parser.feed(content)
