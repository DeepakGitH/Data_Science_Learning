
# Course of CNN

########## Week 1
1. The convolution allows it to detect edges. The filter has a design which allows it to modify the input tensor into a smaller representation 
with edges marked. There are both horizontal and vertical filters which detect horizontal and vertical edges. 

2. The weights of the filter can be learnt using backpropagation and you do not need to define a filter matrix.

3. Padding is required for 1. Avoiding reduction in the size of the output layer 2. Better use of the corner and edge pixels. Usually only 
odd filter is used. For a filter of size F, padding to keep the same p = (F - 1)/2

4. Convolution is really Cross-Correlation

5. Strided Convolution is where you do not move one step but you move S number of steps. So the size of the output layer is 

[(N + 2p - f + 1)/S + ] by [(N + 2p - f + 1)/S + ] (floor function)

6. COnvolution on volume requires filters the same depth as number of channels

7. Dimensions on the filters - Number of parameters For 3*3*3 + 1 = 28 Parameters per filter and then 10 filter means 280 number of parameters. Learning 280 parameters is easy. The output of convolution is fed to Relu similar to feed forward.
