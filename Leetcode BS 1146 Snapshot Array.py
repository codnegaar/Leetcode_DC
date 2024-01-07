'''
Leetcode BS 1146 Snapshot Array
 
Implement a SnapshotArray that supports the following interface:
        SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
        void set(index, val) sets the element at the given index to be equal to val.
        int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
        int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
         

Example 1:
        Input: ["SnapshotArray","set","snap","set","get"]
        [[3],[0,5],[],[0,6],[0,0]]

        Output: [null,null,0,null,5]

        Explanation: 
                SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
                snapshotArr.set(0,5);  // Set array[0] = 5
                snapshotArr.snap();  // Take a snapshot, return snap_id = 0
                snapshotArr.set(0,6);
                snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5
                 

Constraints:
        1 <= length <= 5 * 104
        0 <= index < length
        0 <= val <= 109
        0 <= snap_id < (the total number of times we call snap())
        At most 5 * 104 calls will be made to set, snap, and get.

'''

class SnapshotArray:
    def bs(self,lt,rt,tr,lst):
        ps=0
        while lt<=rt:
            mid=(lt+rt)//2
            if lst[mid][1]<=tr:
                ps=mid
                lt=mid+1
            else:
                rt=mid-1
        return ps


    def __init__(self, length: int):
        self.lst=[0]*length
        self._id=0
        self.nums=[[(0,0)] for _ in range(length)]
        

    def set(self, index: int, val: int) -> None:
        self.lst[index]=val
        if self.nums[index][-1][1]==self._id:
            self.nums[index][-1]=(val,self._id)
        elif self.nums[index][-1][1]<self._id:
            self.nums[index].append((val,self._id))
        

    def snap(self) -> int:
        x=self._id
        self._id+=1
        return x
        

    def get(self, index: int, snap_id: int) -> int:
        x=self.bs(0,len(self.nums[index])-1,snap_id,self.nums[index])
        return self.nums[index][x][0]

        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
