# 获取抖音直播的真实流媒体地址，默认最高画质。
# 如果知道该直播间如“6779127643792280332”形式的room_id，则直接传入room_id。
# 如果不知道room_id，可以使用手机上打开直播间后，选择“分享--复制链接”，传入如“https://v.douyin.com/qyRqMp/”形式的分享链接。
#
import requests
import re

class DouYin:

    def __init__(self, rid):
        self.rid = rid

    def get_real_url(self):
        try:
            print(self.rid)
            if 'v.douyin.com' in self.rid:
                room_id = re.findall(r'(\d{19})', requests.get(url=self.rid).url)[0]
                print(room_id)
            else:
                room_id = self.rid
            room_url = 'https://webcast.amemv.com/webcast/reflow/{}'.format(room_id)
            response = requests.get(url=room_url).text
            rtmp_pull_url = re.search(r'"rtmp_pull_url":"(.*?flv)"', response).group(1)
            hls_pull_url = re.search(r'"hls_pull_url":"(.*?m3u8)"', response).group(1)
            print(rtmp_pull_url)
            print(hls_pull_url)
            real_url = [rtmp_pull_url, hls_pull_url]
        except:
            raise Exception('直播间不存在或未开播或参数错误')
        return real_url



