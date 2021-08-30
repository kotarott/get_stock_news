import eel
import desktop
import common.ro_scraping as ro_scraping

app_name = "web"
end_point = "index.html"
size = (600,700)

@ eel.expose
def get_news_title(news_source, search_keyword):
    if news_source == "ro":
        ro_scraping.get_news_title(search_keyword)
    elif news_source == "bb":
        pass

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     df = get_news_title("ro", "欧州市場サマリー")
