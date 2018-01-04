# coding=utf-8

# print输出内容到本地文件
import log_utils

log_path = './test_output.txt'
write_type = 'w'
output = '1a3'
log_utils.log_to_file(log_path, write_type, output)
