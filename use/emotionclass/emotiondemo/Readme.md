## data_helper.py
文本预处理文件
- getdata(begin, end, datapath)

  数据太多了，用这个函数提取一部分来训练和测试

  从原始数据中提取部分用来训练和测试，参数为结束和开始的下标

- clean_str(string)

  去除标点符号

- load_data_preprocess(path)

  数据预处理（每个句子拆解成一个词列表）

- pad_sentences(sentences, padding_word="<PAD/>", sequence_length=SEQUENCE_LENGTH)

  填充句子，使所有句子长度等于sequence_length

  确定一个padding size，固定句子向量的宽度，可以简单的调用keras.sequence来做
  
- do_data_helper()

  整合上面的操作，合在一个方法中
  
  返回词列表向量话后的矩阵
  
## classification.py

. . .