from math import floor
def binning(data, nBins, binType, binBy=None):
    data_ = sorted(data)
    bins = [ [] for i in range(nBins)]
    if binType == "equal frequency":
        numElemPerBin=len(data)//nBins;
        for i in range(nBins):
            bins[i]=data_[i*numElemPerBin:(i+1)*numElemPerBin]
    elif binType == "equal range":
        minval = data_[0]
        maxval = data_[-1]
        rangePerBin=(maxval-minval)/nBins
        for i in range(len(data_)):
            if i == len(data_) - 1:
                binNumber= nBins - 1
            else:
                binNumber = int(floor((data_[i]-minval)/rangePerBin))

            bins[binNumber].append(data_[i])
    else:
        print("Please use correct option")

    for i in range(nBins):
        currBin=bins[i]
        #To be continue

if __name__=="__main__":
    print(binning([9,15,21,24,24,11,15,6,26,28,8,21,16,34,29],4,"equal range"))
                
            
        
