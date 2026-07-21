/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
 
func reverseBetween(head *ListNode, left int, right int) *ListNode {
    headCpy := head
    var prev *ListNode
    cur := head
    i := 1
    for ; i < left; i++ {
        prev = cur
        cur = cur.Next
    }

    leftSectionTail := prev
    reversedTail := cur

    for ; i <= right; i++ {
        nextNode := cur.Next
        cur.Next = prev
        prev = cur
        cur = nextNode
    }

    if leftSectionTail != nil {
        leftSectionTail.Next = prev
    }
    reversedTail.Next = cur

    if left == 1 {
        return prev
    }
    return headCpy

}

