from matplotlib import pylab as pl
from numpy.random import randn
from scipy import array, ceil, dot, float64, floor, matrix, sqrt, zeros
from scipy.linalg import cholesky, eig, norm, solve

# =================
#  主成分分析 (PCA)
# =================
"""
Maximum Variance criterion
"""
def pca(data, base_num = 1):
    N, dim = data.shape
    
    data_m = data.mean(0)
    data_new = data - data_m

    ### データ数 > 次元数
    if N > dim:
        ### データ行列の共分散行列
        cov_mat = dot(data_new.T, data_new) / float(N)
        ### 固有値・固有ベクトルを計算
        l, vm = eig(cov_mat)
        ### 固有値が大きい順に並び替え
        axis = vm[:, l.argsort()[- min(base_num, dim) :][:: -1]].T

    ### 次元数 > データ数
    else:
        base_num = min(base_num, N)
        cov_mat = dot(data_new, data_new.T) / float(N)
        l, v = eig(cov_mat)
        ### 固有値と固有ベクトルを並び替え
        idx = l.argsort()[::-1]
        l = l[idx]
        v = vm[:, idx]
        ### 固有ベクトルを変換
        vm = dot(data_m.T, v[:, : base_num])
        ### （主成分の）基底を計算
        axis = zeros([base_num, dim], dtype = float64)
        for ii in range(base_num):
            if l[ii] <= 0:
                break
            axis[ii] = vm[:, ii] / norm(vm[:, ii])

    return axis

# ========
#  テスト
# ========
from numpy.random import multivariate_normal
def test():
    data = multivariate_normal([0, 0], [[1, 2], [2, 5]], 100)
    ### PCA
    pc_base = pca(data, base_num = 1)[0]
 
    ### Plotting
    fig = pl.figure()
    fig.add_subplot(1,1,1)
    pl.axvline(x=0, color = "#000000")
    pl.axhline(y=0, color = "#000000")
    ### Plot data
    pl.scatter(data[:, 0], data[:, 1])
    ### Draw the 1st principal axis
    pc_line = array([-3., 3.]) * (pc_base[1] / pc_base[0])
    pl.arrow(0, 0, -pc_base[0] * 2, -pc_base[1] * 2, fc = "r", width = 0.15, head_width = 0.45)
    pl.plot([-3, 3], pc_line, "r")
    ### Settings
    pl.xticks(size = 15)
    pl.yticks(size = 15)
    pl.xlim([-3, 3])
    pl.tight_layout()
    pl.show()


if __name__ == "__main__":
    test()
