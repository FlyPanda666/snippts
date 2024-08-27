def get_next(pattern: str):
    # 初始化
    n = len(pattern)
    nxt = [0] * n
    # j表示前缀的末尾
    j = 0
    for i in range(1, n):
        # i表示后缀的末尾.
        # 先处理不等的情况.
        while j > 0 and pattern[i] != pattern[j]:
            j = nxt[j - 1]
        # 再处理相等的情况.
        if pattern[i] == pattern[j]:
            j += 1
        # 更新next数组.
        nxt[i] = j
    return nxt


if __name__ == "__main__":
    s = "aabaaf"
    print(get_next(s))
