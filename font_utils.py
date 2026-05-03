import os
import matplotlib
if not hasattr(matplotlib, '_called_use'):
    matplotlib.use('Agg')
    matplotlib._called_use = True
import matplotlib as mpl
import matplotlib.font_manager as fm


def configure_matplotlib_font():
    root = os.path.dirname(__file__)
    font_path = os.path.join(root, "font", "NanumGothic-Regular.ttf")
    if not os.path.isfile(font_path):
        raise FileNotFoundError(f"Font 파일을 찾을 수 없습니다: {font_path}")

    fm.fontManager.addfont(font_path)
    font_prop = fm.FontProperties(fname=font_path)
    mpl.rcParams["font.family"] = font_prop.get_name()
    mpl.rcParams["axes.unicode_minus"] = False
