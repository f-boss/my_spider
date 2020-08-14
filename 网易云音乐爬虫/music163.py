"""
Author: Bo_ss | Facker
Time: 2020/8/12
About: Crawl the music in https://music.163.com/
该项目仅供学习，侵权必删！！！
"""
import binascii
import os
import base64

try:
    import requests
    from Crypto.Cipher import AES
    from Crypto.Util.Padding import pad
except Exception as e:
    print(e)
    print('\nYou can try using:\n'
          '\'python3 -m pip install ***\'\n'
          'to resolve this exception\n')
    exit(-1)


class Encrypt:
    def __init__(self, ids=None, keyword=None, search_id=True):
        ids = str(ids)
        self.iv = '0102030405060708'
        self.pub_key = '010001'
        if search_id:
            self.text = '{"ids":"[' + ids + ']","level":"standard","encodeType":"aac","csrf_token":""}'
        else:
            self.text = '{"hlpretag":"<span class=\\"s-fc7\\">","hlposttag":"</span>","s":"'\
                        + keyword + '","type":"1","offset":"'\
                        + str(0) + '","total":"true","limit":"30","csrf_token":""}'
        self.modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876' \
                       'aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d0' \
                       '5c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e2' \
                       '89dc6935b3ece0462db0a22b8e7'
        self.nonce = '0CoJUm6Qyw8W8jud'

    def aes_encrypt(self, msg, key):
        encrypts = AES.new(str.encode(key), mode=AES.MODE_CBC, IV=str.encode(self.iv))
        result = encrypts.encrypt(pad(msg.encode(), AES.block_size))  # 这是一个加密的关键点
        result_str = base64.b64encode(result).decode('utf-8')
        return result_str

    @staticmethod
    def rsa_encrypt(text, pubkey, modulus):
        text = text[::-1]
        rsa = pow(int(binascii.hexlify(text), 16), int(pubkey, 16), int(modulus, 16))
        return format(rsa, 'x').zfill(256)

    def encrypt(self):
        i = binascii.hexlify(os.urandom(14))[:16]
        enc_text = self.aes_encrypt(self.text, self.nonce)
        enc_text = self.aes_encrypt(enc_text, i.decode('utf-8'))
        enc_sec_key = self.rsa_encrypt(i, self.pub_key, self.modulus)
        data = {
            'params': enc_text,
            'encSecKey': enc_sec_key,
        }
        return data


class MusicCrawl:
    def __init__(self, keyword=None, ids=None):
        self.session = requests.Session()
        self.base_url = 'https://music.163.com/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/55.0.2883.87 Safari/537.36',
            'Referer': 'http://music.163.com/',
        }
        self.keyword = keyword
        self.ids = str(ids)

    def search_data(self):
        encrypt = Encrypt(search_id=False, keyword=self.keyword)
        search_data = encrypt.encrypt()
        return search_data

    def ids_data(self):
        encrypt = Encrypt(ids=self.ids)
        ids_data = encrypt.encrypt()
        return ids_data

    def get_list(self):
        data = self.search_data()
        search_url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
        r = self.session.post(search_url, data=data, headers=self.headers)
        song_list = r.json()
        i = 0
        for song in song_list['result']['songs']:
            i += 1
            yield {
                'num': i,
                'name': song['name'],
                'singer': song['ar'][0]['name'],
                'ids': song['id'],
            }

    def get_song(self, name):
        data = self.ids_data()
        song_url = 'https://music.163.com/weapi/song/enhance/player/url/v1?csrf_token='
        r = self.session.post(song_url, data=data, headers=self.headers)
        song = r.json()
        if song['code'] == 200:
            self.downing_song(song['data'][0]['url'], name)
        else:
            print('Download error')

    def downing_song(self, url, name):
        r = self.session.get(url, headers=self.headers)
        if r.status_code == 200:
            file_path = '{0}/{1}.{2}'.format('music', name, 'mp3')
            if not os.path.exists('music'):
                os.mkdir('music')
            with open(file_path, 'wb') as f:
                f.write(r.content)
            print('Download successfully')
        else:
            print('Download error. You might want to check the problem')


class Run:
    """
    Author: Bo_ss | Facker
    Email: 2362315840@qq.com
    h                              | help
            You can use the 'help' command to get help
    d [-id ids name] [-list]            | down [-id ids] [-list]
            You can use the 'd' command to download songs
            (e.g. d -id 12345454 song_name)
            (e.g. d -list)
    s [keyword]                    | search [keyword]
            You can search for songs using the 's' command
            (e.g. s QQ飞车主题曲)
            (e.g. s Everything's Alright)
    l [-save num] [-view] [-remove num]  | list [-save num] [-view] [-remove num]
            You can use the 'l' command to save the songs you want to download
            (e.g. l -save 1 --> It saves the first song you get in a search)
            (e.g. l -view)
            (e.g. l -remove 2)
    q                              | quit
            You can exit the program using 'q'
    """

    def __init__(self):
        self.all_lists = []
        self.search_lists = []

    @staticmethod
    def shell_error():
        print('You may have typed this command incorrectly')
        print('You can use the \'help\' or \'h\' command to get help')

    def quit(self, command):
        if not len(command.split()) == 1:
            self.shell_error()
        else:
            if self.all_lists:
                print("I found some undownloaded data in your list.")
                save = input("Would you want to download it (y/n)?")
                if save == 'Y' or save == 'y':
                    pass
                if save == 'N' or save == 'n':
                    exit(0)

    def down(self, command):
        length = len(command.split())
        if length == 2 and command.split()[1] == '-list':
            for all_list in self.all_lists:
                down_music = MusicCrawl(ids=all_list['ids'])
                down_music.get_song(name=all_list['name'])
        elif length == 4 and command.split()[1] == '-id':
            down_music = MusicCrawl(ids=command.split()[2])
            down_music.get_song(command.split()[3])
        else:
            self.shell_error()

    def search(self, command):
        length = len(command.split())
        self.search_lists = []
        if length == 2:
            music_lists = MusicCrawl(keyword=command.split()[1])
            tag = 'num   |   name   |   singer   |   ids'
            tag1 = '{}   |   {}   |   {}   |   {}'
            print(tag)
            for music_list in music_lists.get_list():
                self.search_lists.append(music_list)
                print(tag1.format(music_list['num'], music_list['name'], music_list['singer'], music_list['ids']))
        else:
            self.shell_error()

    def list(self, command):
        length = len(command.split())
        if length == 2 and command.split()[1] == '-view':
            if self.all_lists:
                for i, all_list in enumerate(self.all_lists):
                    all_list['num'] = str(i)
                tag = 'num   |   name   |   singer   |   ids'
                tag1 = '{}   |   {}   |   {}   |   {}'
                print(tag)
                for music_list in self.all_lists:
                    print(tag1.format(music_list['num'], music_list['name'], music_list['singer'], music_list['ids']))
            else:
                print('There\'s nothing in there')
        elif length == 3:
            if command.split()[1] == '-save':
                if not self.search_lists[int(command.split()[2])-1] in self.all_lists:
                    self.all_lists.append(self.search_lists[int(command.split()[2])-1])
                    print('Save successfully')
                else:
                    print('It\'s already in there!!!')
            elif command.split()[1] == '-remove':
                if self.all_lists:
                    if str(len(self.all_lists)) == command.split()[2]:
                        a = int(int(command.split()[2])-1)
                        del self.all_lists[a]
                        print('Remove successfully')
                    else:
                        a = str(int(command.split()[2]) - 1)
                        print('There are only '+a+' of them')
                else:
                    print('Remove the failure.\nThere\'s nothing in there')
            else:
                self.shell_error()
        else:
            self.shell_error()

    def execute(self, command):
        if command.split()[0] == 'h' or command.split()[0] == 'help':
            print(self.__doc__)
        elif command.split()[0] == 'd' or command.split()[0] == 'down':
            self.down(command)
        elif command.split()[0] == 's' or command.split()[0] == 'search':
            self.search(command)
        elif command.split()[0] == 'l' or command.split()[0] == 'list':
            self.list(command)
        elif command.split()[0] == 'q' or command.split()[0] == 'quit':
            self.quit(command)

    def working(self):
        command = input("Facker> ")
        com = command.split()
        try:
            if com[0] in ['h', 'help', 'd', 'down', 's', 'search', 'l', 'list', 'q', 'quit']:
                self.execute(command)
            else:
                print('*** Usage error: command "' + com[0] + '" is not find')
        except IndexError:
            pass


if __name__ == '__main__':
    print("===============")
    print("Music163Crawler")
    print("===============\n")
    print('Author: Bo_ss | Facker')
    print('Email: 2362315840@qq.com\n')
    print('You can use the \'help\' or \'h\' command to get help\n')
    run = Run()
    while True:
        run.working()
# successfully!!!!
