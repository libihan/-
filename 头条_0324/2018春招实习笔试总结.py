
# coding: utf-8

# ## 今日头条

# ### 数组中差为K的数对
# 
# **题目:** 给定n个数，k是差值，计算非重复数字对的个数。
#     
#     第一行输入n,k; 第二行输入n个数
# 
# **解法：** [leetcode532](https://www.cnblogs.com/grandyang/p/6545075.html)
# 
# > 法1_pynums中每个元素+k, 得到新数组new, set(nums)和set(new)取交集
# 
# > 法2：(1)和法1类似，建立一个dic存储nums中元素出现的个数; (2)然后遍历哈希表中的数字, 如果k为0且该数字出现的次数大于1，则结果res自增1; (3)如果k不为0，且用当前数字加上k后得到的新数字也在数组中存在，则结果res自增1
# 
# > 法3：时间换空间。给数组排序，然后使用双指针。遍历排序后的数组，然后在当前数字之后找第一个和当前数之差不小于k的数字，若这个数字和当前数字之差正好为k，那么结果res自增1，然后遍历后面的数字去掉重复数字。

# In[3]:

# O(n) O(n)
def findPairs(nums, k): 
    new = [num+k for num in nums]
    return len(set(nums)&set(new))


# In[4]:

# O(n) O(n)
def findPairs(nums, k): 
    dic = {}
    for num in nums:
        if num in dic:
            dic[num] += 1
        else:
            dic[num] = 1
    
    res = 0
    for num in dic:
        if k == 0 and dic[num] > 1:
            res += 1
        elif k > 0 and num + k in dic:
            res += 1
    return res


# In[5]:

def findPairs(nums, k):
    res = 0
    nums.sort()
    i = 0
    while i < len(nums):
        j = i+1    # i后面的第一个数
        while j < len(nums) and  nums[j] - nums[i] < k:    # 找到第一个和当前数之差≥k的数字
            j += 1
        if j < len(nums) and nums[j] - nums[i] == k:
            res += 1
        while i < len(nums)-1 and nums[i] == nums[i+1]:  # 去重
            i += 1
        i += 1
    return res


# ### 求函数调用次数
# 
# **题目:** 定义两个字符串变量：s和m，再定义两种操作：
# 
# > ① m = s; s = s + s;  ② s = s + m
# 
# > 假设s初始化如下：s = "a", m = s;
# 
# 求最小的操作步骤数, 可以将s拼接到长度等于n。
# 
# **示例：**
# 
# > 输入6，输出3；输入5，输出4；输入7，输出6；输入9，输出4。
# 
# **解法：** 
# 
# > 法1:（递归）从头开始考虑选用①或②
# 
# > 法2：（BFS）模拟层次遍历，每一步两条路走
# 
# > 法3：[leetcode650变形](https://blog.csdn.net/feifeiiong/article/details/76379966)
# 
# > 可以转换为 ① m = s; s = s + m;  ② s = s + m ——> 复制操作m=s和粘贴操作s=s+m
# 
# > ？？
# 
# 

# In[6]:

def get_minpot(s,m,n):
    cnt = 0
    # 截止条件
    if s == n:
        return cnt
    if s > n:
        return n
    return min(get_minpot(s*2,s,n), get_minpot(s+m,m,n)) + 1
def countStep(n):
    return get_minpot(1,1,n)


# In[7]:

def countStep(n):
    step = 0
    queue = [(1,1,step)]    # 初始化为(s,m)
    
    while queue:
        size = len(queue)
        for i in range(size):
            temp = queue.pop(0)
            if temp[0] == n:
                return step
            # 采用①
            if temp[0]*2 <= n:
                queue.append((temp[0]*2,temp[0]))
            # 采用②
            if temp[0] + temp[1] <= n:
                queue.append((temp[0] + temp[1],temp[1]))      
        step += 1  # 每遍历一层，步数+1


# ### 输出666

# In[8]:

nn = [
[
'66666',
'6...6',
'6...6',
'6...6',
'66666'
],[
'....6',
'....6',
'....6',
'....6',
'....6'
],[
'66666',
'....6',
'66666',
'6....',
'66666'
],[
'66666',
'....6',
'66666',
'....6',
'66666'
],[
'6...6',
'6...6',
'66666',
'....6',
'....6'
],[
'66666',
'6....',
'66666',
'....6',
'66666'
],[
'66666',
'6....',
'66666',
'6...6',
'66666'
],[
'66666',
'....6',
'....6',
'....6',
'....6'
],[
'66666',
'6...6',
'66666',
'6...6',
'66666'
],[
'66666',
'6...6',
'66666',
'....6',
'66666'
]
]


# In[9]:

if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()  # 比如输入6+6
        s = str(eval(s))  # 求得s='12'
        
        ans = [[] for _ in range(5)]  # 输出5行
        for i in s:
            x = int(i)
            ans[0].append(nn[x][0])
            ans[1].append(nn[x][1])
            ans[2].append(nn[x][2])
            ans[3].append(nn[x][3])
            ans[4].append(nn[x][4])
        for i in range(5):
            print('..'.join(ans[i]))


# ### Magic
# 
# **题目:** 
# 
# **示例：**
# 
# **解法：** 
# 
# > 都排序，比较平均值大小，均值大A的往均值小的B放数（数a大于B均值，且小于A均值）
# 

# In[10]:

def magic(A, B):
    A = sorted(A)
    B = sorted(B)
    if sum(set(A))/len(A) < sum(set(B))/len(B):
        A, B = B, A
    cnt = 0    
    av_A = sum(set(A))/len(A)
    av_B = sum(set(B))/len(B)
    
    for i in range(len(A)):
        if len(A) <= 1:
            return cnt
        if A[i] > av_B and A[i] < av_A:
            B = set(B)
            B.add(A[i])
            A.pop(i)
            
            print('A:',A)
            print('B:',B)
            cnt += magic(A, B)+1
            break
            
    return cnt


# ### 跳板游戏
# 
# **题目:** 已知空中有N个高度不同的跳板，小T刚开始在高度为0的地方，每次跳跃可以选择和直接当前..
# 
# 
# **解法：** 
# 
# > 不一定每次都要贪心选最好的跳板
# 
# > 比如1 3 4 6，h=2，贪心只能0-2-6，而实际上可以0-2-4-8
# 
# > 解法：每层都存储跳1,2..H高度的结果，层次遍历

# In[11]:

# 考虑不周全的代码
N = [1,3,6]
K = 3  # K次
H = 2  # 高度差

start = 0
N.sort()
for _ in range(K):
    for i in range(len(N)):
        if N[i] - start > H or len(N) == 1 and N[i] - start <= H:  # 找到第一个大于的
            start = 2 * N[i-1] - start
            N.pop(i-1)
            break
print(start)


# In[12]:

N = [1,3,6]
K = 4  # K次
H = 2  # 高度差

vis = [0] * int(1e8)
# 建立一个稀疏向量，存储台阶的位置
a = [0] * int(1e8)
for n in N:
    a[n] = 1

start = 0
step= 0
q = [(start,step)]  # (位置，到该位置要跳多少下)

res = 0  # 高度
while q:
    start, step = q.pop(0)
    if step > K:  # 此处判断>K,是想让K次的最高位置都保存了
        break

    if start > res:
        res = start
    for h in range(1,H+1):  # 一次跳多高
        # 位置有跳板,&可以跳到未被访问的位置
        if a[start+h] and not vis[start+2*h]:
            vis[start+2*h] = True  # 之前跳到过这个位置，不用再存储了
            q.append((start+2*h,step+1))
            
        if start-2*h>0 and a[start-h] and not vis[start-2*h]:
            vis[start+2*h] = True  # 之前跳到过这个位置，不用再存储了
            q.append((start-2*h,step+1))
print(res)      


# In[ ]:



