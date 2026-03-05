# ロコ・ダッシュ (Loco Board)

地域密着型モバイルダッシュボード「ロコ・ダッシュ（仮）」のバックエンドリポジトリです。
本リポジトリでは、気象庁APIと5374.jpのデータを定期取得・JSON整形し、静的ファイルとしてCDN配信するための構成を管理します（Firebase等の動的バックエンド費用をゼロに抑えるためのアーキテクチャ）。

## 構成
- `.github/workflows/data_update.yml`: 定期的にデータを取得し、GitHub Pagesに公開するCI/CDパイプラインです。
- `backend/scripts/fetch_data.py`: 各自治体のデータを取得・整形するPythonスクリプトです。

## 技術スタック
- Python 3.12
- GitHub Actions (Cron)
- GitHub Pages (Hosting)
