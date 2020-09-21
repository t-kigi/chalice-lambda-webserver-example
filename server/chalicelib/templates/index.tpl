<!DOCTYPE html>
<html lang="ja">
<head>
  <title>{{ title or 'HELLO' }}</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <h1>Lambda Web Hosting</h1>
  <p>バックエンドとして AWS Lambda + Chalice (Python) で Flask/Bottle っぽく動かして見るサンプルです。</p>
  <h2>Load Static Files</h2>
  <p>h1タグに別のファイル /css/style.css から読み取られたスタイルが当たっています。</p>
  <p>画像は以下の通りです。</p>
  <img src="/images/sample.png"/><br>
  <p>JavaScriptも読み込まれています。</p>
  <span id="counter">0</span><br>
  <button id="button" type="button">カウンター (ボタンを押すと数値を加算します)</button>
  <h2>Form Post</h2>
  <p>内部で持っているデータベースモックから一致するものを取得します。</p>
  <form method="POST" action="/search">
    <label>検索キーワード: </label>
    <input type="text" name="keyword" value="" />
    <br>
    <button type="submit">検索</button>
  </form>
  <script src="/js/index.js"></script>
</body>
</html>
