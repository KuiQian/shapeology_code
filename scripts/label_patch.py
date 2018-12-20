"""
map each patch into diffusion-map coordinates.
"""
import pickle as pk
import pydiffmap
import sys
import numpy as np
from lib.utils import calc_err

# Pre-process patch to reduce resolution and filter if too
# noisy. (have flag in the label for that)
class diffusionMap:
    def __init__(self,dmapFilename):
        """diffusionMap labels a patch using a diffusion map

        :param dmapFilename: name of pickle file containing the pydiffmap.dmap object 
        """
        self.Dict=pk.load(open(dmapFilename,'rb'))
        # Dict={'diffusion_map'  : pydiffmap.diffusion_map.DiffusionMap
        #       'Reps'           : VQ Reps
        #       'Counts'         : Count associated with each rep
        #       'coordinates'    : Coordinates of the Reps according to diffusion_map

    def transform(self,data1D):
        """compute the dmap transformation for a list of square patches.

        :param data1D a two dimensional vector where each row is a vector corresponding to a flattened image
        :returns: an array of projected values (shape =  length of list * number of eigenvectors)
        :rtype: numpy array
        """
        lowD=self.Dict['diffusion_map'].transform(data1D)
        return lowD

    def label_patch(self,Patches,smooth_threshold=0.4):
        """compute a label for each raw patch.

        preprocessing replicates the one used in the vector quantization:
        for each patch:
        compare image to smoothed image and if difference is large: reject (return None)
        otherwise reduce resolution by 2 and call transform.

        :param Patches: List of patches
        :param smooth_threshold: if err>smooth_threshold, return None for this patch
        :returns: returns a list of the same length as Patches where each element is either None or a 1d numpy array
        :rtype: list

        """
        err,sub=calc_err(Patches[0])
        _sub_size=sub.shape[0]
        data1D=np.zeros((len(Patches),_sub_size*_sub_size))
        for i in range(len(Patches)):
            patch=Patches[i]
            err,sub=calc_err(patch)
            if err<smooth_threshold:
                data1D[i,:] = sub.flatten();
        dmap=self.transform(data1D)

        labels=[]
        for i in range(dmap.shape[0]):
            proj=dmap[i,:]
            if np.sum(np.abs(data1D[i,:]))==0:
                labels.append(None)
            else:
                labels.append(data1D[i,:])
        return labels


