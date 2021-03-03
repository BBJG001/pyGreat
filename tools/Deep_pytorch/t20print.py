import torch

torch.random.manual_seed(0)

tensor = torch.rand(100, 9)-0.5
print(tensor)

torch.set_printoptions(
    precision=2,    # 精度，保留小数点后几位，默认4
    threshold=1000,
    # 最多可现实的Array元素个数，默认1000；
    # 限制的是基本元素个数，如3*5的矩阵，限制的是15而非3（行）
    # 如果超过就采用缩略显示
    edgeitems=3,
    # 在缩率显示时在起始和默认显示的元素个数
    linewidth=150,  # 每行最多显示的字符数，默认80，超过则换行显示
    profile=None,
    # 3中预定义的显示模板，可选'default'、'short'、'full'
    # if profile == "default":
    #     PRINT_OPTS.precision = 4
    #     PRINT_OPTS.threshold = 1000
    #     PRINT_OPTS.edgeitems = 3
    #     PRINT_OPTS.linewidth = 80
    # elif profile == "short":
    #     PRINT_OPTS.precision = 2
    #     PRINT_OPTS.threshold = 1000
    #     PRINT_OPTS.edgeitems = 2
    #     PRINT_OPTS.linewidth = 80
    # elif profile == "full":
    #     PRINT_OPTS.precision = 4
    #     PRINT_OPTS.threshold = inf
    #     PRINT_OPTS.edgeitems = 3
    #     PRINT_OPTS.linewidth = 80
    sci_mode=False  # 用科学技术法显示数据，默认True
)
print(tensor)