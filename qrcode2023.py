from qrcode import make as make_qrcode


def create_qrcode(link: str):
    __myqr = make_qrcode(link)
    __myqr.save('qr_code.png')


if __name__ == '__main__':
    link = 'https://linktr.ee/diotelecom'
    create_qrcode(link)