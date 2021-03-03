
# 决策树保存
f = open('.\\iris_tree.dot', 'w')
#下句是管道模式下的写法，注释起来的不这么写
tree.export_graphviz(model.get_params('DTC')['DTC'], out_file=f)    # 这里的DTC只是一个代号，代指局册数模型
#           可视化
f.close()

# np保存
np.save('../data/data.npy', data)

datain = np.load('../data/d_inpro.npy', allow_pickle=True) # 没有后面这个属性好像不能还原原格式

wlist = wlist.reshape([1, -1])[0]   # 二维变成一维，-1


np.savetxt(pathin, datain, delimiter=',', header='x,y,z,I', fmt='%.2f')
np.savetxt(pathout, dataout, delimiter=',', header='x,y,z,P,I', fmt='%.2f')

