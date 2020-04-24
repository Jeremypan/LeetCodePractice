class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        def get_dep(root):
            if not root:
                return 0
            else:
                return 1+max(get_dep(root.left),get_dep(root.right))
        height=get_dep(root)
        num_col=2**height-1
        self.array=[]
        for i in range(height):
            temp=[]
            for j in range(num_col):
                temp.append("")
            self.array.append(temp)
        self.fill_array(root,0,0,num_col-1)
        return self.array
    
    def fill_array(self,root,height,l,r):
        if root==None:return  #终止条件在此
        mid=(l+r)//2
        self.array[height][mid]=str(root.val)
        if root.right:self.fill_array(root.right,height+1,mid+1,r) #注意不需要return
        if root.left:self.fill_array(root.left,height+1,l,mid-1) #注意不需要return