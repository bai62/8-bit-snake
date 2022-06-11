# 游戏窗体的宽(像素数)，高，格子行数，格子大小
wd_W, wd_H, gd_size = 1000, 750, 25
# 游戏窗体的宽，高
wd_size = (wd_W, wd_H)
# 背景颜色，蛇身颜色，蛇头颜色，线条颜色
bg_color, snake_color, line_color, food_color ,font_color= (170, 204, 102), (43, 51, 26), (43, 51, 26), (43, 51, 26), (43, 51, 26)

# 游戏界面的宽，高
gm_W, gm_H = 750, 500
# 游戏界面四个坐标量
gm_x1, gm_y1 = (wd_W - gm_W) / 2, (wd_H - gm_H) / 2
gm_x2, gm_y2 = gm_x1 + gm_W, gm_y1 + gm_H
# 游戏的行数的列数
gm_r, gm_c = gm_H / gd_size, gm_W / gd_size


class Point:
    x, y = 0, 0

    # 构造函数
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self,other):
            return self.__dict__ == other.__dict__

    # 返回一个当前对象的值拷贝
    def copy(self):
        return Point(self.x, self.y)
