############ These are notes of DL Course on Training Strategy #####

##### Week 1
1. Orthogonalization - What to tune to achieve what? Like controls in the car.
  You need to look at the performance at Train/Dev/Test and then real world based on performance in these different places you have 
  to make a call as to what needs to be changed.
2. Setting up a single metric you care about makes a lot of difference in tuning the algorithm like example - F1 Score for classifiers.
   This helps speed up iterating.
3. When dealing with multiple metrics it is hard to combine them so for lot of metrics constraints are sufficient. Accuracy is an optimizing
   metric while running time is a satisfying metric. 
     - Accuracy is an optimizing metric while #FALSE POSITIVES can be a satisfying metrics
4. Make sure that the Dev and Test Set come from the same distributions
5. Training set should be large. The Test set should be large enough to be able to measure the performance of the system.
6. Changing the metric, adding weights to deal with different costs of misclassification
7. Looking at Human Performance provides a good measure of Bayes Error. Avoidable Bias.


###### Week 2
1. Looking at Errors and using that to figure out Bias and Variance problems
   - Creating a Training-Dev set can tell whether it is really a variance problem or whether this is due to training - Dev data mismatch
    data mismatch problem can be identified using a Training-Dev data set
    - If there is a gap between Test and Dev set it may mean that you have overfit to Dev Set, so you may need larger Dev set
    - Ideas around generating data to reduce mismatch between data sets
2. Key ideas around - Transfer learning, Multi Task Learning and End-to-End Learning
    - For end-to-end deep learning do we have sufficient data to model the complexity
