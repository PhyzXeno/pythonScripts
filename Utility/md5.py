
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import hashlib
 
def get_md5_value(src):
    myMd5 = hashlib.md5()
    myMd5.update(src)
    myMd5_Digest = myMd5.hexdigest()
    return myMd5_Digest
 
def get_sha1_value(src):
    mySha1 = hashlib.sha1()
    mySha1.update(src)
    mySha1_Digest = mySha1.hexdigest()
    return mySha1_Digest
 
if __name__== '__main__':
    src = 'aaa'
    src_encode = src.encode('utf-8')
    result_md5_value=get_md5_value(src_encode)
    result_sha1_value=get_sha1_value(src_encode)
    print(src)
    print(result_md5_value)
    print(result_sha1_value)
