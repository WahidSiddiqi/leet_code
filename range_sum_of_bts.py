def rangeSumBST(root, L, R):
    if not root:
        return 0
    elif root:
        sum = 0
        if root.val <= R and root.val >= L:
            sum += root.val
    return sum

rangeSumBST([10,5,15,3,7,null,18], L = 7, R = 15)
