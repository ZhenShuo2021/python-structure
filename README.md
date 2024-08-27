這是一個基本 Python 專案架構，是記錄也算教學
# Python 專案基本架構
本文旨在撰寫一個最精簡的教學，網路上的教學東扯西扯，講什麼直譯器，會查這些問題的就是新手，誰管你什麼直譯器。  
文章的順序是依照剛開始寫程式的人寫的，從第一個檔案開始
1. 看到大家都用 `__name__`
2. 光是單個檔案就可以很亂，學習變數命名
3. 檔案越來越多，分成多個檔案後的專案架構
4. 有架構後如何正確 import


# 什麼是 \_\_name\_\_ == "\_\_main\_\_"   
***避免特定程式在 import 時被執行。***   

就一句話！！！到底為什麼可以寫成一整篇文章，有夠白癡。  
詳細原因：為了避免特定程式在 import 時被執行，Python 執行時會為每個文件建立 `__name__` 屬性，當文件是頂層腳本直接執行時被設定為`"__main__"`，其餘則為模組的名稱，以此區別主程式和被引入的程式。

整個解釋就五句話。

延伸閱讀：`Python 執行時` 這句話也太攏統了吧，看[Python 到底怎麼被執行？](https://medium.com/citycoddee/python%E9%80%B2%E9%9A%8E%E6%8A%80%E5%B7%A7-5-python-%E5%88%B0%E5%BA%95%E6%80%8E%E9%BA%BC%E8%A2%AB%E5%9F%B7%E8%A1%8C-%E7%9B%B4%E8%AD%AF-%E7%B7%A8%E8%AD%AF-%E5%AD%97%E7%AF%80%E7%A2%BC-%E8%99%9B%E6%93%AC%E6%A9%9F%E7%9C%8B%E4%B8%8D%E6%87%82-553182101653)

# 如何命名變數
請參照[码农高天](https://www.youtube.com/watch?v=x6I8x-40w6k)的影片，說的非常好，這裡簡單整理摘錄。  

> 學習標準變數命名方式可以一眼看出變數的類型，增加資訊密度。
- 全部大寫：常數
- 駝峰式 (camel case)：類別 (class)
- 小寫加上底線：函式 (def)，一般變數
- 前置單底線：隱藏函式，沒有強制效果
- 前置雙底線：隱藏函式，具有強制效果，用名字修飾 (name mangling) 實現
- 前後雙底線：魔法物件，PEP8 就是這樣寫的，會看這篇文章的不要用

**import 也有順序**   

根據[官方建議 (PEP8)](https://peps.python.org/pep-0008/)，建議絕對導入，並且順序為

1. 標準庫  
2. 第三方套件  
3. 本機程式  

以前知道這些但是沒有照做，照做之後真的好讀很多，果然規定要遵守。

# 專案架構
當程式越寫越複雜需要切成多檔案，應該會變成這樣：

```md
root/.
├── README.md                # 簡介、安裝和使用說明
├── requirements.txt         # 專案的套件依賴和版本要求
├── setup.py                 # 進階的 Python 依賴管理，發在 pypi 需要用到
├── setup.cfg                # 配合 setup.py
├── main.py                  # 主執行檔，入口檔案
├── src
│   └── package
│       ├── __main__.py      # 設定當目錄被作為套件 (package) 直接執行時要執行的程式碼
│       ├── __init__.py      # 設定當目錄被作為套件 (package) 直接執行時要初始化的程式碼，也將目錄標記為 Package
│       ├── module1.py       # 模組檔案
│       ├── module2.py       # 模組檔案
│       └── utils
│           └── util.py      # 工具模組檔案
└── test
    └── test.py              # 測試程式碼 (unittest)
```

## 如何 import
分為相對導入和絕對導入，PEP8 建議絕對導入因為更好偵錯。
```python
# 相對導入
from . import module1
from .utils import util
# 絕對導入
from src.modules import module1
from src.modules.utils import util
```

不建議使用 PYTHONPATH 新增系統路徑，僅作為最後手段使用。  

延伸閱讀：[相對導入](https://stackoverflow.com/questions/14132789/relative-imports-for-the-billionth-time)


## 如何偵錯
建立 [`.vscode/launch.json`](https://stackoverflow.com/a/78060960/26993682) ，然而，此方法我測試無法使用相對引入。


## 如何呼叫模組（什麼是 python -m）
Python 導入 (import) 時根本不知道你的資料夾結構，所以**單獨執行** module2 時不管是相對引入還是絕對引入都會報錯，正確的呼叫方式是`python3 -m module2` 告訴 Python 把模組當作腳本執行。

原理：不重要，你又不會去改[這個](https://a7744hsc.github.io/python/2018/05/03/Run-python-script.html)。


## 模組和套件的差異
關於模組 (Module) 和套件 (Package) 的差異，前面說到  

> 當文件是頂層腳本直接執行時被設定為`"__main__"`，其餘則為模組的名稱    

套件就是一堆模組的集合，只是一個名詞，不重要。



