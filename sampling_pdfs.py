
"""
    Sampling an arbitrary pdf
  -  VEERY SLOW
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# numpy implementation
mu = 0.
sigma = 1.

gaussian_pdf = lambda x: 1./(np.sqrt(2*np.pi*sigma))*np.exp(-(x-mu)**2/(2*sigma**2))


#### REIMPLEMENT IN A VECTORISED FORM
def gaussian_cdf_inv(p, mu=0., sigma=1.):
    """ 
        Inverse CDF of a normal distribution a.k.a. quantile function
        source: https://en.wikipedia.org/wiki/Normal_distribution#Quantile_function
        complexity: O(n^2)
    """    
    def _erf_fn_inv(z):
        assert z<1. and z>-1.
        _k_max = 10
        def c_fn(k):
            return 1. if k==0 else sum([ c_fn(m_)*c_fn(k-1-m_)/(2*m_**2+3*m_+1)for m_ in range(k)])
        return sum([c_fn(k_)/(2*k_+1)*(z*np.sqrt(np.pi)/2.)**(2*k_+1) for k_ in range(_k_max)])
    def _probit_fn_inv(p):
        assert p<1. and p>0.
        return np.sqrt(2)*_erf_fn_inv(2*p-1)
    
    return mu + sigma*_probit_fn_inv(p)



####### UNIVARIATE

###  using inverse transform sampling ###


# scipy implementation
from scipy.stats import norm
N = 100
uniform_samples = np.random.random(N)
pdf_samples = norm.ppf(uniform_samples)



# LEFT: plot uniform samples rotated and attached to cdf plot
# RIGHT: sampled






### using rejection method ###

### Box–Muller transform




###### MULTIVARIATE (using Metropolis-Hastings, Gibbs) 
# http://www.pbr-book.org/3ed-2018/Monte_Carlo_Integration/Sampling_Random_Variables.html
# https://theclevermachine.wordpress.com/tag/multivariate-sampling-methods/
# https://appsilon.com/how-to-sample-from-multidimensional-distributions-using-gibbs-sampling/

### block-wise,

### component-wise 