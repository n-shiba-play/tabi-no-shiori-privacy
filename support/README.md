# Shioring. サポートページの公開準備

この `support/` は、既存のプライバシーポリシー用 GitHub Pages リポジトリ
[`n-shiba-play/tabi-no-shiori-privacy`](https://github.com/n-shiba-play/tabi-no-shiori-privacy)
の**ルートに追加するための完成フォルダ**です。アプリの Git リポジトリは別なので、
このフォルダをアプリ側だけへ commit しても Pages には公開されません。

2026年9月20日時点で公開リポジトリの `main` にはルートの `index.html` があり、
`https://n-shiba-play.github.io/tabi-no-shiori-privacy/` で既存のポリシーを閲覧できました。
Pages の実際の配信元ブランチ・ディレクトリは、公開画面だけでは確認できません。
リポジトリの管理者が **Settings → Pages** で確認してください。

## 公開手順（ユーザーが実施）

1. GitHub の `tabi-no-shiori-privacy` リポジトリの **Settings → Pages** で、現在の公開元ブランチとディレクトリを確認します。既存設定は変更しません。
2. その公開ディレクトリのルートへ、この `support/` フォルダを丸ごとコピーします。既存の `index.html` は上書きしません。
3. ご自身で差分を確認し、commit / push します。Pages の反映後、`https://n-shiba-play.github.io/tabi-no-shiori-privacy/support/` を開きます。
4. スマートフォン・PCで画像、問い合わせ先、プライバシーポリシーへのリンクを確認してから、App Store Connect のサポートURLへ登録します。

ページの外部リンクは既存の公開ポリシーと、そのポリシーが案内しているお問い合わせフォームだけです。Google Fonts、解析タグ、外部動画サービスは使用しません。

## 操作画像

`assets/images/help-*.jpg` は、アプリ本体の `AppStoreAssets/raw/` に保存済みの実際の iOS Simulator 画面から切り出したものです。表示している「秋の京都旅」は架空のデモ旅行です。再生成には `tools/prepare_images.py` と Pillow を使用します。画像の文字やボタンは描き直していません。

## 動画を後から追加する方法

現在、操作動画は未同梱です。サポート本文と画像だけで基本操作を確認できます。動画を追加したい場合、**完成した MP4 を `assets/videos/basic-guide.mp4` に置くだけ**で、ページ上の動画欄が自動表示されます。ファイルがない間は動画欄が隠れ、ページの読み込みを妨げません。動画は自動再生せず、ユーザーが再生したときだけ読み込みます。

録画の推奨手順：

1. Xcode で Shioring. を iOS Simulator に起動し、個人情報のない架空の旅行データを使用します。通知が映らないようにします。
2. Terminal で `xcrun simctl io booted recordVideo --codec h264 --mask ignored basic-guide.mp4` を実行します。録画を止めるときは **Control-C** です。Apple の [Simulator解説](https://developer.apple.com/jp/videos/play/wwdc2020/10647/) にある標準機能です。
3. 目安は **30〜60秒**。旅行一覧の「＋」から旅行名・日程を入力して保存 → DAYの「予定」から1件追加 → DAY地図を開く → 旅行詳細のPDFボタンからプレビュー、という順に操作します。待ち時間や入力に迷った時間は編集でカットします。
4. 音声・BGMは不要です。実際のアプリ画面だけを残し、Macのデスクトップ・通知・個人情報が入っていないか再生して確認します。
5. H.264のMP4として保存し、ファイルサイズを確認します。高解像度で大きい場合は macOS の書き出し機能等で縮小・圧縮し、画面の文字が読める品質を維持します。目標は数MB程度です。
6. `support/assets/videos/basic-guide.mp4` として配置し、Safari（iPhone）で再生・一時停止・画面幅を確認します。

動画の自動表示は `assets/site.js` が同じディレクトリのMP4を HEAD で確認するだけで、動画本体は `preload="none"` です。GitHub Pagesで公開した状態で確認してください。
