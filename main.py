import numpy as np
import matplotlib.pyplot as plt

# def multiplication_Matrix(ma_tran1 , ma_tran2 ):
#     res = ma_tran1@ma_tran2
#     if res == ValueError:
#         return  "Dinh dang ma tran khong dung"
#     return ma_tran1@ma_tran2

#lúc đầu là em if else thì nó luôn bào lỗi Value hiển thị ra sai định dạng
 #nên em tìm hiểu cách dùng "try" và "expect"
def multiplication_Matrix(ma_tran1 , ma_tran2):
    try:
        res = ma_tran1@ma_tran2
        return res
    except ValueError:
        return "Kiểm tra cột của ma trận thứ nhất và hàng của ma trận thứ hai"

def linear_trans(ma_tran, vector):
    try:
        res = ma_tran@vector
        return res
    except ValueError:
        return "kiểm tra số cột của ma trận có bằng số phẩn tử của vector không"


def  transpose_matrix(ma_tran):
    try:
        res = np.transpose(ma_tran)
        return res
    except ValueError:
        return "Không đúng  định dạng"
def det_matrix(matrix):
    try:
        res = np.linalg.det(matrix)
        return res
    except ValueError:
        return "Ma trận cần tính định thức không phải ma trận vuông"




a = np.random.randint(0,10,size=(3,2))
b = np.random.randint(0,10,size=(3,3))
c = np.array([1,2,3])

print("a\n",a)
print("b\n",b)
print("c\n",c)
print("nhan hai ma tran\n", multiplication_Matrix(a,b))
print("bien doi tuyen tinh \n",linear_trans(a,c))
print("ma tran chuyen vi \n",transpose_matrix(a))
print("dinh thuc \n",det_matrix(a))