![PDF Unlocker Banner](images/banner.png)

# PDF解鎖工具 🔓

一個簡單、好用的線上 PDF 密碼移除工具，使用 Streamlit 開發。

**簡介**：上傳被密碼保護的 PDF 文件，輸入正確密碼，一鍵解鎖並下載無密碼版本。

## 功能亮點
- 支援使用者自行輸入密碼（不硬編碼，安全靈活）
- 完全在瀏覽器本地處理，不上傳檔案到伺服器
- 操作簡單：上傳 → 輸入密碼 → 點選解鎖 → 下載
- 介面清爽、直觀，適合學生、上班族快速使用

## 線上體驗
已部署版本（隨時可存取）：
👉 [Visit PDF unlock website ](https://pdf-unlock-app-chengmanyu.streamlit.app/)

## 本機運作步驟（3分鐘快速上手）

### 1. 環境要求
- Python 3.8 或以上

### 2. 安裝依賴
```bash
pip install streamlit pikepdf
```

3. 運行應用
```bash
# 進入專案資料夾
cd 你的專案目錄

# 啟動 Streamlit
streamlit run pdf_unlock_app.py
```

啟動後，瀏覽器會自動開啟 http://localhost:8501 ，即可使用。

4. 使用方法

1. 點擊「上傳你的PDF檔案」按鈕，選擇你需要解鎖的 PDF
2. 在「輸入PDF密碼」方塊中輸入檔案開啟密碼
3. 點擊藍色“解鎖PDF”按鈕
4. 成功後會出現「下載解鎖後的PDF」按鈕，點擊即可下載無密碼版本

**常見問題**:

- 密碼錯誤 → 會顯示“解鎖失敗：密碼不正確”
- 不是密碼保護的PDF → 會提示對應錯誤
- 檔案損壞 → 同樣會有錯誤提示

## 如何自行部署網路（免費）
使用 Streamlit Community Cloud（原 Streamlit Sharing），步驟如下：

1. 把專案推送到 GitHub（新公開倉庫）
2. 倉庫根目錄必須包含以下檔案：
    - pdf_unlock_app.py（主程式）
    - requirements.txt（內容如下）
        ```
        streamlit
        pikepdf
        ```

3. 造訪 https://share.streamlit.io/
4. 用 GitHub 帳號登入 → New app → 選擇你的倉庫 → 選擇主檔案 pdf_unlock_app.py → Deploy

部署成功後會獲得一個永久鏈接，例如：
https://你的倉庫名稱.streamlit.app


## 注意事項

- 本工具僅用於合法擁有的、你有權解鎖的文件
- 不支援非常複雜的權限保護（如憑證加密、編輯限制等），只處理最常見的「需要密碼才能開啟」情況
- 免費部署有使用量限制，適合個人/小範圍使用

## 許可證
MIT License - 隨意使用、修改、分享
有任何問題或改進建議，歡迎在 Issues 裡留言！

最後更新：2026年 2月 10日

祝你使用愉快～ 🚀
