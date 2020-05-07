import os
import numpy as np


def evaluate_pose(pose_seq, exercise):
    """Evaluate a pose sequence for a particular exercise.

    Args:
        pose_seq: PoseSequence object.
        exercise: String name of the exercise to evaluate.

    Returns:
        correct: Bool whether exercise was performed correctly.
        feedback: Feedback string.

    """
    print('This is a '+exercise+' POSTURE.')
    if exercise == 'bicep_curl':
        return _bicep_curl(pose_seq)
    elif exercise == 'shoulder_press':
        return _shoulder_press(pose_seq)
    elif exercise == 'front_raise':
        return _front_raise(pose_seq)
    elif exercise == 'shoulder_shrug':
        return _shoulder_shrug(pose_seq)
    elif exercise == 'half_moon3':
        return _half_moon3(pose_seq)
    elif exercise == 'shushi':
        return _shushi(pose_seq)
    elif exercise == 'half_moon1':
        return _half_moon1(pose_seq)
    elif exercise == 'half_moon2':
        return _half_moon2(pose_seq)
    elif exercise == 'camle':
        return _camle(pose_seq)
    if exercise=='warrior1':
        return _warrior1(pose_seq)
    elif exercise=='warrior2':
        return _warrior2(pose_seq)
    elif exercise=='warrior3':
        return _warrior3(pose_seq)
    elif exercise=='mountain':
        return _mountain(pose_seq)
    elif exercise=='seat':
        return _seat(pose_seq)
    elif exercise=='tree_by_wind':
        return _tree_by_wind(pose_seq)
    elif exercise=='low-bow-stance':
        return _low_bow_stance(pose_seq)
    elif exercise=='walking_stick':
        return _walking_stick(pose_seq)
    else:
        return (False, "Exercise string not recognized.")


def _camle(pose_seq):
    # find the arm that is seen most consistently
    poses = pose_seq.poses
    # right_present = [1 for pose in poses
    #                  if pose.right_knee.exists and pose.right_hip.exists and pose.right_ankle.exists]
    # left_present = [1 for pose in poses
    #                 if pose.left_knee.exists and pose.left_hip.exists and pose.left_ankle.exists]
    right_present = [1 for pose in poses
                     if pose.right_shoulder.y > pose.left_shoulder.y]
    left_present = [1 for pose in poses
                    if pose.left_shoulder.y > pose.right_shoulder.y]
    right_count = sum(right_present)
    left_count = sum(left_present)
    # ==为左边，左右算法有待改进
    side = 'right' if right_count > left_count else 'left'
    # print(right_count, left_count)
    # [print(pose.left_shoulder.y, pose.right_shoulder.y) for pose in poses]
    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_knee, pose.right_hip, pose.right_ankle, pose.mid_hip, pose.neck, pose.left_knee, pose.left_hip, pose.left_shoulder, pose.left_elbow) for pose in poses]
    else:
        joints = [(pose.left_knee, pose.left_hip, pose.left_ankle, pose.mid_hip, pose.neck, pose.right_knee, pose.right_hip, pose.right_shoulder, pose.right_elbow) for pose in poses]
    #                        0         1            2            3          4           5          6            7               8

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 四个角度，八个肢体向量
    # 上大腿
    knee_right_hip_vecs = np.array([(joint[5].x - joint[6].x, joint[5].y - joint[6].y) for joint in joints])
    # 中点到侧臀
    right_hip_mid_hip_vecs = np.array([(joint[3].x - joint[6].x, joint[3].y - joint[6].y) for joint in joints])
    # 脖子到中点
    neck_mid_hip_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    left_hip_mid_hip_vecs = np.array([(joint[1].x - joint[3].x, joint[1].y - joint[3].y) for joint in joints])
    # 另一侧中点到侧臀
    # 上直臂两向量
    neck_shoulder_vecs = np.array([(joint[4].x - joint[7].x, joint[4].y - joint[7].y) for joint in joints])
    shoulder_elbow_vecs = np.array([(joint[8].x - joint[7].x, joint[8].y - joint[7].y) for joint in joints])

    # 膝盖到臀部
    hip_knee_vecs = np.array([(joint[1].x - joint[0].x, joint[1].y - joint[0].y) for joint in joints])

    # 下肢
    ankle_knee_vecs = np.array([(joint[2].x - joint[0].x, joint[2].y - joint[0].y) for joint in joints])

    # normalize vectors
    knee_right_hip_vecs = knee_right_hip_vecs / np.expand_dims(np.linalg.norm(knee_right_hip_vecs, axis=1), axis=1)
    right_hip_mid_hip_vecs = right_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(right_hip_mid_hip_vecs, axis=1), axis=1)
    neck_mid_hip_vecs = neck_mid_hip_vecs / np.expand_dims(np.linalg.norm(neck_mid_hip_vecs, axis=1), axis=1)
    left_hip_mid_hip_vecs = left_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(left_hip_mid_hip_vecs, axis=1), axis=1)
    neck_shoulder_vecs = neck_shoulder_vecs / np.expand_dims(np.linalg.norm(neck_shoulder_vecs, axis=1), axis=1)
    shoulder_elbow_vecs = shoulder_elbow_vecs / np.expand_dims(np.linalg.norm(shoulder_elbow_vecs, axis=1), axis=1)
    hip_knee_vecs = hip_knee_vecs / np.expand_dims(np.linalg.norm(hip_knee_vecs, axis=1), axis=1)
    ankle_knee_vecs = ankle_knee_vecs / np.expand_dims(np.linalg.norm(ankle_knee_vecs, axis=1), axis=1)

    mid_hip_hip_knee_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(knee_right_hip_vecs, right_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_mid_hip_hip_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_mid_hip_vecs, left_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_shoulder_elbow_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_shoulder_vecs, shoulder_elbow_vecs), axis=1), -1.0, 1.0)))
    hip_knee_ankle_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(hip_knee_vecs, ankle_knee_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    # 视频所需
    # upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    # upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
    #
    # print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    # print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    # neck_mid_hip_hip_angles 和 hip_knee_ankle_angles 的问题
    # print(mid_hip_hip_knee_angles)
    # print(neck_mid_hip_hip_angles)
    # print(mid_hip_left_hip_knee_angles)
    # print(hip_knee_ankle_angles)
    correct = True
    feedback = ''
    # 右腿没展开
    if mid_hip_hip_knee_angles < 83.0:
        correct = False
        feedback += 'Your legs don''t seem to be moving big enough. Maybe you should try to take a bigger step and keep your legs straight.\n'
    #  腰没下弯
    if neck_mid_hip_hip_angles > 52.0:
        correct = False
        feedback += 'Your waist may not bend down enough, you should bend down as much as possible while maintaining stability.\n'
    # 上直臂角度不对
    if neck_shoulder_elbow_angles < 155.0:
        correct = False
        feedback += 'Your arm may not be straight up. Please adjust the angle of arm extension to make ' + \
                    'it stretch up vertically as much as possible, which is conducive to the coordinated ' + \
                    'development of the body'
    # 左腿不直
    if hip_knee_ankle_angles < 169.0:
        correct = False
        feedback += 'Your legs may not be straight. Maybe you can do as many warm-up exercises or ' \
                    'leg exercises as you can, but be careful not to strain your legs.\n'
    if correct:
        return (
        correct, 'Exercise performed correctly! Weight was lifted fully.')
    else:
        return (correct, feedback)


def _half_moon1(pose_seq):
    # find the arm that is seen most consistently
    poses = pose_seq.poses
    # right_present = [1 for pose in poses
    #                  if pose.right_knee.exists and pose.right_hip.exists and pose.right_ankle.exists]
    # left_present = [1 for pose in poses
    #                 if pose.left_knee.exists and pose.left_hip.exists and pose.left_ankle.exists]
    right_present = [1 for pose in poses
                     if pose.right_shoulder.y > pose.left_shoulder.y]
    left_present = [1 for pose in poses
                    if pose.left_shoulder.y > pose.right_shoulder.y]
    right_count = sum(right_present)
    left_count = sum(left_present)
    # ==为左边，左右算法有待改进
    side = 'right' if right_count > left_count else 'left'
    # print(right_count, left_count)
    # [print(pose.left_shoulder.y, pose.right_shoulder.y) for pose in poses]
    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_knee, pose.right_hip, pose.right_ankle, pose.mid_hip, pose.neck, pose.left_knee, pose.left_hip, pose.left_shoulder, pose.left_elbow) for pose in poses]
    else:
        joints = [(pose.left_knee, pose.left_hip, pose.left_ankle, pose.mid_hip, pose.neck, pose.right_knee, pose.right_hip, pose.right_shoulder, pose.right_elbow) for pose in poses]
    #                        0         1            2            3          4           5          6            7               8

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 四个角度，八个肢体向量
    # 上大腿
    knee_right_hip_vecs = np.array([(joint[5].x - joint[6].x, joint[5].y - joint[6].y) for joint in joints])
    # 中点到侧臀
    right_hip_mid_hip_vecs = np.array([(joint[3].x - joint[6].x, joint[3].y - joint[6].y) for joint in joints])
    # 脖子到中点
    neck_mid_hip_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    left_hip_mid_hip_vecs = np.array([(joint[1].x - joint[3].x, joint[1].y - joint[3].y) for joint in joints])
    # 另一侧中点到侧臀
    # 上直臂两向量
    neck_shoulder_vecs = np.array([(joint[4].x - joint[7].x, joint[4].y - joint[7].y) for joint in joints])
    shoulder_elbow_vecs = np.array([(joint[8].x - joint[7].x, joint[8].y - joint[7].y) for joint in joints])

    # 膝盖到臀部
    hip_knee_vecs = np.array([(joint[1].x - joint[0].x, joint[1].y - joint[0].y) for joint in joints])

    # 下肢
    ankle_knee_vecs = np.array([(joint[2].x - joint[0].x, joint[2].y - joint[0].y) for joint in joints])

    # normalize vectors
    knee_right_hip_vecs = knee_right_hip_vecs / np.expand_dims(np.linalg.norm(knee_right_hip_vecs, axis=1), axis=1)
    right_hip_mid_hip_vecs = right_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(right_hip_mid_hip_vecs, axis=1), axis=1)
    neck_mid_hip_vecs = neck_mid_hip_vecs / np.expand_dims(np.linalg.norm(neck_mid_hip_vecs, axis=1), axis=1)
    left_hip_mid_hip_vecs = left_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(left_hip_mid_hip_vecs, axis=1), axis=1)
    neck_shoulder_vecs = neck_shoulder_vecs / np.expand_dims(np.linalg.norm(neck_shoulder_vecs, axis=1), axis=1)
    shoulder_elbow_vecs = shoulder_elbow_vecs / np.expand_dims(np.linalg.norm(shoulder_elbow_vecs, axis=1), axis=1)
    hip_knee_vecs = hip_knee_vecs / np.expand_dims(np.linalg.norm(hip_knee_vecs, axis=1), axis=1)
    ankle_knee_vecs = ankle_knee_vecs / np.expand_dims(np.linalg.norm(ankle_knee_vecs, axis=1), axis=1)

    mid_hip_hip_knee_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(knee_right_hip_vecs, right_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_mid_hip_hip_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_mid_hip_vecs, left_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_shoulder_elbow_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_shoulder_vecs, shoulder_elbow_vecs), axis=1), -1.0, 1.0)))
    hip_knee_ankle_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(hip_knee_vecs, ankle_knee_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    # 视频所需
    # upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    # upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
    #
    # print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    # print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    # neck_mid_hip_hip_angles 和 hip_knee_ankle_angles 的问题
    # print(mid_hip_hip_knee_angles)
    # print(neck_mid_hip_hip_angles)
    # print(mid_hip_left_hip_knee_angles)
    # print(hip_knee_ankle_angles)
    correct = True
    feedback = ''
    # 右腿没展开
    if mid_hip_hip_knee_angles < 83.0:
        correct = False
        feedback += 'Your legs don''t seem to be moving big enough. Maybe you should try to take a bigger step and keep your legs straight.\n'
    #  腰没下弯
    if neck_mid_hip_hip_angles > 52.0:
        correct = False
        feedback += 'Your waist may not bend down enough, you should bend down as much as possible while maintaining stability.\n'
    # 上直臂角度不对
    if neck_shoulder_elbow_angles < 155.0:
        correct = False
        feedback += 'Your arm may not be straight up. Please adjust the angle of arm extension to make ' + \
                    'it stretch up vertically as much as possible, which is conducive to the coordinated ' + \
                    'development of the body'
    # 左腿不直
    if hip_knee_ankle_angles < 169.0:
        correct = False
        feedback += 'Your legs may not be straight. Maybe you can do as many warm-up exercises or ' \
                    'leg exercises as you can, but be careful not to strain your legs.\n'
    if correct:
        return (
        correct, 'Exercise performed correctly! Weight was lifted fully.')
    else:
        return (correct, feedback)


def _half_moon2(pose_seq):
    # find the arm that is seen most consistently
    poses = pose_seq.poses
    # right_present = [1 for pose in poses
    #                  if pose.right_knee.exists and pose.right_hip.exists and pose.right_ankle.exists]
    # left_present = [1 for pose in poses
    #                 if pose.left_knee.exists and pose.left_hip.exists and pose.left_ankle.exists]
    right_present = [1 for pose in poses
                     if pose.right_shoulder.y > pose.left_shoulder.y]
    left_present = [1 for pose in poses
                    if pose.left_shoulder.y > pose.right_shoulder.y]
    right_count = sum(right_present)
    left_count = sum(left_present)
    # ==为左边，左右算法有待改进
    side = 'right' if right_count > left_count else 'left'
    # print(right_count, left_count)
    # [print(pose.left_shoulder.y, pose.right_shoulder.y) for pose in poses]
    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_knee, pose.right_hip, pose.right_ankle, pose.mid_hip, pose.neck, pose.left_knee, pose.left_hip, pose.left_shoulder, pose.left_elbow) for pose in poses]
    else:
        joints = [(pose.left_knee, pose.left_hip, pose.left_ankle, pose.mid_hip, pose.neck, pose.right_knee, pose.right_hip, pose.right_shoulder, pose.right_elbow) for pose in poses]
    #                        0         1            2            3          4           5          6            7               8

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 四个角度，八个肢体向量
    # 上大腿
    knee_right_hip_vecs = np.array([(joint[5].x - joint[6].x, joint[5].y - joint[6].y) for joint in joints])
    # 中点到侧臀
    right_hip_mid_hip_vecs = np.array([(joint[3].x - joint[6].x, joint[3].y - joint[6].y) for joint in joints])
    # 脖子到中点
    neck_mid_hip_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    left_hip_mid_hip_vecs = np.array([(joint[1].x - joint[3].x, joint[1].y - joint[3].y) for joint in joints])
    # 另一侧中点到侧臀
    # 上直臂两向量
    neck_shoulder_vecs = np.array([(joint[4].x - joint[7].x, joint[4].y - joint[7].y) for joint in joints])
    shoulder_elbow_vecs = np.array([(joint[8].x - joint[7].x, joint[8].y - joint[7].y) for joint in joints])

    # 膝盖到臀部
    hip_knee_vecs = np.array([(joint[1].x - joint[0].x, joint[1].y - joint[0].y) for joint in joints])

    # 下肢
    ankle_knee_vecs = np.array([(joint[2].x - joint[0].x, joint[2].y - joint[0].y) for joint in joints])

    # normalize vectors
    knee_right_hip_vecs = knee_right_hip_vecs / np.expand_dims(np.linalg.norm(knee_right_hip_vecs, axis=1), axis=1)
    right_hip_mid_hip_vecs = right_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(right_hip_mid_hip_vecs, axis=1), axis=1)
    neck_mid_hip_vecs = neck_mid_hip_vecs / np.expand_dims(np.linalg.norm(neck_mid_hip_vecs, axis=1), axis=1)
    left_hip_mid_hip_vecs = left_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(left_hip_mid_hip_vecs, axis=1), axis=1)
    neck_shoulder_vecs = neck_shoulder_vecs / np.expand_dims(np.linalg.norm(neck_shoulder_vecs, axis=1), axis=1)
    shoulder_elbow_vecs = shoulder_elbow_vecs / np.expand_dims(np.linalg.norm(shoulder_elbow_vecs, axis=1), axis=1)
    hip_knee_vecs = hip_knee_vecs / np.expand_dims(np.linalg.norm(hip_knee_vecs, axis=1), axis=1)
    ankle_knee_vecs = ankle_knee_vecs / np.expand_dims(np.linalg.norm(ankle_knee_vecs, axis=1), axis=1)

    mid_hip_hip_knee_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(knee_right_hip_vecs, right_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_mid_hip_hip_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_mid_hip_vecs, left_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_shoulder_elbow_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_shoulder_vecs, shoulder_elbow_vecs), axis=1), -1.0, 1.0)))
    hip_knee_ankle_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(hip_knee_vecs, ankle_knee_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    # 视频所需
    # upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    # upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
    #
    # print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    # print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    # neck_mid_hip_hip_angles 和 hip_knee_ankle_angles 的问题
    # print(mid_hip_hip_knee_angles)
    # print(neck_mid_hip_hip_angles)
    # print(mid_hip_left_hip_knee_angles)
    # print(hip_knee_ankle_angles)
    correct = True
    feedback = ''
    # 右腿没展开
    if mid_hip_hip_knee_angles < 105.0:
        correct = False
        feedback += 'Your legs don''t seem to be moving big enough. Maybe you should try to take a bigger step and keep your legs straight up.\n'
    #  腰没下弯
    if neck_mid_hip_hip_angles > 89.0:
        correct = False
        feedback += 'Your waist may not bend down enough, you should bend down as much as possible while maintaining stability.\n'
    # 上直臂角度不对
    if neck_shoulder_elbow_angles < 150.0:
        correct = False
        feedback += 'Your arm may not be straight up. Please adjust the angle of arm extension to make ' + \
                    'it stretch up vertically as much as possible, which is conducive to the coordinated ' + \
                    'development of the body'
    # 左腿不直
    if hip_knee_ankle_angles < 169.0:
        correct = False
        feedback += 'Your legs may not be straight. Maybe you can do as many warm-up exercises or ' \
                    'leg exercises as you can, but be careful not to strain your legs.\n'
    if correct:
        return (
        correct, 'Exercise performed correctly! Weight was lifted fully.')
    else:
        return (correct, feedback)


def _half_moon3(pose_seq):
    # find the arm that is seen most consistently
    poses = pose_seq.poses
    # right_present = [1 for pose in poses
    #                  if pose.right_knee.exists and pose.right_hip.exists and pose.right_ankle.exists]
    # left_present = [1 for pose in poses
    #                 if pose.left_knee.exists and pose.left_hip.exists and pose.left_ankle.exists]
    right_present = [1 for pose in poses
                     if pose.right_shoulder.y > pose.left_shoulder.y]
    left_present = [1 for pose in poses
                    if pose.left_shoulder.y > pose.right_shoulder.y]
    right_count = sum(right_present)
    left_count = sum(left_present)
    # ==为左边，左右算法有待改进
    side = 'right' if right_count > left_count else 'left'
    # print(right_count, left_count)
    # [print(pose.left_shoulder.y, pose.right_shoulder.y) for pose in poses]
    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_knee, pose.right_hip, pose.right_ankle, pose.mid_hip, pose.neck, pose.left_knee, pose.left_hip, pose.left_ankle) for pose in poses]
    else:
        joints = [(pose.left_knee, pose.left_hip, pose.left_ankle, pose.mid_hip, pose.neck, pose.right_knee, pose.right_hip, pose.right_ankle,) for pose in poses]
    #                        0         1            2            3          4           5          6            7
    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 四个角度，八个肢体向量
    # 上大腿
    knee_right_hip_vecs = np.array([(joint[5].x - joint[6].x, joint[5].y - joint[6].y) for joint in joints])
    # 中点到侧臀
    right_hip_mid_hip_vecs = np.array([(joint[3].x - joint[6].x, joint[3].y - joint[6].y) for joint in joints])
    # 脖子到中点
    neck_mid_hip_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    # 另一侧中点到侧臀
    left_hip_mid_hip_vecs = np.array([(joint[1].x - joint[3].x, joint[1].y - joint[3].y) for joint in joints])

    # 膝盖到臀部
    hip_knee_vecs = np.array([(joint[1].x - joint[0].x, joint[1].y - joint[0].y) for joint in joints])

    # 下肢
    ankle_knee_vecs = np.array([(joint[2].x - joint[0].x, joint[2].y - joint[0].y) for joint in joints])

    # normalize vectors
    knee_right_hip_vecs = knee_right_hip_vecs / np.expand_dims(np.linalg.norm(knee_right_hip_vecs, axis=1), axis=1)
    right_hip_mid_hip_vecs = right_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(right_hip_mid_hip_vecs, axis=1), axis=1)
    neck_mid_hip_vecs = neck_mid_hip_vecs / np.expand_dims(np.linalg.norm(neck_mid_hip_vecs, axis=1), axis=1)
    left_hip_mid_hip_vecs = left_hip_mid_hip_vecs / np.expand_dims(np.linalg.norm(left_hip_mid_hip_vecs, axis=1), axis=1)
    hip_knee_vecs = hip_knee_vecs / np.expand_dims(np.linalg.norm(hip_knee_vecs, axis=1), axis=1)
    ankle_knee_vecs = ankle_knee_vecs / np.expand_dims(np.linalg.norm(ankle_knee_vecs, axis=1), axis=1)

    mid_hip_hip_knee_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(knee_right_hip_vecs, right_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    neck_mid_hip_hip_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(neck_mid_hip_vecs, left_hip_mid_hip_vecs), axis=1), -1.0, 1.0)))
    mid_hip_left_hip_knee_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(left_hip_mid_hip_vecs, hip_knee_vecs), axis=1), -1.0, 1.0)))
    hip_knee_ankle_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(hip_knee_vecs, ankle_knee_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    # 视频所需
    # upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    # upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
    #
    # print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    # print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    # neck_mid_hip_hip_angles 和 hip_knee_ankle_angles 的问题
    # print(mid_hip_hip_knee_angles)
    # print(neck_mid_hip_hip_angles)
    # print(mid_hip_left_hip_knee_angles)
    # print(hip_knee_ankle_angles)
    correct = True
    feedback = ''
    # 右腿没展开
    if mid_hip_hip_knee_angles < 83.0:
        correct = False
        feedback += 'Your legs don''t seem to be moving big enough. Maybe you should try to take a bigger step and keep your legs straight.\n'
    #  腰没下弯
    if neck_mid_hip_hip_angles > 52.0:
        correct = False
        feedback += 'Your waist may not bend down enough, you should bend down as much as possible while maintaining stability.\n'
    # 左腿没迈出去
    if mid_hip_left_hip_knee_angles < 155.0:
        correct = False
        feedback += 'Your legs don''t seem to be moving big enough. Maybe you should try to take a bigger step and keep your legs straight..\n'
    # 左腿不直
    if hip_knee_ankle_angles < 172.0:
        correct = False
        feedback += 'Your legs may not be straight. Maybe you can do as many warm-up exercises or ' \
                    'leg exercises as you can, but be careful not to strain your legs.\n'
    if correct:
        return (
        correct, 'Exercise performed correctly! Weight was lifted fully.')
    else:
        return (correct, feedback)


def _shushi(pose_seq):
    # find the arm that is seen most consistently
    # poses为很多个姿势列表，根据json文件而定
    poses = pose_seq.poses
    right_present = [1 for pose in poses
                     if pose.right_shoulder.exists and pose.right_elbow.exists and pose.right_hip.exists and pose.right_knee.exists and pose.right_ankle.exists]
    left_present = [1 for pose in poses
                    if pose.left_shoulder.exists and pose.left_elbow.exists and pose.left_hip.exists and pose.left_knee.exists and pose.left_ankle.exists]
    right_count = sum(right_present)
    left_count = sum(left_present)
    side = 'left' if right_count < left_count else 'right'

    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_shoulder, pose.right_elbow, pose.right_knee, pose.right_hip, pose.neck, pose.right_ankle, pose.mid_hip) for pose in poses]
    else:
        joints = [(pose.left_shoulder, pose.left_elbow, pose.left_knee, pose.left_hip, pose.neck, pose.left_ankle, pose.mid_hip) for pose in poses]
    #              0               1            2           3          4          5            6
    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 上胳膊向量
    upper_arm_vecs = np.array([(joint[1].x - joint[0].x, joint[1].y - joint[0].y) for joint in joints])
    # 肩部到脖子的向量
    shoulder_neck_vecs = np.array([(joint[4].x - joint[0].x, joint[4].y - joint[0].y) for joint in joints])
    # 身体中心躯干向量
    torso_vecs = np.array([(joint[4].x - joint[6].x, joint[4].y - joint[6].y) for joint in joints])
    # 中心点到臀的横向量
    mid_hip_vecs = np.array([(joint[3].x - joint[6].x, joint[3].y - joint[6].y) for joint in joints])
    # 大腿肢体
    hip_knee_vecs = np.array([(joint[3].x - joint[2].x, joint[3].y - joint[2].y) for joint in joints])
    # 小腿肢体
    ankle_knee_vecs = np.array([(joint[5].x - joint[2].x, joint[5].y - joint[2].y) for joint in joints])

    # normalize vectors
    upper_arm_vecs = upper_arm_vecs / np.expand_dims(np.linalg.norm(upper_arm_vecs, axis=1), axis=1)
    torso_vecs = torso_vecs / np.expand_dims(np.linalg.norm(torso_vecs, axis=1), axis=1)
    mid_hip_vecs = mid_hip_vecs / np.expand_dims(np.linalg.norm(mid_hip_vecs, axis=1), axis=1)
    hip_knee_vecs = hip_knee_vecs / np.expand_dims(np.linalg.norm(hip_knee_vecs, axis=1), axis=1)
    ankle_knee_vecs = ankle_knee_vecs / np.expand_dims(np.linalg.norm(ankle_knee_vecs, axis=1), axis=1)
    shoulder_neck_vecs = shoulder_neck_vecs / np.expand_dims(np.linalg.norm(shoulder_neck_vecs, axis=1), axis=1)

    elbow_shoulder_neck_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(upper_arm_vecs, shoulder_neck_vecs), axis=1), -1.0, 1.0)))
    neck_mid_hip_hip_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(torso_vecs, mid_hip_vecs), axis=1), -1.0, 1.0)))
    mid_hip_hip_ankle_angles = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(hip_knee_vecs, ankle_knee_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    # 视频中存在范围
    # upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    # upper_arm_forearm_min = np.min(upper_arm_forearm_angles)
    #
    # print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    # print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    correct = True
    feedback = ''

    if elbow_shoulder_neck_angles > 99.0:
        correct = False
        feedback += 'Your upper arm is up, but it''s too far from your head.' + \
                    'Try to make your upper arm as perpendicular to your shoulder as possible.\n'

    if neck_mid_hip_hip_angles < 85.0:
        correct = False
        feedback += 'Your upper torso doesn''t seem to stand straight. Maybe you need more practice to improve your stability until you stand straight.\n'

    if mid_hip_hip_ankle_angles > 35.0:
        correct = False
        feedback += 'Your lower leg doesn''t seem to be bent enough. It''s a bit difficult for beginners to reach the standard. ' + \
                                                                      'Try to practice to increase the flexibility of your lower leg.\n'
    if correct:
        return (
        correct, 'Exercise performed correctly! Weight was lifted fully up, and lower leg shows perfectly!.')
    else:
        return (correct, feedback)


def _bicep_curl(pose_seq):
    # find the arm that is seen most consistently
    poses = pose_seq.poses
    right_present = [1 for pose in poses 
            if pose.right_shoulder.exists and pose.right_elbow.exists and pose.rwrist.exists]
    left_present = [1 for pose in poses
            if pose.left_shoulder.exists and pose.left_elbow.exists and pose.lwrist.exists]
    right_count = sum(right_present)
    left_count = sum(left_present)
    side = 'right' if right_count > left_count else 'left'

    print('Exercise arm detected as: {}.'.format(side))

    if side == 'right':
        joints = [(pose.right_shoulder, pose.right_elbow, pose.rwrist, pose.right_hip, pose.neck) for pose in poses]
    else:
        joints = [(pose.left_shoulder, pose.left_elbow, pose.lwrist, pose.left_hip, pose.neck) for pose in poses]

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    # 上肢
    upper_arm_vecs = np.array([(joint[0].x - joint[1].x, joint[0].y - joint[1].y) for joint in joints])
    # 身体躯干
    torso_vecs = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    # 下肢
    forearm_vecs = np.array([(joint[2].x - joint[1].x, joint[2].y - joint[1].y) for joint in joints])

    # normalize vectors
    upper_arm_vecs = upper_arm_vecs / np.expand_dims(np.linalg.norm(upper_arm_vecs, axis=1), axis=1)
    torso_vecs = torso_vecs / np.expand_dims(np.linalg.norm(torso_vecs, axis=1), axis=1)
    forearm_vecs = forearm_vecs / np.expand_dims(np.linalg.norm(forearm_vecs, axis=1), axis=1)

    upper_arm_torso_angles = np.degrees(np.arccos(np.clip(np.sum(np.multiply(upper_arm_vecs, torso_vecs), axis=1), -1.0, 1.0)))
    upper_arm_forearm_angles = np.degrees(np.arccos(np.clip(np.sum(np.multiply(upper_arm_vecs, forearm_vecs), axis=1), -1.0, 1.0)))

    # use thresholds learned from analysis
    upper_arm_torso_range = np.max(upper_arm_torso_angles) - np.min(upper_arm_torso_angles)
    upper_arm_forearm_min = np.min(upper_arm_forearm_angles)

    print('Upper arm and torso angle range: {}'.format(upper_arm_torso_range))
    print('Upper arm and forearm minimum angle: {}'.format(upper_arm_forearm_min))

    correct = True
    feedback = ''

    if upper_arm_torso_range > 35.0:
        correct = False
        feedback += 'Your upper arm shows significant rotation around the shoulder when curling. Try holding your upper arm still, parallel to your chest, ' + \
                    'and concentrate on rotating around your elbow only.\n'
    
    if upper_arm_forearm_min > 70.0:
        correct = False
        feedback += 'You are not curling the weight all the way to the top, up to your shoulders. Try to curl your arm completely so that your forearm is parallel with your torso. It may help to use lighter weight.\n'

    if correct:
        return (correct, 'Exercise performed correctly! Weight was lifted fully up, and upper arm did not move significantly.')
    else:
        return (correct, feedback)


def _front_raise(pose_seq):
    poses = pose_seq.poses

    right_present = [1 for pose in poses 
            if pose.right_shoulder.exists and pose.right_elbow.exists and pose.rwrist.exists]
    left_present = [1 for pose in poses
            if pose.left_shoulder.exists and pose.left_elbow.exists and pose.lwrist.exists]
    right_count = sum(right_present)
    left_count = sum(left_present)
    side = 'right' if right_count > left_count else 'left'

    print('Exercise arm detected as: {}.'.format(side))
    
    if side == 'right':
        joints = [(pose.right_shoulder, pose.right_elbow, pose.rwrist, pose.right_hip, pose.neck) for pose in poses]
    else:
        joints = [(pose.left_shoulder, pose.left_elbow, pose.lwrist, pose.left_hip, pose.neck) for pose in poses]

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    joints = np.array(joints)
    
    # Neck to hip
    back_vec = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    # Check range of motion of the back
    back_vec_range = np.max(back_vec, axis=0) - np.min(back_vec, axis=0)
    print("Horizontal range of motion for back: %s" % back_vec_range[0])
    
    # Shoulder to hip    
    torso_vecs = np.array([(joint[0].x - joint[3].x, joint[0].y - joint[3].y) for joint in joints])
    # Arm
    arm_vecs = np.array([(joint[0].x - joint[2].x, joint[0].y - joint[2].y) for joint in joints])
    
    # normalize vectors
    torso_vecs = torso_vecs / np.expand_dims(np.linalg.norm(torso_vecs, axis=1), axis=1)
    arm_vecs = arm_vecs / np.expand_dims(np.linalg.norm(arm_vecs, axis=1), axis=1)
    
    # Check if raised all the way up
    angles = np.degrees(np.arccos(np.clip(np.sum(np.multiply(torso_vecs, arm_vecs), axis=1), -1.0, 1.0)))
    print("Max angle between torso and arm when lifting: ", np.max(angles))

    correct = True
    feedback = ''

    if back_vec_range[0] > 0.3:
        correct = False
        feedback += 'Your back shows significant movement. Try keeping your back straight and still when you lift the weight. Consider using lighter weight.\n'

    if np.max(angles) < 90.0:
        correct = False
        feedback += 'You are not lifting the weight all the way up. Finish with wrists at or slightly above shoulder level.\n'

    if correct:
        return (correct, 'Exercise performed correctly! Weight was lifted fully up, and no significant back movement was detected.')
    else:
        return (correct, feedback)


def _shoulder_shrug(pose_seq):
    poses = pose_seq.poses

    joints = [(pose.left_shoulder, pose.right_shoulder, pose.left_elbow, pose.right_elbow, pose.lwrist, pose.rwrist) for pose in poses]

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    joints = np.array(joints)
    
    # Shoulder position
    shoulders = np.array([(joint[0].y, joint[1].y) for joint in joints])

    # Straining back
    shoulder_range = np.max(shoulders, axis=0) - np.min(shoulders, axis=0)
    print("Range of motion for shoulders: %s" % np.average(shoulder_range))
    
    # Shoulder to elbow    
    upper_arm_vecs = np.array([(joint[0].x - joint[2].x, joint[0].y - joint[2].y) for joint in joints])
    # Elbow to wrist
    forearm_vecs = np.array([(joint[2].x - joint[4].x, joint[2].y - joint[4].y) for joint in joints])
    
    # normalize vectors
    # np.linalg.norm(upper_arm_vecs, axis=1):求多个行的平方和开根号
    upper_arm_vecs = upper_arm_vecs / np.expand_dims(np.linalg.norm(upper_arm_vecs, axis=1), axis=1)
    forearm_vecs = forearm_vecs / np.expand_dims(np.linalg.norm(forearm_vecs, axis=1), axis=1)
    
    # Check if raised all the way up
    # np.sum(np.multiply(upper_arm_vecs, forearm_vecs), axis=1按行求和。
    # np.clip(,-1,1)最小值为-1，最大值为1，进行裁剪。
    upper_arm_forearm_angles = np.degrees(np.arccos(np.clip(np.sum(np.multiply(upper_arm_vecs, forearm_vecs), axis=1), -1.0, 1.0)))
    upper_forearm_angle = np.max(upper_arm_forearm_angles)
    print("Max upper arm and forearm angle: ", upper_forearm_angle)

    correct = True
    feedback = ''

    if np.average(shoulder_range) < 0.1:
        correct = False
        feedback += 'Your shoulders do not go through enough motion. Squeeze and raise your shoulders more through the exercise.\n'

    if upper_forearm_angle > 30.0:
        correct = False
        feedback += 'Your arms are bending when lifting. Keep your arms straight and still, and focus on moving only the shoulders.\n'

    if correct:
        return (correct, 'Exercise performed correctly! Shoulders went through full range of motion, and arms remained straight.')
    else:
        return (correct, feedback) 


def _shoulder_press(pose_seq):
    poses = pose_seq.poses
    
    right_present = [1 for pose in poses 
            if pose.right_shoulder.exists and pose.right_elbow.exists and pose.rwrist.exists]
    left_present = [1 for pose in poses
            if pose.left_shoulder.exists and pose.left_elbow.exists and pose.lwrist.exists]
    right_count = sum(right_present)
    left_count = sum(left_present)
    side = 'right' if right_count > left_count else 'left'

    print('Exercise arm detected as: {}.'.format(side))
    
    if side == 'right':
        joints = [(pose.right_shoulder, pose.right_elbow, pose.rwrist, pose.right_hip, pose.neck) for pose in poses]
    else:
        joints = [(pose.left_shoulder, pose.left_elbow, pose.lwrist, pose.left_hip, pose.neck) for pose in poses]

    # filter out data points where a part does not exist
    joints = [joint for joint in joints if all(part.exists for part in joint)]
    joints_ = np.array(joints)
    
    # Neck to hip
    back_vec = np.array([(joint[4].x - joint[3].x, joint[4].y - joint[3].y) for joint in joints])
    # Check range of motion of the back
    # Straining back
    back_vec_range = np.max(back_vec, axis=0) - np.min(back_vec, axis=0)
    print("Range of motion for back: %s" % back_vec_range[0])
    
    # Rolling shoulder too much
    elbow = joints_[:, 1]
    elbow_x = np.array([joint.x for joint in elbow])

    neck = joints_[:, 4]
    neck_x = np.array([joint.x for joint in neck])
    elbow_neck_dist = 0 
    if side =='right':
        elbow_neck_dist = np.min(elbow_x - neck_x)
        print("Minimum distance between elbow and neck: ", np.min(elbow_x - neck_x))
    else:
        elbow_neck_dist = np.min(neck_x - elbow_x)
        print("Minimum distance between elbow and neck: ", np.min(neck_x - elbow_x))
    
    # Shoulder to elbow    
    upper_arm_vecs = np.array([(joint[0].x - joint[1].x, joint[0].y - joint[1].y) for joint in joints])
    # Elbow to wrist
    forearm_vecs = np.array([(joint[2].x - joint[1].x, joint[2].y - joint[1].y) for joint in joints])
    
    # normalize vectors
    upper_arm_vecs = upper_arm_vecs / np.expand_dims(np.linalg.norm(upper_arm_vecs, axis=1), axis=1)
    forearm_vecs = forearm_vecs / np.expand_dims(np.linalg.norm(forearm_vecs, axis=1), axis=1)
    
    # Check if raised all the way up
    upper_arm_forearm_angles = np.degrees(np.arccos(np.clip(np.sum(np.multiply(upper_arm_vecs, forearm_vecs), axis=1), -1.0, 1.0)))
    upper_forearm_angle = np.max(upper_arm_forearm_angles)
    print("Max upper arm and forearm angle: ", np.max(upper_arm_forearm_angles))

    correct = True
    feedback = ''

    if back_vec_range[0] > 0.16:
        correct = False
        feedback += 'Your back shows significant movement while pressing. Try keeping your back straight and still when you lift the weight.\n'
    
    if elbow_neck_dist < -0.12:
        correct = False
        feedback += 'You are rolling your shoulders when you lift the weights. Try to steady your shoulders and keep them parallel.\n'
    
    if upper_forearm_angle < 178:
        correct = False
        feedback += 'You are not lifting the weight all the way up. Extend your arms through the full range of motion. Lower the weight if necessary.\n'

    if correct:
        return (correct, 'Exercise performed correctly! Weight was lifted fully up, shoulders remained parallel, and no significant back movement was detected.')
    else:
        return (correct, feedback)

def _mountain(pose_seq):
    poses = pose_seq.poses

    correct = True
    feedback = False
    joints = [(pose.nose, pose.left_shoulder, pose.left_wrist, pose.right_shoulder, pose.right_wrist, pose.left_hip, pose.left_knee,pose.right_hip, pose.right_knee) for pose in poses]
    #            0           1              2           3             4                  5          6         7          8
    left_shoulder_right_shoulder_vec = np.array([(joint[1].x - joint[3].x, joint[1].y - joint[3].y) for joint in joints])
    left_shoulder_left_wrist_vec = np.array([(joint[1].x - joint[2].x, joint[1].y - joint[2].y) for joint in joints])
    right_shoulder_right_wrist_vec = np.array([(joint[3].x - joint[4].x, joint[3].y - joint[4].y) for joint in joints])
    left_hip_right_hip_vec = np.array([(joint[5].x - joint[7].x, joint[5].y - joint[7].y) for joint in joints])
    left_hip_knee_vec = np.array([(joint[5].x - joint[6].x, joint[5].y - joint[6].y) for joint in joints])
    right_hip_knee_vec = np.array([(joint[7].x - joint[8].x, joint[7].y - joint[8].y) for joint in joints])

    # normalization
    left_shoulder_right_shoulder_vec = left_shoulder_right_shoulder_vec / np.expand_dims(np.linalg.norm(left_shoulder_right_shoulder_vec, axis=1),
                                                                       axis=1)
    left_shoulder_left_wrist_vec = left_shoulder_left_wrist_vec / np.expand_dims(np.linalg.norm(left_shoulder_left_wrist_vec, axis=1), axis=1)
    right_shoulder_right_wrist_vec = right_shoulder_right_wrist_vec / np.expand_dims(np.linalg.norm(right_shoulder_right_wrist_vec, axis=1), axis=1)
    left_hip_right_hip_vec = left_hip_right_hip_vec / np.expand_dims(np.linalg.norm(left_hip_right_hip_vec, axis=1), axis=1)
    left_hip_knee_vec = left_hip_knee_vec / np.expand_dims(np.linalg.norm(left_hip_knee_vec, axis=1), axis=1)
    right_hip_knee_vec = right_hip_knee_vec / np.expand_dims(np.linalg.norm(right_hip_knee_vec, axis=1), axis=1)
    y_vec = np.array([(0, 1)])
    # angles
    # 肩部水平
    shoulder_y_angle = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(left_shoulder_right_shoulder_vec, y_vec), axis=1), -1.0, 1.0)))
    # 手臂与肩膀的夹角
    left_shoulder_wrist_angle = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(left_shoulder_left_wrist_vec, left_shoulder_right_shoulder_vec), axis=1), -1.0, 1.0)))
    right_shoulder_wrist_angle = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(right_shoulder_right_wrist_vec, left_shoulder_right_shoulder_vec), axis=1), -1.0, 1.0)))
    # 上身与地面垂直
    # 髋部水平
    hip_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, y_vec), axis=1), -1.0, 1.0)))
    # 大腿与髋部夹角
    left_hip_knee_angle = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, left_hip_knee_vec), axis=1), -1.0, 1.0)))
    right_hip_knee_angle = np.degrees(
        np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, right_hip_knee_vec), axis=1), -1.0, 1.0)))

    if shoulder_y_angle - 90 > 5:
        correct = False
        feedback += 'your shoulders are not in the same level,check if one of them is higher\n'
    if left_shoulder_wrist_angle - right_shoulder_wrist_angle > 5:
        correct = False
        feedback += 'Your arm seem not head-centered symmetry ,try to close your two arm to your ear respectively\n'

    if hip_y_angle - 90 > 5:
        correct = False
        feedback += 'your left hip and right hip are not in the same level,make sure you buttom if fully on the ground\n'
    if left_hip_knee_angle - right_hip_knee_angle > 5:
        correct = False
        feedback += 'Try to make your legs symmetry\n'

    if correct:
        return (
            correct, 'Exercise performed correctly! Weight was lifted fully up, and lower leg shows perfectly!.')
    else:
        return (correct, feedback)


def _seat(pose_seq):
    poses = pose_seq.poses

    correct = True
    feedback = False
    joints=[(pose.nose,pose.left_shoulder,pose.left_wrist,pose.right_shoulder,pose.right_wrist,pose.left_hip,pose.left_knee,pose.right_hip,pose.right_knee,pose.mid_hip) for pose in poses]
    #            0           1                2                          3             4           5                  6         7              8              9

    nose_hip_vec=np.array([(joint[0].x-joint[9].x,joint[0].y-joint[9].y) for joint in joints])
    left_shoulder_right_shoulder_vec=np.array([(joint[1].x-joint[3].x,joint[1].y-joint[3].y) for joint in joints])
    left_shoulder_left_wrist_vec=np.array([(joint[1].x-joint[2].x,joint[1].y-joint[2].y) for joint in joints])
    right_shoulder_right_wrist_vec=np.array([(joint[3].x-joint[4].x,joint[3].y-joint[4].y) for joint in joints])
    left_hip_right_hip_vec=np.array([(joint[5].x-joint[7].x,joint[5].y-joint[7].y) for joint in joints])
    left_hip_knee_vec=np.array([(joint[5].x-joint[6].x,joint[5].y-joint[6].y) for joint in joints])
    right_hip_knee_vec=np.array([(joint[7].x-joint[8].x,joint[7].y-joint[8].y) for joint in joints])

    #normalization
    nose_hip_vec = nose_hip_vec / np.expand_dims(np.linalg.norm(nose_hip_vec, axis=1), axis=1)
    left_shoulder_right_shoulder_vec = left_shoulder_right_shoulder_vec / np.expand_dims(np.linalg.norm(left_shoulder_right_shoulder_vec, axis=1), axis=1)
    left_shoulder_left_wrist_vec = left_shoulder_left_wrist_vec / np.expand_dims(np.linalg.norm(left_shoulder_left_wrist_vec, axis=1), axis=1)
    right_shoulder_right_wrist_vec = right_shoulder_right_wrist_vec / np.expand_dims(np.linalg.norm(right_shoulder_right_wrist_vec, axis=1), axis=1)
    left_hip_right_hip_vec = left_hip_right_hip_vec / np.expand_dims(np.linalg.norm(left_hip_right_hip_vec, axis=1), axis=1)
    left_hip_knee_vec = left_hip_knee_vec / np.expand_dims(np.linalg.norm(left_hip_knee_vec, axis=1), axis=1)
    right_hip_knee_vec = right_hip_knee_vec / np.expand_dims(np.linalg.norm(right_hip_knee_vec, axis=1), axis=1)
    y_vec=np.array([(0,1)])
    #angles
    #肩部水平
    shoulder_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_shoulder_right_shoulder_vec, y_vec), axis=1), -1.0, 1.0)))
    #手臂与肩膀的夹角
    left_shoulder_wrist_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_shoulder_left_wrist_vec, left_shoulder_right_shoulder_vec), axis=1), -1.0, 1.0)))
    right_shoulder_wrist_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_shoulder_right_wrist_vec, left_shoulder_right_shoulder_vec), axis=1), -1.0, 1.0)))
    #上身与地面垂直
    torso_y_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(nose_hip_vec,y_vec), axis=1), -1.0, 1.0)))
    #髋部水平
    hip_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, y_vec), axis=1), -1.0, 1.0)))
    #大腿与髋部夹角
    left_hip_knee_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, left_hip_knee_vec), axis=1), -1.0, 1.0)))
    right_hip_knee_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_hip_right_hip_vec, right_hip_knee_vec), axis=1), -1.0, 1.0)))

    if shoulder_y_angle-90>5:
        correct=False
        feedback+='your shoulders are not in the same level,check if one of them is higher\n'
    if left_shoulder_wrist_angle-right_shoulder_wrist_angle>5:
        correct=False
        feedback+='Your arm seem not head-centered symmetry ,try to close your two arm to your ear respectively\n'
    if torso_y_angle>5:
        correct = False
        feedback += 'Your torso is not vertical to the ground,try to keep your head \n'
    if hip_y_angle-90>5:
        correct=False
        feedback+='your left hip and right hip are not in the same level,make sure you buttom if fully on the ground\n'
    if left_hip_knee_angle-right_hip_knee_angle>5:
        correct=False
        feedback+='Try to make your legs symmetry\n'

    if correct:
        return (
            correct, 'Exercise performed correctly! Weight was lifted fully up, and lower leg shows perfectly!.')
    else:
        return (correct, feedback)




def _tree_by_wind(pose_seq):
    poses = pose_seq.poses

    correct = True
    feedback = False
    joints = [(pose.left_hip,pose.right_hip,pose.nose,pose.left_knee,pose.left_ankle,pose.right_knee,pose.right_ankle) for pose in poses]
             # 0             1        2       3          4                5          6
    hip_vec=np.array([(joint[0].x-joint[1].x,joint[0].y-joint[1].y) for joint in joints])
    left_hip_knee_vec=np.array([(joint[0].x-joint[3].x,joint[0].y-joint[3].y) for joint in joints])
    right_hip_knee_vec=np.array([(joint[1].x-joint[5].x,joint[1].y-joint[5].y) for joint in joints])

    hip_vec = hip_vec / np.expand_dims(np.linalg.norm(hip_vec, axis=1), axis=1)
    left_hip_knee_vec = left_hip_knee_vec / np.expand_dims(np.linalg.norm(left_hip_knee_vec, axis=1), axis=1)
    right_hip_knee_vec = right_hip_knee_vec / np.expand_dims(np.linalg.norm(right_hip_knee_vec, axis=1), axis=1)

    left_hip_knee_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(hip_vec, left_hip_knee_vec), axis=1), -1.0, 1.0)))
    right_hip_knee_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(hip_vec, right_hip_knee_vec), axis=1), -1.0, 1.0)))

    if left_hip_knee_angle-right_hip_knee_angle>5:
        correct=False
        feedback+='Try to keep your hip vertical to the ground and  just tilt torso\n'

    if correct:
        return (
            correct, 'Exercise performed correctly! Weight was lifted fully up, and lower leg shows perfectly!.')
    else:
        return (correct, feedback)


##=========================================================================================================
##
##=========================================================================================================
def _low_bow_stance(pose_seq):
    poses=pose_seq.poses

    correct=True
    feedback=False
    left_present=[1 for pose in poses if pose.left_hip.exists and pose.lear.exists and pose.left_shoulder.exists]
    right_present=[1 for pose in poses if pose.right_hip.exists and pose.rear.exists and pose.right_shoulder.exists]
    left_count=sum(left_present)
    right_count=sum(right_present)

    if left_count>right_count:
        joints = [(pose.left_shoulder,pose.lelbow,pose.left_hip,pose.left_wrist, pose.left_knee, pose.left_ankle, pose.lbigtoe, pose.right_knee, pose.right_ankle, pose.rbigtoe) for pose in poses]
    elif left_count<right_count:
        joints=[(pose.right_shoulder,pose.relbow,pose.right_hip,pose.right_wrist, pose.left_knee, pose.left_ankle, pose.right_knee, pose.right_ankle) for pose in poses]
        #          0               1          2          3             4            5            6           7          8             9
    else:
        correct=False
        feedback+='Fall to detect all the joints needs,Please reinput your picture\n'
        return (correct,feedback)
    for joint in joints:
        if not all(part.exists for part in joint):
            correct=False
            feedback += 'Fall to detect all the joints needs,Please reinput your picture\n'
            return (correct,feedback)

    shoulder_hip_vec=np.array([(joint[2].x-joint[0].x,joint[2].y-joint[0].y) for joint in joints])
    shoulder_elbow_vec=np.array([(joint[1].x-joint[0].x,joint[1].y-joint[0].y) for joint in joints])
    wrist_hip_vec=np.array([(joint[3].x-joint[2].x,joint[3].y-joint[2].y) for joint in joints])


    if joints[4].y<joints[6].y:#左膝垂直
        hip_knee_vec=np.array([(joint[2].x-joint[4].x,joint[2].y-joint[4].y) for joint in joints])
        #ankle_toe_vec=np.array([(joint[5].x-joint[6].x,joint[5].y-joint[6].y) for joint in joints])
        #左小腿
        horizontal_knee_ankle_vec = np.array([(joint[6].x - joint[7].x, joint[6].y - joint[7].y) for joint in joints])
        #右小腿
        vertical_knee_ankle_vec = np.array([(joint[4].x - joint[5].x, joint[4].y - joint[5].y) for joint in joints])
    else:
        hip_knee_vec=np.array([(joint[2].x-joint[6].x,joint[2].y-joint[6].y) for joint in joints])
        #右小腿
        vertical_knee_ankle_vec = np.array([(joint[6].x - joint[7].x, joint[6].y - joint[7].y) for joint in joints])
        #左小腿
        horizontal_knee_ankle_vec = np.array([(joint[4].x - joint[5].x, joint[4].y - joint[5].y) for joint in joints])

    y_vec=np.array([(0,1)])
    #nomalization

    shoulder_hip_vec = shoulder_hip_vec / np.expand_dims(np.linalg.norm(shoulder_hip_vec, axis=1), axis=1)
    shoulder_elbow_vec = shoulder_elbow_vec / np.expand_dims(np.linalg.norm(shoulder_elbow_vec, axis=1), axis=1)
    wrist_hip_vec = wrist_hip_vec / np.expand_dims(np.linalg.norm(wrist_hip_vec, axis=1), axis=1)
    horizontal_knee_ankle_vec = horizontal_knee_ankle_vec / np.expand_dims(np.linalg.norm(horizontal_knee_ankle_vec, axis=1), axis=1)
    hip_knee_vec = hip_knee_vec / np.expand_dims(np.linalg.norm(hip_knee_vec, axis=1), axis=1)
    vertical_knee_ankle_vec = vertical_knee_ankle_vec / np.expand_dims(np.linalg.norm(vertical_knee_ankle_vec, axis=1), axis=1)

    #angle
    #上身与地面垂直
    shoulder_hip_y_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(shoulder_hip_vec, y_vec), axis=1), -1.0, 1.0)))
    #手腕分别放在两侧臀部//向量水平
    wrist_hip_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(wrist_hip_vec, y_vec), axis=1), -1.0, 1.0)))
    #一条，小腿垂直地面,大腿与小腿夹角90以内
    vertical_knee_ankle_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(vertical_knee_ankle_vec, y_vec), axis=1), -1.0, 1.0)))
    hip_knee_ankle_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(hip_knee_vec, vertical_knee_ankle_vec), axis=1), -1.0, 1.0)))
    #另一条腿膝盖尽量贴近地面，脚尖回勾
    horizontal_knee_ankle_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(horizontal_knee_ankle_vec, y_vec), axis=1), -1.0, 1.0)))

    if shoulder_hip_y_angle>5.0 or shoulder_hip_y_angle<175:
        correct=False
        feedback+='Try to keep your torso straight\n'
    if wrist_hip_y_angle<85 or wrist_hip_y_angle>95:
        correct = False
        feedback += 'You should put your hand on your hip\n'
    if vertical_knee_ankle_angle>5.0:
        correct = False
        feedback += 'Try to keep your calf perpendicular to the ground\n'
    if hip_knee_ankle_angle>90.0:
        correct = False
        feedback += 'Try to keep the angle between your calf and your thigh less than 90\n'
    if horizontal_knee_ankle_angle>5.0 or horizontal_knee_ankle_angle<175:
        correct = False
        feedback += 'Try to lower your knees\n'

    if correct:
        return (
            correct, 'Exercise performed correctly! Weight was lifted fully up, and lower leg shows perfectly!.')
    else:
        return (correct, feedback)





def _walking_stick(pose_seq):
    pose=pose_seq.poses[0]

    side='left' if pose.left_shoulder.exists else 'right'

    if side=='left':
        joints=[pose.nose,pose.left_hip,pose.left_knee,pose.left_ankle]
    else:
        joints = [pose.nose, pose.left_hip, pose.left_knee, pose.left_ankle]
        #             0           1           2          3            4
    correct=True
    feedback=''
    #
    torso_vec=np.array([joints[0].x-joints[1].x,joints[0].y-joints[1].y])
    calf_vec=np.array([joints[3].x-joints[2].x,joints[3].y-joints[2].y])
    thigh_vec=np.array([joints[2].x-joints[1].x,joints[2].y-joints[1].y])

    torso_vec =torso_vec/np.linalg.norm(torso_vec)
    calf_vec = calf_vec / np.linalg.norm(calf_vec)
    thigh_vec = thigh_vec / np.linalg.norm(thigh_vec)

    torso_thigh_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(torso_vec, thigh_vec)), -1.0, 1.0)))
    calf_thigh_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(calf_vec, thigh_vec)), -1.0, 1.0)))

    #上半身坐直
    if torso_thigh_angle>95.0 or torso_thigh_angle<85.0:
        correct=False
        feedback+='keep your torso perpendicular to your leg'
    #腿部打直
    if calf_thigh_angle>5.0:
        correct = False
        feedback += 'your leg is not straight and try to straighten your knee  '


    if correct:
        return (correct, 'Exercise performed correctly! ')
    else:
        return (correct, feedback)

##========================================================================================================
##
##========================================================================================================

def _warrior1(pose_seq):
    #1.上半身与地面垂直：neck和midhip 向量与Y轴角度
    #2.膝盖不能超过脚尖：left_ankle和left_knee小腿与地面垂直
    #3.另外一条腿不能弯曲：ankle knee hip向量平行
    #4.大腿与地面平行：ankle hip向量
    #4.手臂打直：shoulder、elbow、wrist向量平行
    #5.双脚踩实地面
    poses = pose_seq.poses

    correct = True
    feedback = False
    left_present = [1 for pose in poses if pose.left_hip.exists and pose.left_shoulder.exists]
    right_present = [1 for pose in poses if pose.right_hip.exists and pose.right_shoulder.exists]
    left_count = sum(left_present)
    right_count = sum(right_present)

    if left_count > right_count:
        joints = [(pose.left_shoulder, pose.lelbow, pose.left_hip, pose.left_wrist, pose.left_knee, pose.left_ankle,pose.right_knee, pose.right_ankle) for pose in poses]
    elif left_count < right_count:
        joints = [(pose.right_shoulder, pose.relbow, pose.right_hip, pose.right_wrist, pose.left_knee, pose.left_ankle, pose.right_knee, pose.right_ankle) for pose in poses]
        #          0               1                 2          3             4            5            6           7
    else:
        correct = False
        feedback += 'Fall to detect all the joints needs,Please reinput your picture\n'
        return (correct, feedback)
    for joint in joints:
        if not all(part.exists for part in joint):
            correct = False
            feedback += 'Fall to detect all the joints needs,Please reinput your picture\n'
            return (correct, feedback)

    shoulder_wrist_vec=np.array([joints[0].x-joints[3].x,joints[0].y-joints[3].y])
    shoulder_hip_vec=np.array([joints[0].x-joints[2].x,joints[0].y-joints[2].y])

    left_knee_hip_vec=np.array([joints[2].x-joints[4].x,joints[2].y-joints[4].y])
    right_knee_hip_vec=np.array([joints[2].x-joints[6].x,joints[2].y-joints[6].y])
    left_knee_left_ankle_vec=np.array([joints[4].x-joints[5].x,joints[4].y-joints[5].y])
    right_knee_right_ankle_vec=np.array([joints[6].x-joints[7].x,joints[6].y-joints[7].y])

    shoulder_wrist_vec = shoulder_wrist_vec / np.linalg.norm(shoulder_wrist_vec)
    shoulder_hip_vec = shoulder_hip_vec / np.linalg.norm(shoulder_hip_vec)
    left_knee_hip_vec = left_knee_hip_vec / np.linalg.norm(left_knee_hip_vec)
    right_knee_hip_vec = right_knee_hip_vec / np.linalg.norm(right_knee_hip_vec)
    left_knee_left_ankle_vec = left_knee_left_ankle_vec / np.linalg.norm(left_knee_left_ankle_vec)
    right_knee_right_ankle_vec = right_knee_right_ankle_vec / np.linalg.norm(right_knee_right_ankle_vec)
    y_vec=np.array([(0,1)])

    #上肢与y轴夹角
    torso_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(shoulder_hip_vec, y_vec)), -1.0, 1.0)))
    #手臂与y轴夹角
    arm_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(shoulder_wrist_vec, y_vec)), -1.0, 1.0)))
    #判断哪只腿在前
    if joints[4].y<joints[6].y:#左腿在前
        #小腿与地面垂直
        fore_calf_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_left_ankle_vec, y_vec)), -1.0, 1.0)))
        #大腿尽量与地面平行
        fore_thigh_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_hip_vec, y_vec)), -1.0, 1.0)))
        #整条腿打直
        pos_calf_thigh_angle=np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_hip_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    else:#右腿在前
        # 小腿与地面垂直
        fore_calf_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_right_ankle_vec, y_vec)), -1.0, 1.0)))
        # 大腿尽量与地面平行
        fore_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_hip_vec, y_vec)), -1.0, 1.0)))
        # 整条腿打直
        pos_calf_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_hip_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    if torso_y_angle>5:
        correct=False
        feedback+='Try to make your torso perpendicular to the ground\n'
    if arm_y_angle>5:
        correct=False
        feedback+='Try to make your arms perpendicular to the ground and keep straight\n'
    if fore_calf_angle>5:
        correct=False
        feedback+='your fore-leg calf should be perpendicular to the ground and make sure to keep your knees behind your toes\n'
    if fore_thigh_angle>90:
        correct = False
        feedback += 'your left thigh should be parallel to the ground\n'
    if pos_calf_thigh_angle>0:
        correct = False
        feedback += 'your right leg should keep straight\n'

    if correct:
        return (correct, 'Exercise performed correctly! ')
    else:
        return (correct, feedback)

##===========================================================================================
##
##===========================================================================================

def _warrior2(pose_seq):
    poses=pose_seq.poses
    joints = [(pose.neck,pose.left_shoulder, pose.right_shoulder,pose.lelbow, pose.relbow,pose.left_wrist,pose.right_wrist,pose.left_hip
               #     0         1              2              3            4          5         6            7
               , pose.right_hip,pose.left_knee, pose.left_ankle, pose.right_knee, pose.right_ankle,pose.mid_hip)for pose in poses]
               #    8           9          10         11           12

    correct=True
    feedback=''
    neck_hip_vec=np.array([joints[0].x-joints[13].x,joints[0].y-joints[13].y])
    left_shoulder_left_wrist_vec=np.array([joints[1].x-joints[5].x,joints[1].y-joints[5].y])
    right_shoulder_right_wrist_vec=np.array([joints[2].x-joints[6].x,joints[2].y-joints[6].y])
    left_hip_left_knee_vec=np.array([joints[7].x-joints[9].x,joints[7].y-joints[9].y])
    left_knee_left_ankle_vec=np.array([joints[9].x-joints[10].x,joints[9].y-joints[10].y])
    right_hip_right_knee_vec=np.array([joints[8].x-joints[11].x,joints[8].y-joints[11].y])
    right_knee_right_ankle_vec=np.array([joints[11].x-joints[12].x,joints[11].y-joints[12].y])

    neck_hip_vec = neck_hip_vec / np.linalg.norm(neck_hip_vec)
    left_shoulder_left_wrist_vec = left_shoulder_left_wrist_vec / np.linalg.norm(left_shoulder_left_wrist_vec)
    right_shoulder_right_wrist_vec = right_shoulder_right_wrist_vec / np.linalg.norm(right_shoulder_right_wrist_vec)
    left_hip_left_knee_vec = left_hip_left_knee_vec / np.linalg.norm(left_hip_left_knee_vec)
    right_hip_right_knee_vec = right_hip_right_knee_vec / np.linalg.norm(right_hip_right_knee_vec)
    left_knee_left_ankle_vec = left_knee_left_ankle_vec / np.linalg.norm(left_knee_left_ankle_vec)
    right_knee_right_ankle_vec = right_knee_right_ankle_vec / np.linalg.norm(right_knee_right_ankle_vec)
    y_vec=np.array([(0,1)])

    torso_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(neck_hip_vec, y_vec)), -1.0, 1.0)))
    left_shoulder_left_wrist_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_shoulder_left_wrist_vec, y_vec)), -1.0, 1.0)))
    right_shoulder_right_wrist_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_shoulder_right_wrist_vec, y_vec)), -1.0, 1.0)))
    # 判断哪只腿在前
    if joints[9].y < joints[11].y:  # 左腿在前
        # 小腿与地面垂直
        fore_calf_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_left_ankle_vec, y_vec)), -1.0, 1.0)))
        # 大腿尽量与地面平行
        fore_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_hip_left_knee_vec, y_vec)), -1.0, 1.0)))
        # 整条腿打直
        pos_calf_thigh_angle = np.degrees(
            np.arccos(np.clip(np.sum(np.multiply(right_hip_right_knee_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    else:  # 右腿在前
        # 小腿与地面垂直
        fore_calf_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_right_ankle_vec, y_vec)), -1.0, 1.0)))
        # 大腿尽量与地面平行
        fore_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_hip_right_knee_vec, y_vec)), -1.0, 1.0)))
        # 整条腿打直
        pos_calf_thigh_angle = np.degrees(
            np.arccos(np.clip(np.sum(np.multiply(left_hip_left_knee_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    if torso_y_angle > 5:
        correct = False
        feedback += 'Try to make your torso perpendicular to the ground\n'
    if left_shoulder_left_wrist_y_angle > 5:
        correct = False
        feedback += 'Try to make your left arms parallel to the ground and keep straight\n'
    if right_shoulder_right_wrist_y_angle > 5:
        correct = False
        feedback += 'Try to make your right arms parallel to the ground and keep straight\n'
    if fore_calf_angle > 5:
        correct = False
        feedback += 'your fore-leg calf should be perpendicular to the ground and make sure to keep your knees behind your toes\n'
    if fore_thigh_angle > 90:
        correct = False
        feedback += 'your left thigh should be parallel to the ground\n'
    if pos_calf_thigh_angle > 0:
        correct = False
        feedback += 'your right leg should keep straight\n'

    if correct:
        return (correct, 'Exercise performed correctly! ')
    else:
        return (correct, feedback)

def _warrior3(pose_seq):
    poses = pose_seq.poses

    correct = True
    feedback = False
    left_present = [1 for pose in poses if pose.left_hip.exists and pose.left_shoulder.exists]
    right_present = [1 for pose in poses if pose.right_hip.exists and pose.right_shoulder.exists]
    left_count = sum(left_present)
    right_count = sum(right_present)

    if left_count > right_count:
        joints = [
            (pose.left_shoulder, pose.lelbow, pose.left_hip, pose.left_wrist, pose.left_knee, pose.left_ankle, pose.right_knee, pose.right_ankle) for
            pose in poses]
    elif left_count < right_count:
        joints = [
            (pose.right_shoulder, pose.relbow, pose.right_hip, pose.right_wrist, pose.left_knee, pose.left_ankle, pose.right_knee, pose.right_ankle) for
            pose in poses]
        #          0               1            2          3             4            5            6           7
    else:
        correct = False
        feedback += 'Fall to detect all the joints needs,Please reinput your picture\n'
        return (correct, feedback)
    for joint in joints:
        if not all(part.exists for part in joint):
            correct = False
            feedback += 'Fall to detect all the joints needs,Please reinput your picture\n'
            return (correct, feedback)

    shoulder_wrist_vec = np.array([joints[0].x - joints[3].x, joints[0].y - joints[3].y])
    shoulder_hip_vec = np.array([joints[0].x - joints[2].x, joints[0].y - joints[2].y])

    left_knee_hip_vec = np.array([joints[2].x - joints[4].x, joints[2].y - joints[4].y])
    right_knee_hip_vec = np.array([joints[2].x - joints[6].x, joints[2].y - joints[6].y])
    left_knee_left_ankle_vec = np.array([joints[4].x - joints[5].x, joints[4].y - joints[5].y])
    right_knee_right_ankle_vec = np.array([joints[6].x - joints[7].x, joints[6].y - joints[7].y])

    shoulder_wrist_vec = shoulder_wrist_vec / np.linalg.norm(shoulder_wrist_vec)
    shoulder_hip_vec = shoulder_hip_vec / np.linalg.norm(shoulder_hip_vec)
    left_knee_hip_vec = left_knee_hip_vec / np.linalg.norm(left_knee_hip_vec)
    right_knee_hip_vec = right_knee_hip_vec / np.linalg.norm(right_knee_hip_vec)
    left_knee_left_ankle_vec = left_knee_left_ankle_vec / np.linalg.norm(left_knee_left_ankle_vec)
    right_knee_right_ankle_vec = right_knee_right_ankle_vec / np.linalg.norm(right_knee_right_ankle_vec)
    y_vec = np.array([(0, 1)])

    # 上肢与y轴夹角
    torso_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(shoulder_hip_vec, y_vec)), -1.0, 1.0)))
    # 手臂与y轴夹角
    arm_y_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(shoulder_wrist_vec, y_vec)), -1.0, 1.0)))
    # 判断哪只腿抬起
    if joints[4].y < joints[6].y:  # 左腿抬起
        # 小腿与地面垂直
        fore_calf_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_left_ankle_vec, y_vec)), -1.0, 1.0)))
        # 大腿尽量与地面平行
        fore_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(left_knee_hip_vec, y_vec)), -1.0, 1.0)))
        # 整条腿打直
        pos_calf_thigh_angle = np.degrees(
            np.arccos(np.clip(np.sum(np.multiply(right_knee_hip_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    else:  # 右腿在上
        # 小腿与地面垂直
        fore_calf_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_right_ankle_vec, y_vec)), -1.0, 1.0)))
        # 大腿尽量与地面平行
        fore_thigh_angle = np.degrees(np.arccos(np.clip(np.sum(np.multiply(right_knee_hip_vec, y_vec)), -1.0, 1.0)))
        # 整条腿打直
        pos_calf_thigh_angle = np.degrees(
            np.arccos(np.clip(np.sum(np.multiply(left_knee_hip_vec, right_knee_right_ankle_vec)), -1.0, 1.0)))

    if torso_y_angle > 95:
        correct = False
        feedback += 'Try to make your torso perpendicular to the ground\n'
    if arm_y_angle > 95:
        correct = False
        feedback += 'Try to make your arms perpendicular to the ground and keep straight\n'
    if fore_calf_angle > 95:
        correct = False
        feedback += 'your fore-leg calf should be parallel to the ground\n'
    if fore_thigh_angle > 95:
        correct = False
        feedback += 'your left thigh should be parallel to the ground\n'
    if pos_calf_thigh_angle > 0:
        correct = False
        feedback += 'your right leg should keep straight\n'
