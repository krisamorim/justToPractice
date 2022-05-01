from time import sleep
num = 10
for c in range(0,11):
    print(num)
    sleep(1)
    num = num-1
print('\033[1:30:41mBUM\033[m {} \033[1:33:44mBOM\033[m {} \033[1:31:43mBUM\033[m'.format(' '*5,' '*5))
sleep(1)
print(('{} \033[1;35;43mPOW\033[m {} \033[7:31mBUM\033[m'.format(' '*4, ' '*4)))