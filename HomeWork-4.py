def func_1():
    data = [
        [13, 25, 23, 34],
        [45, 32, 44, 47],
        [12, 33, 23, 95],
        [13, 53, 34, 35]
    ]
    k = 0
    sum = 0
    for i in data:
        sum += i[k]
        k += 1
    print(sum)

def func_2(fibo, n):
    if len(fibo) < n:
        fibo.append(fibo[-1] + fibo[-2])
        func_2(fibo, n)
    else:
        print(fibo)

def func_3(l):
    while len(l) >= 2:
        d = {l[-2]: l[-1]}
        del l[-2:]
        l.append(d)
    print(l[0])


if __name__ == "__main__":
    func_1()
    #func_2([0, 1], 10)
    #func_3(['2018-01-01', 'yandex', 'cpc', 100])