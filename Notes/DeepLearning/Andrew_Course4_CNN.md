 in 
# Course of CNN

########## Week 1
1. The convolution allows it to detect edges. The filter has a design which allows it to modify the input tensor into a smaller representation 
with edges marked. There are both horizontal and vertical filters which detect horizontal and vertical edges. 

2. The weights of the filter can be learnt using backpropagation and you do not need to define a filter matrix.

3. Padding is required for 1. Avoiding reduction in the size of the output layer 2. Better use of the corner and edge pixels. Usually only 
odd filter is used. For a filter of size F, padding to keep the same p = (F - 1)/2
