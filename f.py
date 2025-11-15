total=cnt=0
smax=0
smin=100
score=eval(input('请输入成绩值0~100,-1结束：'))
while score!=-1:
    if score<0 or score>100:
        print('成绩无效')
        score=eval(input('请输入有效的成绩：'))
        continue
    total+=score
    cnt+=1
    if score>smax:
        smax=score
    if score<smin:
        smin=score
    score=eval(input('请输入成绩值0~100,-1结束：'))
print('最高分：{:.2f}'.format(smax))
print('最低分：{:.2f}'.format(smin))
print('总分：{:.2f}'.format(total))
print('平均分：{:.2f}'.format(total/cnt))