from importlib import reload
from NoraGeneral import noraAbout

reload(noraAbout)


def get_title():
    return 'About'


def get_ui():
    about = noraAbout.NoraAbout()
    method_info = 'Smooth Skinning Decomposition with Rigid Bones(SSDR)\n' \
                  'SSDR 是一个通过数值最优化方法将复杂的顶点形变转换成线性蒙皮权重和骨骼变换的方法，' \
                  '起初用聚类和点云匹配来初始化一个大体的骨骼变换和权重，之后用块坐标下降方法迭代优化骨骼变换和蒙皮权重。\n'\
                  '具体细节可在下面的链接中了解：'
    about.set_text(method_info)
    about.set_link_text('Smooth Skinning Decomposition with Rigid Bones')
    about.set_link(r'http://graphics.cs.uh.edu/ble/papers/2012sa-ssdr/index.html')
    return about


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False