# Overview



# Criteria

# Technologies



# Confusing Terms and Concepts:


## Separation Of Compute And Storage

According to [google](https://cloud.google.com/blog/products/bigquery/separation-of-storage-and-compute-in-bigquery):

> Over the past few years, separation of storage and compute has been broadly embraced by distributed analytics technologies. There are tradeoffs, but benefits of scale, performance, cost, ease of use, reliability, data sharing, and durability are attractive in a vast majority of use cases. 

The basic premise is that a solution is built from two discrete layers: a compute layer and a storage layer. In this design, the storage layer is reponsible for physically storing data and is not dependent on the specifications of the compute layer which is responsible for performing the core functions of the solution. Additionally, the 

For example, consider a database: the amount of data being stored should not depend on the size or number of CPUs under this paradigm; the administrator should be able to manage storage and compute capacity independently. Adding or removing a compute sever should generally not impact the availability of data. When a compute node is added it should have the same access to data that all the other compute nodes have. When the node is removed, the cluster should continue to have access to the same data.

The concept of separating compute and storage is something we take for granted in today's marketplace. The traditional (non-separated) model was to have the physical storage device connected directly to the physical compute device (i.e. the hard drive and processor are connected through the same motherboard). This natually lead to bigger and bigger servers until people realized it was chaper and more efficient to scale horizontally rather than vertically.