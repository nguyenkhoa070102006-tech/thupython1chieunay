
import random
def sinh_mang_tang_dan(n):
    mang = []
    so_dau_tien = random.randint(-100,100)
    mang.append(so_dau_tien)

    for i in range(1,n):
        tang = random.randint(0,10)
        so = mang[i-1]+tang
        mang.append(so)

    return mang
def tim_nhi_phan(mang,x):
    trai = 0
    phai = len(mang)-1

    while trai <= phai:
        giua = (trai+phai)//2
        if mang[giua]==x:
            return giua
        if x < mang[giua]:
            phai = giua - 1
        else:
            trai = giua + 1
    return -1
def main():
    n = int(input('Nhap so luong kich thuoc cua mang:'))
    mang = sinh_mang_tang_dan(n)
    print(mang)
    x = int(input('Nhap vao vi tri can tim:'))
    vi_tri = tim_nhi_phan(mang,x)
    if vi_tri != -1:
        print(f'tim thay gia tri {x} tai vi tri {vi_tri} trong mang')
    else:
        print(f'ko tim thay gia tri {x}')
if __name__ == "__main__":
    main()