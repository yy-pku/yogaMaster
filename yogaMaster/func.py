import argparse
import os
import sys
import subprocess
import numpy as np
import matplotlib.pyplot as plt
from blog.parseParts import parse_sequence
from blog.evaluate_ch import evaluate_pose

def func(text):
    pose_seq = parse_sequence('media/file/'+text+'.json')
    (correct, feedback) = evaluate_pose(pose_seq, text)
    if correct:
        return 'Exercise performed correctly!'
    else:
        return 'Exercise could be improved:'+feedback

