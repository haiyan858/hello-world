test_login.py
import hashlib
from PIL import Image, ImageFont, ImageDraw, ImageFilter
import random


def image():
    str1 = ''
    total = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ012345789'
    # 图片大小130 x 50
    width = 130
    height = 50
    # 先生成一个新图片对象
    im = Image.new('RGB', (width, height), 'white')
    # 设置字体
    font = ImageFont.truetype('FreeSans', 40)
    # 创建draw对象
    draw = ImageDraw.Draw(im)

    # 输出每一个文字
    for item in range(5):
        temp = random.choice(total)
        draw.text((5 + random.randint(4, 7) + 20 * item, 5 + random.randint(3, 7)), text=temp,
                  fill='black', font=font)
        str1 += temp

    # 划几根干扰线
    for num in range(8):
        x1 = random.randint(0, width / 2)
        y1 = random.randint(0, height / 2)
        x2 = random.randint(0, width)
        y2 = random.randint(height / 2, height)
        draw.line(((x1, y1), (x2, y2)), fill='black', width=1)

    # 模糊下,加个帅帅的滤镜～
    im = im.filter(ImageFilter.FIND_EDGES)
    im.show()

    return str1


def store(user, secret, db):
    md5 = hashlib.md5()
    md5.update(secret.encode('utf-8'))
    result = md5.hexdigest()
    db[user] = result


def verify(db):
    while True:
        result1 = image()
        username = input('输入你的用户名\n')
        secret = input('输入你的密码:\n')
        code = input('输入你的验证码:\n')
        md5 = hashlib.md5()
        md5.update(secret.encode('utf-8'))
        result = md5.hexdigest()
        if username not in db:
            print('用户名不存在')
        elif result1 != code:
            print('验证码输入错误')
        elif db[username] == result:
            print('验证通过，欢迎光临')
            break
        else:
            print('密码不正确,请重新输入')


def register(db):
    while True:
        username = input('输入你的用户名\n')
        if username in db.keys():
            print('用户名已存在，请重新输入')
            continue
        result = image()
        secret = input('输入你的密码:\n')
        code = input('输入你的验证码:\n')
        dicta = {'number': 0, 'lower': 0, 'upper': 0, 'other': 0}
        for item in secret:
            if item.isdigit():
                dicta['number'] += 1
            elif item.islower():
                dicta['lower'] += 1
            elif item.isupper():
                dicta['upper'] += 1
            else:
                dicta['other'] += 1
        if dicta['lower'] < 1 or dicta['upper'] < 1 or dicta['number'] < 1 or dicta['other'] < 1:
            print('密码必须有大、小写字母，数字，和特殊字符四部分组成,请重新输入')
        elif code != result:
            print('验证码输入错误')
        else:
            print('验证通过，欢迎光临')
            break
    return username, secret


if __name__ == '__main__':
    database = {'肖鑫': '67ae79674e56657bb652bd02f7251474'}
    receive = input('欢迎光临，输入您的身份,新用户（1），老客户（2）\n')
    if receive == '1':
        user, password = register(database)
        store(user, password, database)
        print(database)
    elif receive == '2':
        verify(database)