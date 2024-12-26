當你 clone 下來這個檔案時，請執行以下步驟：

1. 進入專案目錄：

   ```bash
   cd /你的路徑/登入註冊功能
   ```

2. 安裝專案依賴：

   ```bash
   poetry install
   ```

3. 進行資料庫遷移：
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
