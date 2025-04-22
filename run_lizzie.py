import subprocess
import os
import sys

# 定位到 Lizzie 資料夾（這個 .exe 所在處）
base_dir = os.path.dirname(sys.executable if getattr(sys, 'frozen', False) else __file__)
os.chdir(base_dir)

# 使用內建 JRE 啟動 Lizzie
java_path = os.path.join(base_dir, "jre", "bin", "java.exe")
lizzie_jar = os.path.join(base_dir, "lizzie.jar")

try:
    subprocess.run([java_path, "-jar", lizzie_jar])
except FileNotFoundError:
    print("找不到內建 Java，請確認 jre/bin/java.exe 是否存在。")
except subprocess.CalledProcessError as e:
    print(f"Lizzie 執行錯誤：{e}")
