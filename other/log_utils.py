#! -*- encoding: utf-8 -*-
import time


def log_to_file(file_path='./log_file.txt', write_type='w', output=''):
    f = open(file_path, write_type)
    print >> f, output + ' , time: ' + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
