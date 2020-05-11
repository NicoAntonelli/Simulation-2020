import numpy as np

def testEvenOdd(array):
    odds = 0
    # We create a copy in order to mantain the original 
    test_array = np.array(array)
    # print(array) # Array already shown
    for i in range(len(test_array)):
        test_array[i] = round(test_array[i]*100)
        if (test_array[i] % 2 != 0):
            odds += 1
    orf = odds/len(test_array)
    print()
    print('------------PARITY TEST------------')
    print('Total length of the array:', len(test_array))
    print('Odds Absolute Frequency:', odds)
    print('Odds Relative Frequency:', orf)
    if(orf<0.45 or orf>0.55):
        print('It seems that this is not a good generator, or may be more iterations are needed')
    else:
        print('It seems to be a good generator')        
    print('-----------------------------------')
    print()
