# NewDailyReport 新自动填报

### 修改自 [DailyReport-SAU 沈航每日疫情填报](https://github.com/ShanshanHY/DailyReport-SAU)

## 如何使用

###

- **前置操作**
  1.  利用软件对`https://yqdwxx.sau.edu.cn/ADDJKTB`进行抓包，获取请求数据中的`"uid"`所对应的值（方法不提供）
  2.  Clone 本项目到本地，进入文件夹
  3.  打开`data.json`，按照个人实际信息填写，填入刚刚获取的`"uid"`并保存，遇到问题可以参考[data.demo.json](https://github.com/Bai-Zhi-shen/NewDailyReport/blob/main/data.demo.json)
  4.  ~~等我有时间可能会做出更方便的填写方式~~

###

- **本地运行（二选一）**
  1.  安装`python3`，并配置环境
  2.  运行`main.py`

###

- **利用 Github Actions 云端定时运行（二选一&推荐）**

  1.  首先登陆 Github 账户，并且[Fork](https://github.com/Bai-Zhi-shen/NewDailyReport/fork)本项目到你的仓库
  2.  依次打开`Settings`-`Secrets`-`Actions`-`New repository secret`![屏幕截图 2022-08-05 074444](https://user-images.githubusercontent.com/29966961/182973743-8ad295bb-a220-4487-b0fc-8b5a9873e097.png)
  3.  在`Name`栏中填入`DATA`,复制前面提到的`data.json`中的全部内容并粘贴到`Value`中并保存 (这里的图片来自之前的项目，不要在意图片中内容格式和你不一致的问题)![屏幕截图 2022-08-05 075140](https://user-images.githubusercontent.com/29966961/182974144-eb353697-df5b-4d3e-9b99-304a8d1cc9c0.png)
  4.  打开`Actions`选项卡，并同意启用`Workflows`![image](https://user-images.githubusercontent.com/29966961/182974440-b6c46243-8214-4b66-9893-80b7f3b7a8b3.png)
  5.  依次点击`Daily Report`-`Run workflow`-`Run workflow`测试填报是否正常![image](https://user-images.githubusercontent.com/29966961/182975156-50c6d79d-fb72-4c8f-bcd7-ed3a1f426b65.png)
  6.  若出现异常，请确保`pushkey`正确填写，并前往`PushDeer`检查填报内容
  7.  Github Actions 会自动在每日的`UTC+8:00 00：05`和`UTC+8:00 01：05`自动运行

  **注意！Github Actions 可能存在一定延迟(大概几十分钟后开始运行），如果有极其准确的时间要求，请自建服务器或使用腾讯云函数**

###

- **如果遇到任何问题，可以通过 issue 向我提出**

### 本人不对使用此脚本造成的任何后果负责！！！
