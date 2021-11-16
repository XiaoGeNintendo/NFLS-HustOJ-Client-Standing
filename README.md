# NFLS-HustOJ-Client-Standing
NFLS-HUSTOJ客户端比赛排行榜
# 项目缘由
NFLS-HUSTOJ关闭了排行榜功能，故实现。

# 使用方法（练习排行榜）
1. 登录[HustOJ](http://www.nfls.com.cn:20035/)或内网[HustOJ](http://192.168.188.77)并登录自己的账号
2. 按下F12，在">>"中选择"Application（应用）"，选择"Cookie"，选择"http://192.168.188.77" 或"http://www.nfls.com.cn:20035/" ,拷贝"PHPSESSID"的值
![p1](https://user-images.githubusercontent.com/34835642/141992653-afe2a6ec-6589-48a5-b9f3-991415403d38.PNG)
3. 打开`problemset.txt`，在第一行粘贴你的Session ID，第二行输入题目编号（逗号分隔），第三行请输入：

`http://192.168.188.77/judge/status.php?&problem_id=%s&top=%s`（内网）

`http://www.nfls.com.cn:20035/judge/status.php?&problem_id=%s&top=%s`（外网）

[查看样例](https://github.com/XiaoGeNintendo/NFLS-HustOJ-Client-Standing/blob/main/problemset.txt)

4. 保存文件，运行`spider.py`，确认信息无误后按下Enter。结果可以在`out_ps.html`中找到。
![out_ps](https://user-images.githubusercontent.com/34835642/141994272-7e7d1d5d-8c2c-49d7-a18e-7d6c7f47925e.png)

# 使用方法（比赛排行榜）
1. 登录[HustOJ](http://www.nfls.com.cn:20035/)或内网[HustOJ](http://192.168.188.77)并登录自己的账号
2. 按下F12，在">>"中选择"Application（应用）"，选择"Cookie"，选择"http://192.168.188.77" 或"http://www.nfls.com.cn:20035/" ,拷贝"PHPSESSID"的值
![p1](https://user-images.githubusercontent.com/34835642/141992653-afe2a6ec-6589-48a5-b9f3-991415403d38.PNG)
3. 打开`contest.txt`，在第一行粘贴你的Session ID，第二行输入比赛编号，第三行请输入：

`http://192.168.188.77/judge/status.php?&cid=%s&top=%s`（内网）

`http://www.nfls.com.cn:20035/judge/status.php?&cid=%s&top=%s`（外网）

[查看样例](https://github.com/XiaoGeNintendo/NFLS-HustOJ-Client-Standing/blob/main/contest.txt)

4. 保存文件，运行`spider2.py`，确认信息无误后按下Enter。结果可以在`out_contest.html`中找到。
![out_contest](https://user-images.githubusercontent.com/34835642/141994390-73ce36e7-d7d8-49a1-8479-1b30d635effb.png)


