from importlib import reload
from NoraGeneral import noraAbout

reload(noraAbout)


def get_title():
    return 'About'


def get_ui():
    about = noraAbout.NoraAbout()
    method_info = 'Fast and Deep Deformation Approximations（FDDA）\n' \
                  'FDDA 是一个通过前馈神经网络逼近LBS与标记误差的方法，他将顶点变形划分为了线性和非线性两个部分。' \
                  '线性部分由LBS完成，但每个顶点仅绑到对它变形影响最大的一个骨骼上，这个骨骼通过最小化LBS与标记误差确定；' \
                  '非线性部分由一个前馈神经网络完成，神经网络的输入为骨架中对变形有影响的骨骼的变换，输出为顶点的局部位移。\n' \
                  'FDDA由上述两个部分组合而成，具体细节可在下面的链接中了解：'
    about.set_text(method_info)
    about.set_link(r'http://graphics.berkeley.edu/papers/Bailey-FDD-2018-08/')
    return about


def get_width():
    return 460


def get_height():
    return 300


def get_use_custom_front_style():
    return False

