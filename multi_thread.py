import threading
import scraping


class multiThread(threading.Thread):
    def __init__(self, url, source):
        threading.Thread.__init__(self)
        self.url = url
        self.source = source

    def run(self):
        if self.source == "ro":
            result = scraping.get_ro_article(self.url)
            scraping.output_by_csv(result)
        else:
            result = scraping.get_nky_article(self.url)
            scraping.output_by_csv(result)