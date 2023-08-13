![intro](https://ucscextension-live-28cd95cf77884d15bb06-01c17c1.divio-media.net/images/python-data-structures-and-a.2e16d0ba.fill-2400x858-c100.jpg)

---

## Top data structure and algorithm

![dsa](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20221017172544/Introduction-to-Data-Structures-and-Algorithms-DSA.png)

---

## Classification of data structure

![classification](https://media.geeksforgeeks.org/wp-content/uploads/20220520182504/ClassificationofDataStructure-660x347.jpg)

---

### What is Data Structure?

> A data structure is defined as a particular way of storing and organizing data in our devices to use the data efficiently and effectively.

### What is Algorithm?

> Algorithm is defined as a process or set of well-defined instructions that are typically used to solve a particular group of problem or perform a specific type of calculation.

### Complexities

> * **Time complexity:** Time complexity is used to measure the amount of time required to execute the code.
> * **Space complexity:** Space complexity means the amount of space required to execute successfully the functionalities of the code.

### Big-O Notation

![big-o notation](https://www.bigocheatsheet.com/img/big-o-cheat-sheet-poster.png)

---

<div align="center" style="color: aqua">
    <h1>Data Structure</h1>
</div>

---

<div align="center">
    <h2>Array</h2>
</div>

#### What is Array?

> Array is a linear data structure that is collection of similar data types. Arrays are stored is contiguous memory locations

<img title="" src="https://www.tutorialspoint.com/data_structures_algorithms/images/arrays1.jpg" alt="array" width="593">

#### Advantages

* Efficient access to elements
* Fast data retrieval
* Memory efficiency
* Versatility
* Easy to implement
* compatibility with hardware
* Arrays are faster than list in python

#### Disadvantages

* Fixed size
* Memory allocation issues
* Insertion and deletion issues
* Wasted space
* Limited data type support
* Lack of flexibility

#### Data types

<img title="" src="https://media.geeksforgeeks.org/wp-content/uploads/CommonArticleDesign2-min.png" alt="array operation" width="606">

#### Worst Case

* **Space**: *O(n)*

* **Lookup:** *O(1)*

* **Append:** *O(1)*

* **Insert:** *O(n)*

* **Delete:** *O(n)*

#### Insertion

![https://www.interviewcake.com/images/svgs/arrays__insert_value.svg?bust=210](https://www.interviewcake.com/images/svgs/arrays__insert_value.svg?bust=210)

#### Deleting

![https://www.interviewcake.com/images/svgs/arrays__delete_value.svg?bust=210](https://www.interviewcake.com/images/svgs/arrays__delete_value.svg?bust=210)

---

<div align="center">
    <h2>Linked List</h1>
</div>

> A linked list organizes items sequentially, with each item storing a ponter to the next one.

#### Worst Case

* **Space:** *O(n)*

* **Prepend:** *O(1)*

* **Append:** *O(1)*

* **Lookup:** *O(n)*

* **Insert:** *O(n)*

* **Delete:** *O(n)*



![https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers_labeled_head_and_tail.svg?bust=210](https://www.interviewcake.com/images/svgs/linked_list__nodes_and_pointers_labeled_head_and_tail.svg?bust=210)

![https://www.interviewcake.com/images/svgs/linked_list__doubly_linked_nodes_and_pointers.svg?bust=210](https://www.interviewcake.com/images/svgs/linked_list__doubly_linked_nodes_and_pointers.svg?bust=210)



#### Strengths:

* Fast operations on the ends

* Flexible size

#### Weakness:

* Costly lookups

#### Uses:

* Stacks and queues 

---

<div align="center">
    <h2>Queue</h2>
</div>

> A queue stores items in a first-in, first-out (FIFO) order.

#### Worst Case

* **Space:** *O(n)*

* **Enqueue:** *o(1)*

* **Dequeue:** *O(1)*

* **Peek:** *O(1)*



![https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png](https://media.geeksforgeeks.org/wp-content/uploads/20220805131014/fifo.png)



#### Strengths:

* Fast operations

#### Uses:

* Breadth-first search

* Printers

* Web servers

* Processes

---

<div align="center">
    <h2>Stack</h2>
</div>

> A stack stores items in a last-in, first-out (LIFO) order.

#### Worst Case

* **Space:** *O(n)*

* **Push:** *O(1)*

* **Pop:** *O(1)*

* **Peek:** *O(1)*



<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4AFEpRMvRGQFhFuFFxJWv7Q_6QbamvXwU-j8-93l4viftRRpa9Itumio-iKqfCMqPpco&usqp=CAU" title="" alt="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4AFEpRMvRGQFhFuFFxJWv7Q_6QbamvXwU-j8-93l4viftRRpa9Itumio-iKqfCMqPpco&usqp=CAU" width="681">



#### Strengths:

* Fast operations

#### Uses:

* The call stack

* Depth-first search

* String parsing

---

<div align="center">
    <h2>Hash Table</h2>
</div>

> A hash table organizes data so you can quickly look up values for a given key.