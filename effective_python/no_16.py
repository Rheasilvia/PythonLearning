##考虑用生成器来直接返回列表的函数

##原方法
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result


##使用生成器改写
def index_words2(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1


if __name__ == '__main__':
    address = 'Four score and seven years ago...'
    # result = index_words(address)
    result = list(index_words2(address))
    print(result[:3])
