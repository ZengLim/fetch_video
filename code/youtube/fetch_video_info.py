import yt_dlp

# 输入视频URL
video_url = input("请输入视频URL: ")

# 配置下载选项
ydl_opts = {
    'writeinfojson': True,  # 写入信息JSON文件（包含manifest）
    'outtmpl': '%(title)s.%(ext)s',  # 输出文件名格式（保存为JSON）
}

try:
    # 创建下载器
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # 下载视频信息（不会下载视频内容）
        ydl.download([video_url])
    print("manifest 文件下载完成!")

except Exception as e:
    print(f"发生错误: {e}")
    