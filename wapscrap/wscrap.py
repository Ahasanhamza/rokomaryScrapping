import requests
from bs4 import BeautifulSoup
import csv
import json


class RokomaryBooks:
    __url  = ""
    __data = ""
    __wlog = None
    __soup = None

    def __init__(self, url,wlog):
        self.__url  = url
        self.__wlog = wlog

    def retrieve_webpage(self,x):
        try:
            
            html = requests.get(self.__url + str(x))
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
        else:
            self.__data = html.content
            if len(self.__data) > 0:
                print("retrieve successfully")

    def write_wabpage_as_html(self, filepath, data=''):
        try:
            with open(filepath,'ab') as fobj:
                if data:
                    fobj.write(data)
                else:
                    fobj.write(self.__data)
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))
    
    def read_webpage_from_html(self,filepath):
        try:
            with open(filepath, encoding="utf8") as fobj:
                self.__data = fobj.read()
        except Exception as e:
            print(e)
            self.__wlog.report(str(e))

    def change_url(self,url):
        self.__url = url

    def print_data(self):
        print(self.__data)

    def convert_data_to_bs4(self):
        self.__soup= BeautifulSoup(self.__data,"html.parser")




    def parse_soup_to_simple_html_electronic_items(self):
        
        news_list1 =self.__soup.find_all('div', class_ = 'furnitureListItem')
        
        
        
    
       
        itme_list1 = []
        with open("html/electronics_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)       
            for product in news_list1:
                
                divice_name      =  product.find('h2').text.encode('utf-8').strip()
                
                divice_price     =  product.find('span',class_='presentPrice').text.encode('utf-8').strip()
                
                divice_details   =  product.find('ul').text.encode('utf-8').strip()
                
                
                
                
                
                
                prod = {
                    'divice_name'     : divice_name,
                    'divice_price'    : divice_price,
                    'divice_details'  : divice_details,
                    
                }
                
                itme_list1.append(prod)
                

                writer.writerow([divice_name, divice_price,divice_details])





    def parse_soup_to_simple_html_stationary_itmes(self):
        
        news_list2 =self.__soup.find_all('div', class_ = 'bookListItem')
        
        
        
    
       
        itme_list2 = []
        with open("html/stationary_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)       
            for product in news_list2:
                
                item_name      =  product.find('h2').text.encode('utf-8').strip()
                
                item_price     =  product.find('span',class_='presentPrice').text.encode('utf-8').strip()
                
                item_group_name   =  product.find('li').text.encode('utf-8').strip()
                
                
                
                
                
                
                prod = {
                    'item_name'     : item_name,
                    'item_price'    : item_price,
                    'item_group_name'  : item_group_name,
                    
                }
                
                itme_list2.append(prod)
                

                writer.writerow([item_name, item_price,item_group_name])




    def parse_soup_to_simple_html_giftvoucher_itmes(self):
        
        news_list3 =self.__soup.find_all('div', class_ = 'bookListItem')
        
        
        
    
       
        itme_list3 = []
        with open("html/giftvoucher_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)       
            for product in news_list3:
                
                gift_card_name      =  product.find('h2').text.encode('utf-8').strip()
                
                gift_card_price     =  product.find('span',class_='presentPrice').text.encode('utf-8').strip()
                
                
                
                
                
                
                
                prod = {
                    'gift_card_name'     : gift_card_name,
                    'gift_card_price'    : gift_card_price
                    
                    }
                
                itme_list3.append(prod)
                

                writer.writerow([gift_card_name, gift_card_price])




    def parse_soup_to_simple_html_book_items(self):
        
        news_list4 =self.__soup.find_all('div', class_ = 'book-text-area')
        
        
    
        
        itme_list4 = []
        with open("html/books_data.csv", "w") as csv_file:
            writer = csv.writer(csv_file)       
            for product in news_list4:
                
                book_name   = product.find('p',attrs={"class":"book-title"}).text.encode(encoding = 'UTF-8',errors = 'strict').rstrip()
                book_author = product.find('p',attrs={"class":"book-author"}).text.encode(encoding = 'UTF-8',errors = 'strict').rstrip()
                book_availability = product.find('p',attrs={"class":"book-status text-capitalize"}).text.encode(encoding = 'UTF-8',errors = 'strict').rstrip()
           
                book_price  = product.find('span').text.encode(encoding = 'UTF-8',errors = 'strict').rstrip()
                
                
                prod = {
                    'book_name'  : book_name,
                    'book_author': book_author,
                    'book_availability' : book_availability,
                    'book_price'  : book_price

                }
                itme_list4.append(prod)
                
        
                writer.writerow([book_name, book_author,book_availability,book_price])


        
      
    