# 学！辐！光！说！话！

可！以！学！辐！光！说！话！

## 源项目相关内容

本项目修改自[Anan-s-Sketchbook-Chat-Box](https://github.com/MarkCup-Official/Anan-s-Sketchbook-Chat-Box)

有！相！当！多！的！修！改！

源项目相关视频见：

* [夏目安安传话筒](https://www.bilibili.com/video/BV1Up1tBgEkr)
* [夏目安安传话筒使用教学](https://www.bilibili.com/video/BV16G1mBUECy)

## AI声明

源项目90%的代码由AI生成

## 部署

本项目只支持windows

依赖库安装:

```cmd
pip install -r requirements.txt 
```
## 使用

### 运行源文件

#### 启动
在任意终端运行`main.py`即可

可在源文件所在位置通过右键菜单点击`在终端中打开`，输入下面命令

```powershell
python .\main.py
```

输出就像：

```powershell
PS [源文件所在路径]\TheRadianceInfection> python .\main.py 
Starting...
Hot key bind: True
Press f1 to trans
```

在最后一行会提示设置的`热键`(`HOTKEY`)

此时开始程序开始运行，并且会清空剪切板

!!!注意!!!

    *如果您的剪切板有**重要内容**，请**提前备份***

#### 运行

可在qq或者其他你需要替换文本的地方输入文本后，按下`热键`(`HOTKEY`)

这时程序会清空剪切板并剪切原文本框内所有内容(通过`ctrl+a`与`ctrl+x`快捷键实现)

然后便会自动插入字符、加入剪切板、粘贴并发送(这些操作都可以在`config.py`中配置)

每次按下`热键`(`HOTKEY`)后终端可见增加的文本如下

```powershell
Start generate...
Get Text: 测试文本
Combine Text: ……测！试！文！本！……
Start generate...
Get Text: 另一条测试文本
Combine Text: ……另！一！条！测！试！文！本！……
```

如果发送失败等可以尝试适当增大`main.py`第10行的`DELAY`

#### 终止

在终端按下`ctrl+c`即可

## 修改配置参数

于`config.py`中修改相关的参数即可，保存后重启应用程序生效

相关解释见注释内容

# 修改日志

见[CHANGELOG.md](./CHANGELOG.md)
