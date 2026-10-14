import random
# string.ascii_uppercase:大写字母、string.ascii_lowercase:小写字母、string.ascii_letters:大写字母和小写字母、string.digits:数字
import string

class Utils:
    # 生成指定长度的随机字符串
    @staticmethod
    def generate_random_str(length=8):
        return ''.join(random.choices(string.ascii_letters, k=length))
    # 获取字符串的格式
    @staticmethod
    def get_format(s):
        pos = s.rfind(".")        # 从右往左找第一个点
        result = s[pos + 1:]      # 取点后面的部分
        return result