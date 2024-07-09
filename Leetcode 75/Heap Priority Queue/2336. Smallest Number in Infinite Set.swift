class SmallestInfiniteSet
{
    var numbersTaken = Array(repeating: false, count: 1000)
    
    func popSmallest() -> Int {
        let smallestNumberIndex = numbersTaken.firstIndex { !$0 }!
        numbersTaken[smallestNumberIndex] = true
        return smallestNumberIndex + 1
    }
    
    func addBack(_ num: Int) {
        numbersTaken[num - 1] = false        
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * let obj = SmallestInfiniteSet()
 * let ret_1: Int = obj.popSmallest()
 * obj.addBack(num)
 */