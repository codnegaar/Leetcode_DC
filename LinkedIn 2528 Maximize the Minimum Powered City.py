'''
LinkedIn 2528 Maximize the Minimum Powered City
 
You are given a 0-indexed integer array stations of length n, where stations[i] represents the number of power stations in the ith city.
Each power station can provide power to every city in a fixed range. In other words, if the range is denoted by r, then a power station at city i can provide power to all cities j such that |i - j| <= r and 0 <= i, j <= n - 1.
Note that |x| denotes absolute value. For example, |7 - 5| = 2 and |3 - 10| = 7.
The power of a city is the total number of power stations it is being provided power from.
The government has sanctioned building k more power stations, each of which can be built in any city, and have the same range as the pre-existing ones.
Given the two integers r and k, return the maximum possible minimum power of a city, if the additional power stations are built optimally.
Note that you can build the k power stations in multiple cities. 

Example 1:
          Input: stations = [1,2,4,5,0], r = 1, k = 2
          Output: 5
          Explanation: 
          One of the optimal ways is to install both the power stations at city 1. 
          So stations will become [1,4,4,5,0].
          - City 0 is provided by 1 + 4 = 5 power stations.
          - City 1 is provided by 1 + 4 + 4 = 9 power stations.
          - City 2 is provided by 4 + 4 + 5 = 13 power stations.
          - City 3 is provided by 5 + 4 = 9 power stations.
          - City 4 is provided by 5 + 0 = 5 power stations.
          So the minimum power of a city is 5.
          Since it is not possible to obtain a larger power, we return 5.

Example 2:
        Input: stations = [4,4,4,4], r = 0, k = 3
        Output: 4
        Explanation: 
        It can be proved that we cannot make the minimum power of a city greater than 4.
         

Constraints:
        n == stations.length
        1 <= n <= 105
        0 <= stations[i] <= 105
        0 <= r <= n - 1
        0 <= k <= 109

'''

class Node:
    def __init__(self):
        self.left=None
        self.right=None
        self.l=0
        self.r=100001
        self.val=0
    
class Tree:
    def __init__(self,n):
        self.root=Node()
        self.root.l=0
        self.root.r=n-1

    def addVal(self,root,l,r,val):
        print(root.l,root.r,l,r,val)
        if(root.l>r or root.r<l or l>r):return
        if(root.l>=l and root.r<=r):
            root.val+=val
            return
        if(root.left==None):
            root.left=Node()
            root.left.l=root.l
            root.left.r=(root.l+root.r)//2
            root.right=Node()
            root.right.l=(root.l+root.r)//2+1
            root.right.r=root.r
        self.addVal(root.left,l,r,val)
        self.addVal(root.right,l,r,val)
    
    
    def add(self,l,r,val):
        self.addVal(self.root,l,r,val)

    def getVal(self,root,i):
        if(root==None or root.l>i or root.r<i):return 0
        if(root.l==i and root.r==i):return root.val
        return self.getVal(root.left,i)+self.getVal(root.right,i)+root.val

    def get(self,i):
        return self.getVal(self.root,i)

    def getMini(self,root,l,r):
        if(root==None):return [l,r,1]
        if(root.l>r or root.r<l):return [l,r,100000000000]

    def mini(self,l,r):
        return self.getMini(self.root,l,r)
    

class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n=len(stations)
        t=Tree(n)
        # for i in range(n):
        #     li=max(i-r,0)
        #     ri=min(n-1,i+r)
        #     # print(li,ri)
        #     t.add(li,ri,stations[i])
        #     print(li,ri,i)
        arr=[0 for i in range(n)]
        for i in range(n):
            l=max(0,i-r)
            h=i+r+1
            # print(i,l,h)
            arr[l]+=stations[i]
            if(h<n):arr[h]-=stations[i]
            # if(i):arr[i]+=arr[i-1]
        
        for i in range(1,n):
            arr[i]+=arr[i-1]

        low=0
        high=100000000000
        # print(arr)
        while(low<high):
            # print(low,high)
            mid=(low+high+1)//2
            d={}
            pre=0
            cnt=0
            for i in range(n):
                pre+=d.get(i,0)
                cur=arr[i]+pre
                if(cur>=mid):continue
                ind=i+2*r+1
                dif=mid-cur
                d[ind]=d.get(ind,0)-dif
                pre+=dif
                cnt+=dif
                if(cnt>k):break
            # print(cnt)
            if(cnt>k):
                high=mid-1
            else:
                low=mid
        
        return low


        
