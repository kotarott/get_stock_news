# get_stock_news
市況取得ツール  
ロイター、日経新聞（要アカウント）から記事を取得します。  
https://youtu.be/RZszAL7j0U0  
  
市況データ取得は今後対応予定  

  
## インストール
デスクトップアプリケーション用  
 pip install eel  
 pip install pyinstaller  
  
スクレイピング用  
 pip install selenium  
 pip install webdriver_manager  
 pip install threading  
  
その他  
 pip install investpy  
 ⇒市況データ取得用  
 
## デスクトップアプリ作成
python -m eel view.py web --onefile  
  
日経の記事を取得する場合はルートディレクトリにsecret.pyを作成  
nky_id="自分のメールアドレス"  
nky_pw="パスワード"  
2つの変数を作成しておく。  
