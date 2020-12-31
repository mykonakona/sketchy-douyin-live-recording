import subprocess as sp

def exec_ffmpeg(input_file):
    FFMPEG_BIN = "ffmpeg.exe"
    #input_file = 'http://pull-flv-l13.douyincdn.com/stage/stream-684444605647421880_or4.flv'
    output_file = '.\output.mp4'

    # 转码命令
    cmd = [FFMPEG_BIN,
           '-i', input_file,
           '-c', 'copy',
           output_file]
    # ffmpeg进度信息输出到标准错误流而不是标准输出流，这里将其错误流重定向到child管道中
    # 重点是一定要设置bufsize=0,禁用缓冲区，否则信息不能及时输出
    # universal_newlines=True将管道输出设为文本模式
    child = sp.Popen(cmd, stderr=sp.PIPE, bufsize=0, universal_newlines=True, encoding='utf-8')

    # child.poll()判断子进程是否结束
    while child.poll() is None:
        line = child.stderr.readline().strip()
        if line:
            # 在此可以获取到ffmpeg每一次的信息输出
            print(line)

    # ffmpeg进程结束，关闭流
    child.stderr.close()



