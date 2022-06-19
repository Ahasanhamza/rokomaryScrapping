from wapscrap import wlog 
from wapscrap import wscrap

urls   = ["https://rokomari.com/electronics/category/2051/Mouse?page=","https://rokomari.com/electronics/category/2050/Keyboard?page=","https://rokomari.com/electronics/category/2052/Pen%20drive%20and%20Flash%20drive%20?page=","https://rokomari.com/electronics/category/2035/Speaker?page=","https://rokomari.com/electronics/category/2043/Motherboard?page=","https://rokomari.com/electronics/category/2045/Hard%20Disk%20Drive?page=","https://rokomari.com/electronics/category/2047/Graphics-Card?page=","https://rokomari.com/electronics/category/1982/Science-Kit?page=","https://rokomari.com/electronics/category/2061/Headphone?page=","https://rokomari.com/electronics/category/2048/WebCam?page=","https://rokomari.com/electronics/category/2060/Router?page=","https://rokomari.com/electronics/category/2097/Antivirus?rpage=","https://rokomari.com/product/category/2086/product?ref=nm&page=","https://rokomari.com/giftfinder?page=","https://rokomari.com/book/category/80/rokomari-collection?ref=rok_pack&page=","https://www.rokomari.com/book/category/81/islamic?page=","https://www.rokomari.com/book/category/32/self-help--motivational-and-meditation?page=","https://www.rokomari.com/book/category/35/translated-books?page=","https://www.rokomari.com/book/category/14/computer--internet--freelancing-and-outsourcing?page=","https://www.rokomari.com/book/category/31/mathematics--science---technology?page=","https://www.rokomari.com/book/category/364/novel?page=","https://www.rokomari.com/book/category/403/english-language-books?page=","https://www.rokomari.com/book/category/406/west-bangal-books?page=","https://www.rokomari.com/book/category/408/mystery--detective--horror--thriller-and-adventure?page=","https://www.rokomari.com/book/category/410/science-fiction?page=","https://www.rokomari.com/book/category/11/children---teens?page=","https://www.rokomari.com/book/category/363/story?page=","https://www.rokomari.com/book/category/19/history-and-tradition?page=","https://www.rokomari.com/book/category/9/biographies--memories---interviews?page=","https://www.rokomari.com/book/category/12/collections---box-sets?page="]
filepath = "html/data.html"

wlog.set_coustom_log_info('html/error.log')
for link in urls:
    book_scrap = wscrap.RokomaryBooks(link,wlog)
    #for x in range(1,10):
        #book_scrap.retrieve_webpage(x)
        #book_scrap.write_wabpage_as_html(filepath)

   

    book_scrap.read_webpage_from_html(filepath)
    book_scrap.convert_data_to_bs4()
   
    #book_scrap.parse_soup_to_simple_html_electronic_items()
    #book_scrap.parse_soup_to_simple_html_stationary_itmes()
    #book_scrap.parse_soup_to_simple_html_giftvoucher_itmes()
    book_scrap.parse_soup_to_simple_html_book_items()
    

