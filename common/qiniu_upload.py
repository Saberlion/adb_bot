# -*- coding: utf-8 -*-
from qiniu import Auth, put_file


def upload_to_qiniu(access_key, secret_key, bucket_name, localfile, key):
    # 构建鉴权对象
    q = Auth(access_key, secret_key)
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    return put_file(token, key, localfile)
