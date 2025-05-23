const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

//minheap 로직은 gpt의 도움
class MinHeap {
  constructor() {
    this.heap = [];
  }

  push(val) {
    this.heap.push(val);
    this._bubbleUp();
  }

  pop() {
    const min = this.heap[0];
    const end = this.heap.pop();
    if (this.heap.length > 0) {
      this.heap[0] = end;
      this._sinkDown();
    }
    return min;
  }

  top() {
    return this.heap[0];
  }

  size() {
    return this.heap.length;
  }

  _bubbleUp() {
    let idx = this.heap.length - 1;
    const elem = this.heap[idx];
    while (idx > 0) {
      let parentIdx = Math.floor((idx - 1) / 2);
      let parent = this.heap[parentIdx];
      if (elem >= parent) break;
      this.heap[idx] = parent;
      idx = parentIdx;
    }
    this.heap[idx] = elem;
  }

  _sinkDown() {
    let idx = 0;
    const length = this.heap.length;
    const elem = this.heap[0];

    while (true) {
      let leftIdx = 2 * idx + 1;
      let rightIdx = 2 * idx + 2;
      let swap = null;

      if (leftIdx < length) {
        if (this.heap[leftIdx] < elem) swap = leftIdx;
      }

      if (rightIdx < length) {
        if (
          (swap === null && this.heap[rightIdx] < elem) ||
          (swap !== null && this.heap[rightIdx] < this.heap[leftIdx])
        ) {
          swap = rightIdx;
        }
      }

      if (swap === null) break;
      this.heap[idx] = this.heap[swap];
      idx = swap;
    }
    this.heap[idx] = elem;
  }
}

//내가 짠 로직
const solution = () => {
  const N = +input[0];
  const heap = new MinHeap();

  for (let i = 1; i <= N; i++) {
    const row = input[i].split(" ").map(Number);
    for (const num of row) {
      if (heap.size() < N) {
        heap.push(num);
      } else if (num > heap.top()) {
        heap.pop();
        heap.push(num);
      }
    }
  }

  console.log(heap.top());
};

solution();
