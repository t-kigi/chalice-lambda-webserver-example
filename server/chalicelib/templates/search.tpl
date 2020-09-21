<!DOCTYPE html>
<html lang="ja">
<head>
  <title>{{ title or 'HELLO' }}</title>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="/css/style.css">
</head>
<body>
  <h1>Search Result</h1>
  <p>検索結果: {{ results|length }} 件</p>
  <ul>
  {% for item in results %}
    <li>{{ item }}</li>
  {% endfor %}
  </ul>
  <a href="/">トップへ戻る</a>
</body>
</html>
