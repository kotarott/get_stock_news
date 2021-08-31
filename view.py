import eel
import desktop
import scraping

app_name = "web"
end_point = "index.html"
size = (600,700)

@ eel.expose
def get_news_title(news_source, search_keyword):
    if news_source == "ro":
        return scraping.get_ro_news_title(search_keyword)
    elif news_source == "nky":
        return scraping.get_nky_news_title(search_keyword)

desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     df = get_news_title("ro", "欧州市場サマリー")
