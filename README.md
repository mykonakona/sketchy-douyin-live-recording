# 简陋douyin直播录制gui

## v0.0.2
ffmpeg总是断掉，太不稳定了。所以录制的部分打算改掉，现在把[OpenCRS](https://github.com/KamijoToma/OpenCRS)拿来用了，但还没有机会做测试。

## 简介
python大作业水平，一个把各种代码拿来用的缝合怪，抄了以下代码：

- https://github.com/wbt5/real-url
- http://www.codezd.com/experience/279.html
- https://www.liaoxuefeng.com/wiki/1016959663602400/1017786914566560

## 环境
Windows

## 打包

建议使用pycharm，完成环境配置与依赖安装后，执行：

`pipinstaller -F main.py -p gui.py -p realurl.py -p record.py`

可生成可执行文件main.exe

## 使用

1. 下载ffmpeg.exe另存至main.exe同一目录
2. 打开douyin，点击“更多”-“分享”-“复制链接”
3. 打开main.exe，填入刚得到的链接，点击“开始录制”，会在同目录下生成名为output.mp4的录制文件
4. 如需截断录制，可在同时打开的命令行窗口内输入q并回车（可能需要多试几次）

 