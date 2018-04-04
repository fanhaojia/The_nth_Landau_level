import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations
from skmonaco import mcquad

def Laughlin_1d(x0=None, q=3):
    def psi(xs):
        if isinstance(x0, np.ndarray):
            xs = list(xs)
            xs.insert(0, x0)
        elif x0 is not None:
            raise Exception('x0 should be numpy.array')
        wf = np.exp(-sum(x**2 for x in xs)/4.)
        for xi, xj in combinations(xs, 2):
            wf *= (xi - xj)**q
        return wf**2
    return psi

def density(x0=np.linspace(0, 8), q=3, ne=2, npoints=1e5, err=0.05, **kwds):
    #XXX choose ONLY symmetric positive part leads to large error
    l, u = [-10., 10.]
    M, Merr = mcquad(Laughlin_1d(x0=x0, q=q), npoints=npoints, xl=[l]*(ne-1), xu=[u]*(ne-1), **kwds)
    # Caclculate N, which will not affect relative density profile
    # N, Nerr = mcquad(Laughlin_1d(q=q), npoints=npoints, xl=[l]*ne, xu=[u]*ne)
    # This N works only if x0 is large enough
    N = M.sum()*(x0[1]-x0[0])*2 # 2 for positive part only
    reM = Merr/M
    if max(reM) > err:
        print 'Large err for ne={}, q={}: M ~{:.2f}%'.format(ne, q, max(reM)*100)
    return M * ne / N

def plot_density(x=8, nx=None, ne=2, q=3, show=True, **kwds):
    # 8-10 points per unit length is enough.
    x0 = np.linspace(0, x, nx if nx else 9*x)
    npoints = kwds.pop('npoints', ne*1e5) 
    rho = density(x0, q, ne, **kwds)
    fig, ax = plt.subplots()
    ax.plot(x0, rho, 'b')
    ax.plot(-x0, rho, 'b')
    ax.set_xlabel('x')
    ax.set_ylabel(r'$\rho$')
    ax.set_title('ne={}, q={}, npoints={}'.format(ne, q, int(npoints)))
    if show is True:
        plt.show()
    elif show and isinstance(show, str):
        fig.savefig(show)
    else:
        return fig, ax

for i in range(2, 7):
    plot_density(x=9, ne=i, q=3, show='Laughlin_1d_{}f.pdf'.format(i))
