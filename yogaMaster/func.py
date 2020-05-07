from yoga.settings import MEDIA_ROOT
from yogaMaster.parseParts import parse_sequence
from yogaMaster.evaluate_ch import evaluate_pose


def func(text):
    pose_seq = parse_sequence(MEDIA_ROOT+'file/'+text+'.json')
    (correct, feedback) = evaluate_pose(pose_seq, text)
    if correct:
        return 'Exercise performed correctly!'
    else:
        return 'Exercise could be improved:'+feedback

