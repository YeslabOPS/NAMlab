import time

# 时间字符串到时间戳
def string_to_timestamp(time_string):
    # 定义时间格式
    time_format = "%b %d, %Y %I:%M %p"
    # 将时间字符串解析为时间元组
    time_tuple = time.strptime(time_string, time_format)
    # 将时间元组转换为时间戳（秒级别）
    timestamp = int(time.mktime(time_tuple) * 1000)  # 转换为毫秒
    return timestamp

# 时间戳到时间字符串
def timestamp_to_string(timestamp):
    # 将时间戳（毫秒）转换为秒
    timestamp_sec = timestamp / 1000
    # 将时间戳转换为本地时间元组
    time_tuple = time.localtime(timestamp_sec)
    # 定义时间格式
    time_format = "%b %d, %Y %I:%M %p"
    # 将时间元组转换为时间字符串
    time_string = time.strftime(time_format, time_tuple)
    return time_string

# 示例
time_string = "Dec 15, 2023 10:04 AM"
print(string_to_timestamp(time_string))
timestamp = 1702605890601
print(timestamp_to_string(timestamp))
