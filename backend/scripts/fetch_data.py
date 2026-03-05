import csv
import json
import os
import urllib.request
import ssl
import io
from datetime import datetime

# 出力先ディレクトリ
OUTPUT_DIR = "../public/api"

# 気象庁エリアコードマッピング
JMA_AREA_CODES = {
    "hiroshima": "340000",
    "fukuoka": "400000",
    "nagoya": "230000"
}

# 5374.jpのデータ取得先マッピング
# Nagoyaは独自ドメインが無いため公式リポジトリのサンプル(金沢)等で仮置きし、後で調整可能にする
GOMI_URLS = {
    "hiroshima": "https://hiroshima.5374.jp/data/area_days.csv",
    "fukuoka": "https://fukuoka.5374.jp/data/area_days.csv",
    "nagoya": "https://raw.githubusercontent.com/codeforjapan/5374/master/data/area_days.csv"  # ダミー（通常は金沢市のデータ）
}

def fetch_jma_weather():
    """気象庁APIから天気を取得し、各地域ごとのJSONに保存"""
    print("Fetching weather data...")
    for area_key, area_code in JMA_AREA_CODES.items():
        url = f"https://www.jma.go.jp/bosai/forecast/data/forecast/{area_code}.json"
        
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req) as res:
                data = json.loads(res.read().decode('utf-8'))
                
                output_path = os.path.join(OUTPUT_DIR, f"weather_{area_key}.json")
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                    
            print(f"  - Saved weather for {area_key}")
            
        except Exception as e:
            print(f"  - Error fetching weather for {area_key}: {e}")

def fetch_5374_data():
    """5374.jpのCSVからゴミ収集日データを取得し、JSONに変換して保存"""
    print("Fetching 5374.jp data...")
    
    # SSL証明書エラーを回避するためのコンテキスト
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    
    for area_key, url in GOMI_URLS.items():
        try:
            req = urllib.request.Request(url)
            with urllib.request.urlopen(req, context=ctx) as res:
                raw_data = res.read()
                
                # 文字コードの判定（Shift_JIS / UTF-8）
                try:
                    decoded_data = raw_data.decode('utf-8-sig')
                except UnicodeDecodeError:
                    decoded_data = raw_data.decode('shift_jis')

                csv_reader = csv.DictReader(io.StringIO(decoded_data))
                areas = list(csv_reader)
                
                output_path = os.path.join(OUTPUT_DIR, f"gomi_{area_key}.json")
                with open(output_path, 'w', encoding='utf-8') as f:
                    json.dump(areas, f, ensure_ascii=False, indent=2)
                    
            print(f"  - Saved gomi data for {area_key}")
            
        except Exception as e:
            print(f"  - Error fetching gomi data for {area_key} at {url}: {e}")

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    meta_info = {
        "last_updated": datetime.now().isoformat()
    }
    with open(os.path.join(OUTPUT_DIR, "meta.json"), 'w', encoding='utf-8') as f:
        json.dump(meta_info, f, ensure_ascii=False, indent=2)
        
    fetch_jma_weather()
    fetch_5374_data()
    
    print("Data fetch completed.")

if __name__ == "__main__":
    main()
