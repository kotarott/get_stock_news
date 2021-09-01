import eel
import desktop
import scraping
import multi_thread

app_name = "web"
end_point = "index.html"
size = (600,700)

@ eel.expose
def get_news_title(news_source, search_keyword):
    if news_source == "ro":
        return scraping.get_ro_news_title(search_keyword)
    elif news_source == "nky":
        return scraping.get_nky_news_title(search_keyword)

@ eel.expose
def get_articles(url_list):
    scraping.create_folder()
    thread_list = []
    for url in url_list:
        if "nikkei" in url:
            t = multi_thread.multiThread(url, "nky")
        else:
            t = multi_thread.multiThread(url, "ro")
        t.start()
        thread_list.append(t)

    for thread in thread_list:
        thread.join()


desktop.start(app_name,end_point,size)
#desktop.start(size=size,appName=app_name,endPoint=end_point)

# if __name__ == "__main__":
#     df = get_news_title("ro", "欧州市場サマリー")
