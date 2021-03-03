from graphviz import Digraph

gz=Digraph("会议报名购票流程图",'comment',None,None,'png',None,"UTF-8",
           {'rankdir':'TB'},
           {'color':'black','fontcolor':'black','fontname':'FangSong','fontsize':'12','style':'rounded','shape':'box'},
           {'color':'#999999','fontcolor':'#888888','fontsize':'10','fontname':'FangSong'},None,False)

gz.node('0','会议')
gz.node('1','直播会议')
gz.node('2','直播页面')
gz.node('a','现场会议')
gz.node('b','报名')
gz.node('i','报名')
gz.node('c','选择门票')
gz.node('d','填写需求单')
gz.node('j','填写需求单')
gz.node('e','报名成功',{'color':'red','fontcolor':'red'})
gz.node('f','订单页面')
gz.node('g','报名购票成功',{'color':'red','fontcolor':'red'})

t=set(['01','0a','12'])
a=set(['ab','bd','de'])
b=set(['ab','be'])
c=set(['ac','ci','ij','jf','fg'])
d=set(['ac','ci','if','fg'])
gz.edges(a|b|c|d|t)
gz.edge('c','f','已报名')
print(gz.source)
gz.view()
