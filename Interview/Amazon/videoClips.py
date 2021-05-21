'''
Question: Given a list of video clips with start and end positions, write a program to find out the  missing video segments in a given interval
Each video clip comes with two elements start and end which is an integer that indeces into position of clip.

Clips are not ordered.They can overlap.

example of
input: [s = 1, e = 3], [s = 3, e = 5], [s = 2, e = 6], [s = 7, e = 9], [s = 11, e = 13]

output: [s = 6, e = 7], [s = 9, e = 11]

'''

video_clips= [[2,6],[7,9],[1,3],[11,13],[3,5]]
'''
output = [[6,7],[9,11]]
'''


def find_gaps(video_clips):
    video_clips.sort(key=lambda x: x[0])
    prev_start, prev_end = video_clips[0]  # initialised [1,3]
    result = []
    for i in range(1,len(video_clips)):
        current_start, current_end = video_clips[i]
        if prev_end < current_start:  # if prev_end is less than current_start --> GAP
            result.append((prev_end, current_start))

            prev_start = current_start
            prev_end = current_end
        else:
            prev_start = min(prev_start, current_start)
            prev_end = max(prev_end, current_end)


    return result

print(find_gaps(video_clips))