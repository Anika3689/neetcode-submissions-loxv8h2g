type MinStack struct {
    stk []int
    minHistory []int
}


func Constructor() MinStack {
    return MinStack{stk : []int{}, minHistory: []int{}}
}


func (this *MinStack) Push(value int)  {
    this.stk = append(this.stk, value)
    if len(this.minHistory) == 0 {
        this.minHistory = append(this.minHistory, value)
    } else {
        n := len(this.minHistory)
        this.minHistory = append(this.minHistory, min(this.minHistory[n-1], value))
    }
}


func (this *MinStack) Pop()  {
    n := len(this.stk)
    this.stk = this.stk[:n-1]
    n = len(this.minHistory)
    this.minHistory = this.minHistory[:n-1]
}


func (this *MinStack) Top() int {
    n := len(this.stk)
    return this.stk[n-1]
}


func (this *MinStack) GetMin() int {
    n := len(this.minHistory)
    return this.minHistory[n-1]
}


/**
 * Your MinStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(value);
 * obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.GetMin();
 */