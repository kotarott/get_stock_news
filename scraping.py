import os
from numpy import NaN
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time
import pandas as pd
import datetime
from webdriver_manager.chrome import ChromeDriverManager
import secret

# Chromeを起動する関数
def set_driver(driver_path, headless_flg):
    if "chrome" in driver_path:
        options = ChromeOptions()
    else:
        options = Options()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    if "chrome" in driver_path:
        return Chrome(ChromeDriverManager().install(), options=options)
    else:
        return Firefox(executable_path=os.getcwd()  + "/" + driver_path,options=options)

# ニュース一覧の取得
def get_ro_news_title(search_keyword):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)

    url = "https://jp.reuters.com/search/news?blob=" + search_keyword.replace(' ', '+') + "&sortBy=date&dateRange=all"

    driver.get(url)
    time.sleep(2)

    news_titles = driver.find_elements_by_css_selector(".search-result-indiv .search-result-title")
    news_dates = driver.find_elements_by_css_selector(".search-result-indiv .search-result-timestamp")
    time.sleep(2)
    news_links = get_links(news_titles)

    # 空のDataFrame作成
    df = pd.DataFrame()
    for count, (title, news_link, news_date) in enumerate(zip(news_titles, news_links, news_dates)):

        df = df.append(
                {"title": title.text,
                "link": news_link,
                "date": news_date.text}, 
                ignore_index=True)
    
    driver.close()
    return list(df["title"]), list(df["link"]), list(df["date"])

def get_ro_article(url):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", True)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    
    driver.get(url)
    time.sleep(2)

    news_title = driver.find_element_by_css_selector(".ArticlePage-article-header-23J2O .ArticleHeader-headline-NlAqj")
    news_date = driver.find_element_by_css_selector(".ArticlePage-article-header-23J2O .ArticleHeader-date-line-3oc3Y")
    news_wrapper = driver.find_element_by_css_selector(".ArticleBodyWrapper")
    news_content = news_wrapper.find_element_by_tag_name("pre")

    df = pd.DataFrame()
    df = df.append(
            {"title": news_title.text,
            "article": news_content.text,
            "date": news_date.text}, 
            ignore_index=True)
    
    return df

def get_links(news_titles):
    news_links = []
    for news_title in news_titles:
        a_tag = news_title.find_element_by_tag_name("a")
        link = a_tag.get_attribute("href")
        news_links.append(link)
    return news_links

def get_nky_news_title(search_keyword):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    
    driver.get("https://www.nikkei.com/login")
    time.sleep(2)
    id = driver.find_element_by_id("LA7010Form01:LA7010Email")
    id.send_keys(secret.nky_id)
    pw = driver.find_element_by_id("LA7010Form01:LA7010Password")
    pw.send_keys(secret.nky_pw)

    driver.execute_script('document.querySelector(".btnM1").click()')
    time.sleep(1)

    url = "https://r.nikkei.com/search?keyword=" + search_keyword + "&volume=20"

    driver.get(url)
    time.sleep(2)

    news_titles = driver.find_elements_by_css_selector(".search__result-item .nui-card__title")
    news_dates = driver.find_elements_by_css_selector(".search__result-item .nui-card__meta")
    time.sleep(2)
    news_links = get_links(news_titles)
    
    # 空のDataFrame作成
    df = pd.DataFrame()
    for count, (title, news_link, news_date) in enumerate(zip(news_titles, news_links, news_dates)):

        df = df.append(
                {"title": title.text,
                "link": news_link,
                "date": news_date.text}, 
                ignore_index=True)
    
    driver.close()
    return list(df["title"]), list(df["link"]), list(df["date"])

def get_nky_article(url):
    # driverを起動
    if os.name == 'nt': #Windows
        driver = set_driver("chromedriver.exe", False)
    elif os.name == 'posix': #Mac
        driver = set_driver("chromedriver", False)
    
    driver.get("https://www.nikkei.com/login")
    time.sleep(2)
    id = driver.find_element_by_id("LA7010Form01:LA7010Email")
    id.send_keys(secret.nky_id)
    pw = driver.find_element_by_id("LA7010Form01:LA7010Password")
    pw.send_keys(secret.nky_pw)

    driver.execute_script('document.querySelector(".btnM1").click()')
    time.sleep(1)

    driver.get(url)
    time.sleep(2)

    if "style" in url:
        df = pd.DataFrame()
        df = df.append(
                {"title": "日経スタイルの記事は取得できません",
                "article": "日経スタイルの記事は取得できません",
                "date": "日経スタイルの記事は取得できません"}, 
                ignore_index=True)
    else:
        news_title = driver.find_element_by_css_selector(".container_c1oucich .title_tyodebu")
        news_date = driver.find_element_by_css_selector(".container_c1oucich .TimeStamp_t165nkxq")
        news_contents = driver.find_element_by_css_selector(".container_c1oucich .container_cz8tiun")

        df = pd.DataFrame()
        df = df.append(
                {"title": news_title.text,
                "article": news_contents.text,
                "date": news_date.text}, 
                ignore_index=True)

    return df

# CSV作成関数
def create_csv(data, file_name="company_list.csv"):
    num = 0
    while num == 0:
        if os.path.exists(file_name):
            print(f"ファイル名{file_name}は存在します。")
            num = 0
            file_name = input("ファイル名を入力してください >>>")
            file_name += ".csv"
        else:
            data.to_csv(file_name)
            create_log(f'ファイル名:{file_name} を作成しました。')
            return print("ファイルを作成しました。")

# ログ作成関数
def create_log(comment):
    path = "log.csv"
    now = datetime.datetime.now()
    time_stamp = now.strftime("%Y/%m/%d %H:%M:%S")
    logs = ','.join([time_stamp, comment])

    if not os.path.exists(path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(logs)
    else:
        with open(path, 'a', encoding='utf-8') as f:
            f.write('\n' + logs)


if __name__ == "__main__":
    # df = get_nky_news_title("サマリー")
    # print(list(df[1]))
    # url = "https://jp.reuters.com/article/idJPL4N2PV3F8"
    # get_ro_article(url)
    # url = "https://style.nikkei.com/article/DGXMZO54372300U0A110C2000000"
    # get_nky_article(url)
    df = get_ro_news_title("欧州市場サマリー")
    print(df)