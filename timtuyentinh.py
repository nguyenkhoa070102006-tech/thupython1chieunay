# import random

# def san_sinh_mang(n):
#     mang = []
#     for i in range(n):
#         so_ngau_nhien = random.randint(-100, 100)
#         mang.append(so_ngau_nhien)
#     return mang

# def tim_tuyen_tinh(mang, x):
#     n = len(mang)
#     for i in range(n):
#         if mang[i] == x:
#             return i
#     return -1

# def main():
#     so_luong = int(input('Nhap so gia tri cua mang: '))
#     mang = san_sinh_mang(so_luong)
#     print(mang)
#     x = int(input('Nhap vao gia tri can tim: '))
#     vi_tri = tim_tuyen_tinh(mang, x)
#     if vi_tri != -1:
#         print(f'Tim thay gia tri {x} tai vi tri {vi_tri}')
#     else:
#         print(f'Khong tim thay gia tri {x} trong mang')

# if __name__ == '__main__':
#     main()
import random

def sinh_so_ngau_nhien(n):
    mang = []
    for i in range(0,n):
        so_ngau_nhien = random.randint(-100,100)
        mang.append(so_ngau_nhien)
    return mang

def tim_tuyen_tinh(mang,x):
    n = len(mang)
    for i in range(0,n):
        if mang[i]==x:
            return i
    return -1
def main():
    so_luong = int(input('Nhap kich thuoc mang:'))
    mang = sinh_so_ngau_nhien(so_luong)
    print(mang)
    x = int(input('Nhap vi tri can tim:'))
    vi_tri = tim_tuyen_tinh(mang,x)
    if vi_tri != -1:
        print(f'tim thay gia tri{x} tai vi tri{vi_tri}')
    else:
        print(f'ko tim thay gia tri{x}')
if __name__ == '__main__':
    main()