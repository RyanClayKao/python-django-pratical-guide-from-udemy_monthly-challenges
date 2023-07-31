## Django專案進行 git版控及clone方式
------
### 資料夾層級
------
* django project 名稱資料夾(github reponsitoy名稱)
    * django project同名資料夾(若從github clone下來則會與外層資料夾名稱不同)
    * manage.py (django 主程式核心進入點)
    * django app資料夾
    * .gitignore 檔案(可以去 https://gitignore.io 下載django適用的檔案)
    * (requirement.txt) ==> 運行環境需裝的套件，可以理解為就是要給外層 venv虛擬環境 git clone後還原用的
* venv (python -m venv venv 來的虛擬環境)

### 專案從無到有建立方式
------
1. 在資料夾中開啟命令提示字元視窗，先建 python 的虛擬環境專案
    ``` powershell
        python -m venv venv
    ```
2. Windows作業系統來說，再輸入下方指令，進入到虛擬環境，會看到命令列的最開頭多了 (venv)
    ``` powershell
        venv\Scripts\activate
    ```

3. 安裝 Django
    ``` python
        pip install Django
    ```

4. 建立 Django專案 (這裡以 monthly_challenges為例)，會產生 monthly_challenges資料夾，裡面也會有一個同名的資料夾，如前述資料夾層級
    ``` python
        django-admin startproject monthly_challenges
    ```

5. 用 VS Code開啟最外層的專案資料夾(monthly_challenges)，在終端機裡面改用下面的指令來進入虛擬環境(venv)
    ``` powershell
        ..\venv\Scripts\activate
    ```

6. 建立 Django的app(這裡以 challenges為例)，會產生 challenges資料夾
    ``` python
        django-admin startapp challenges
    ```

### 建立 git版本控制及設定
------
1. 在 monthly_challenges資料夾(外層的那個)開啟命令提示自元視窗，或是使用 VS code開啟

2. 輸入git初始化指令，進行 git初始化
    ``` git
        git init
    ```

3. 進入虛擬環境(venv)
    ``` powershell
        ..\venv\Scripts\activate
    ```

4. 將虛擬環境有安裝的內容輸出到 requirements.txt文字檔中，輸入下方指令，產出檔案
    ``` python
        pip freeze > requirements.txt
    ```

5. 加入在 github已經開好的新 repository關聯    
    ``` git
        git remote add origin 你的github repository網址
    ```

6. 加入異動的資料到 git紀錄並commit，推送master分支到遠端
    ``` git
        git add .
        git commit -m 'git and django init' 
        git push origin master
    ```

### 從 github clone回來及還原虛擬環境，使專案能回來繼續運作
------
1. 建立本機的 repository資料夾，進到資料夾，開啟命令提示自元視窗或是用 VS Code開啟
    * 備註：在這個 repository同層狀況下，應該還要有虛擬環境的 venv在，才能做到後面第4點的虛擬環境套件還原

2. 從 github repository找到 clone的網址，輸入下方指令
    ``` git
        git clone 你的repository clone網址
    ```

3. 進入虛擬環境(venv)
    ``` powershell
        ..\venv\Scripts\activate
    ```

4. 輸入下方指令，將虛擬環境所需的套件還原回來
    ``` python
        pip install -r requirements.txt
    ```

5. 測試是否能夠把 Django跑起來
    ``` python
        python manage.py runserver
    ```