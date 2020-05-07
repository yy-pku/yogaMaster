import numpy as np


class PoseSequence:
    def __init__(self, sequence):
        self.poses = []
        self.poses.append(Pose(sequence))

        for pose in self.poses:
            for attr, part in pose:
                setattr(pose, attr, part)


class Pose:
    PART_NAMES = ['nose', 'neck', 'right_shoulder', 'right_elbow', 'right_wrist', 'left_shoulder', 'left_elbow', 'left_wrist', 'right_hip',
                  'right_knee', 'right_ankle', 'left_hip', 'left_knee', 'left_ankle','right_ear','right_eye','left_ear','left_eye']

    def __init__(self, parts):
        """Construct a pose for one image, given an array of parts

        Arguments:
            parts - 18* 3 ndarray of x, y, confidence values
        """
        # for name, vals in zip(self.PART_NAMES, parts):
        #     # 设置对象
        #     setattr(self, name, Part(vals))

        for part_name in self.PART_NAMES:
            setattr(self,part_name,Part(parts[part_name]))

        #add mid_hip
        mid_hip_dict={}
        mid_hip_dict['x']=(getattr(self, 'left_hip').x+getattr(self, 'right_hip').x)/2
        mid_hip_dict['y'] = (getattr(self, 'left_hip').y + getattr(self, 'right_hip').y) / 2
        mid_hip_dict['score'] = max(getattr(self, 'left_hip').c,getattr(self, 'right_hip').c)
        setattr(self,'mid_hip',Part(mid_hip_dict))

    def __iter__(self):
        for attr, value in self.__dict__.items():
            yield attr, value

    def __str__(self):
        out = ""
        for name in self.PART_NAMES:
            _ = "{}: {},{}".format(name, getattr(self, name).x, getattr(self, name).x)
            out = out + _ + "\n"
        return out

    def print(self, parts):
        out = ""
        for name in self.PART_NAMES:
            _ = "{}: {},{}".format(name, getattr(self, name).x, getattr(self, name).y)
            out = out + _ + "\n"
        return out


class Part:
    def __init__(self, vals):
        # 点的坐标
        print(vals)
        self.x = vals['x']
        self.y = vals['y']
        # 置信度
        self.c = vals['score']
        self.exists = self.c != 0.0

    def __floordiv__(self, scalar):
        # 定义/和//两种出发的运算
        self.__truediv__(self, scalar)

    def __truediv__(self, scalar):
        return Part([self.x / scalar, self.y / scalar, self.c])

    @staticmethod
    def dist(part1, part2):
        return np.sqrt(np.square(part1.x - part2.x) + np.square(part1.y - part2.y))