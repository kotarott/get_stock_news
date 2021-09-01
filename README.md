# get_stock_news
市況取得ツール
  
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