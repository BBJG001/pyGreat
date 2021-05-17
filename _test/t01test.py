import requests
from bs4 import BeautifulSoup as BS
import os
import time
from PIL import Image
from io import BytesIO

HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
    'cookie': '__cfduid=dda041b867768d495cd0dd401915744ad1616178358',
}

def fun():
    url = 'https://18h.animezilla.com/manga/3934/{}'
    p_dir = './data/{}'.format(url.split('/')[-2])
    os.makedirs(p_dir, exist_ok=True)
    i = 1
    while i<213:
        ui = url.format(i+1)
        HEADERS['referer'] = 'https://18h.animezilla.com/manga/3934/{}'.format(i)
        try:
            resp = requests.get(ui, headers=HEADERS)

            soup = BS(resp.text, 'html.parser')
            img = soup.find('img', id='comic')
            u_img = img.get('src')
            print(i+1, u_img)
            resp_img = requests.get(u_img, headers=HEADERS)
            # img = Image.open(BytesIO(resp_img.content))
            # img.show()
            sp = os.path.join(p_dir, '{}.jpg'.format(str(i+1).zfill(3)))

            with open(sp, 'wb') as f:
                f.write(resp_img.content)
        except:
            time.sleep(2)
            continue
        i+=1

if __name__ == '__main__':
    fun()