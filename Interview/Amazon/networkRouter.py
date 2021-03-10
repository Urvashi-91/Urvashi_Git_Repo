Q.There is a network router which recive a continuos stream of packet at each second

let say at t0= 4
at t1= 87
at t2=32

after certain interval every time a querry is fired on this stream let say k=40 at t3 so the program have to return count of smallest value so output is 2 =[4,32] .

at t4=17
at t5=20
at t6=100
at t7== a query is fired where k=50 output= 4 as [32,4,17,20] these timestamp value is smallest then querry.

Point To Note
1.Production Read code
2.Handle all edge cases

Your solution querry computing time is equal to O(log(n)) and your insertion time is also O(log n). and don't used any sorting on whole data

My Solution:-

package tree;

public class ConstructTree {

public static void main(String[] args) {
	// TODO Auto-generated method stub

}
TreeNode root;

public void insert(int val) {
    root = insert(root, val);
}

private TreeNode insert(TreeNode root, int val) {
    if (root == null) {
        return new TreeNode(val);
    }
    if (root.val >= val) {
        root.left = insert(root.left, val);
        root.leftCnt++;
    } else {
        root.right = insert(root.right, val);
    }
    return root;
}

public int find(int k) {
    return find(root, k);
}

public int find(TreeNode root, int k) {
    if (root == null) {
        return 0;
    }
    if (root.val < k) {
        return 1 + root.leftCnt + find(root.right, k);
    } else {
        return find(root.left, k);
    }
}

static class TreeNode {
    int val;
    TreeNode left, right;
    int leftCnt = 0;

    public TreeNode(int val) {
        this.val = val;
    }
}
}