# 費用最小化・負荷軽減 バックエンド構築タスク

- [x] 1. リポジトリ・ホスティング環境準備
  - [x] GitHub Actions用の実行環境構成
  - [x] 静的ファイル配信先（Firebase Hosting / GitHub Pages等）のセットアップ
- [x] 2. データ取得・整形スクリプト作成（Python）
  - [x] 気象庁の公開APIデータ取得関数とJSON整形処理
  - [x] 5374.jpの公開CSV取得とJSON化処理
- [ ] 3. CI/CDパイプライン構築（GitHub Actions）
  - [ ] GitHub Actionsのスケジュール実行設定（cron）
  - [ ] JSON生成後、静的ホスティング環境への自動デプロイ処理の構築
- [ ] 4. 動作検証
  - [ ] スクリプトが自動実行され、意図通りのJSONが生成・公開されるか確認
