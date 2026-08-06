type MyStack struct {
    queue []int
}


func Constructor() MyStack {
    return MyStack{queue : []int{}}
}


func (this *MyStack) Push(x int)  {
    this.queue = append(this.queue, x)
}


func (this *MyStack) Pop() int {
    for i := 0; i < len(this.queue) - 1; i++ {
        // pop first (head) element and add to end of queue
        this.queue = append(this.queue[1:], this.queue[0])
    }
    mostRecentVal := this.queue[0]
    this.queue = this.queue[1:]
    return mostRecentVal
}

func (this *MyStack) Top() int {
    var mostRecentVal int
    for i := 0; i < len(this.queue); i++ {
        if i == len(this.queue) - 1 {
            mostRecentVal = this.queue[0]
        }
        // pop first (head) element and add to end of queue
        this.queue = append(this.queue[1:], this.queue[0])
    }
    return mostRecentVal
}


func (this *MyStack) Empty() bool {
    return len(this.queue) == 0
}


/**
 * Your MyStack object will be instantiated and called as such:
 * obj := Constructor();
 * obj.Push(x);
 * param_2 := obj.Pop();
 * param_3 := obj.Top();
 * param_4 := obj.Empty();
 */