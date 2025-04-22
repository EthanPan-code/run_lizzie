# run_lizzie.exe

## 🧩 說明

這個 `.exe` 檔案是為了簡化 Lizzie 的啟動流程所設計的。  
使用者只需要雙擊 `run_lizzie.exe`，就能自動啟動 Lizzie。  
它會透過 `jre` 資料夾中的 Java 執行 `lizzie.jar`，**不需要額外安裝任何軟體**。

---

## 🚀 如何使用

請先下載以下 `.zip` 檔案：

1. `run_lizzie.zip`（本專案資料夾）
2. [`Lizzie.0.7.4.Windows.x64.GPU.zip`](https://github.com/featurecat/lizzie/releases/download/0.7.4/Lizzie.0.7.4.Windows.x64.GPU.zip)
3. `OpenJDK21U-jre_x64_windows_hotspot_xx.x.x_x.zip`  
   - 下載位置：[https://adoptium.net/temurin/releases/](https://adoptium.net/temurin/releases/)，選擇 **Windows 版 JRE 的 .zip 檔**

### 🛠 操作步驟

**第一步：**  
解壓縮上述所有 `.zip` 檔案，  
並將 `OpenJDK21U-jre_x64_windows_hotspot_xx.x.x_x` 資料夾重新命名為 `jre`。

**第二步：**  
將 `run_lizzie.exe` 和重新命名後的 `jre` 資料夾一起放入 `Lizzie.0.7.4.Windows.x64.GPU` 資料夾中。

**第三步：**  
雙擊 `run_lizzie.exe` 即可開始運行 Lizzie。

---

## ⚠️ 如果 `run_lizzie.exe` 被 Windows Defender 誤判為病毒

在某些情況下，Windows Defender 可能會誤判 `run_lizzie.exe` 為惡意程式並隔離。若發生此情況，請依以下步驟還原檔案：

### 🔄 還原方法

1. 開啟 **Windows 安全性**  
   - 可在開始選單中搜尋「Windows 安全性」
2. 前往 **病毒與威脅防護**
3. 往下捲動並點擊 **防護歷程記錄**
4. 找到最近與 `run_lizzie.exe` 相關的警告項目  
   - 通常會顯示為 *「發現嚴重威脅」* 等訊息
5. 點選該項目，選擇 **「動作」→「還原」**
6. 還原後請重新嘗試執行 `.exe` 檔案

> ✅ 此檔案 **沒有任何惡意行為**。之所以被封鎖，僅因為它是使用 PyInstaller 打包、且未簽署的自製啟動器。

---

## 📄 授權

本專案包含來自 [Lizzie 專案](https://github.com/featurecat/lizzie) 的開源程式碼，  
其授權方式為 **MIT License**。
