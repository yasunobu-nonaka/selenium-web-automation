## 概要

Flaskで作成したログイン機能付きWebアプリに対し、
Seleniumを用いてログイン操作の自動化テストを行う。

## 構成

- Webアプリ: Flask
- 自動化: Selenium (Page Object Model)
- ブラウザ: Chrome (Headless)

## 自動化内容

- 正常ログイン/ログイン失敗の両ケースを自動化
- セッション制御の検証
- ページ遷移の確認

## 工夫点

- WebDriverWait を用いた安定した操作
- time.sleepを使用せず、URL遷移やDOM状態を明示的に待機
- Page Object Model の採用
- UI変更に強い構成
