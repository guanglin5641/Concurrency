import aaa.common.mysql
import aaa.connector.positive_submission


def interface_comment_run():
    image = ['https://img.dac6.cn/file/image/mobile/1699612698c50de962d06f6d9f2aca5029e45e253e.png',
    'https://img.dac6.cn/file/image/mobile/1699612698c50de962d06f6d9f2aca5029e45e253e.png',
    'https://img.dac6.cn/file/image/mobile/1699613326c50de962d06f6d9f2aca5029e45e253e.png',
    'https://img.dac6.cn/file/image/mobile/169961356915fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961368315fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961382415fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961781615fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961801015fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961822615fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961801015fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/169961887415fd17443f917a39719ca71deef630fd.png',
    'https://img.dac6.cn/file/image/mobile/16996190759ddd3d3018d21f75e556781a882a0df8.png',
    'https://img.dac6.cn/file/image/mobile/16996196403aa81cc484f91f29089338e6e31f8bb9.png',
    'https://img.dac6.cn/file/image/mobile/16996198283aa81cc484f91f29089338e6e31f8bb9.png'

    ]
    i = len(image)
    print(i)
    for i in range(i):
        db = common.mysql.DB()
        updata_sql= '''UPDATE bwc_dev.bwc_comment_cashback_record
        SET client_user_id=1
        WHERE client_user_id=101824698'''
        db.update(updata_sql)
        print(connector.comment_cashback.get_submit(image[i]))
    return ()



if __name__ == '__main__':
    pass
