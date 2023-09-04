#解题思路：
# 1. 首部空格直接用 strip 函数删掉
# 2. 符号位 + - 无符号，保存符号位，判断
# 3. 非数字字符，首个非数字，立即返回
# 4. 数字字符：字符转数字：数字的 ASCLL 码减去 0 的 ASCILL 码；数字拼接：从左到右 10 * res + 数字位
class Solution:
    def strToInt(self, str: str) -> int:

        str = str.strip()  # 删除空格

        if not str: return 0  # 字符串为空直接返回
        res, i, sign = 0, 1, 1 # 数字 遍历开始位 符号位

        int_max, int_min, bndry = 2**31 - 1, -2 ** 31, 2 ** 31 //10  #上下限，处以10边界是因为每次都会✖️10

        if str[0] =='-': sign = -1
        elif str[0] != '+': i = 0 # 无符号从【0】开始遍历

        for c in str[i:]:
            if not '0' <= c <= '9' : break # 非数字直接跳出去
            if res > bndry or res == bndry and c >'7': # 越界处理
                return int_max if sign ==1 else int_min
            
            res = 10 * res + ord(c) - ord('0') # 数字拼接

        return sign * res
    
y = Solution()
aa = "5638 ugf"
print(y.strToInt(aa))
    

    # 优化：不用 strip()方法，降低空间复杂度。可以直接用 res // 10 如果和上次计算的结果不一致说明发生了越界
    # 上界 2147483647 // 10 = 214748364（*10 + x）
    # 情况一：执行拼接10×res≥2147483650越界
    # 情况二：拼接后是2147483648或2147483649越界

