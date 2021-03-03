# mp.Value()是共享内存
# mp.Manager().Value()是共享数据（不通过共享内存的方式）
# 前者速度更快，后者更灵活（支持的类型更多）
import multiprocessing as mp

def job(v, n):
    v.value += 1
    n += 1

if __name__ == '__main__':
    array = mp.Array('i', [1, 2, 3])
    value = mp.Value('d', 1)
    # cdtype https://www.docs4dev.com/docs/zh/python/3.7.2rc1/all/library-array.html#module-array
    num = 10
    print(array[:])

    print('before p, value=', value.value, ', num=', num)

    p1 = mp.Process(target=job, args=(value, num))
    p1.start()
    p1.join()
    print('after p1, value=', value.value, ', num=', num)

    p2 = mp.Process(target=job, args=(value, num))
    p2.start()
    p2.join()
    print('after p2, value=', value.value, ', num=', num)