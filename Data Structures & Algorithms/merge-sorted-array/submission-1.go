func merge(nums1 []int, m int, nums2 []int, n int)  {
    i, j := m-1, n-1;
    write := len(nums1) - 1

    for ; i >= 0 && j >= 0; write-- {
        if nums1[i] >= nums2[j] {
            nums1[write] = nums1[i]
            i--
        } else {
            nums1[write] = nums2[j]
            j--
        }
    }

    for ; j >= 0; j, write = j - 1, write - 1{
        nums1[write] = nums2[j]
    }

}