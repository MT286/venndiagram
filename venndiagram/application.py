import argparse
import sys
from venndiagram import __version__
from matplotlib_venn import venn2
from matplotlib_venn import venn3
from matplotlib import pyplot as plt

_version = "venndiagram %s" % __version__

def main():
    parser = argparse.ArgumentParser(prog="venndiagram",
                                     version=_version)
    
    setup_args(parser)
    args = parser.parse_args()
    #args.func(args)
            
    venn(args)
    
    
def check_max3(lst):
    if (len(lst) > 3 or
    len(lst) < 1):
        sys.stderr.write('error: number of input arguments are not between 2 and 3\n')
        sys.exit()
        
        
def setup_args(parser):
    parser.add_argument('-i,', 
                        '--input_files', 
                        nargs = "*",
                        help='', 
                        required = True)
                     
    parser.add_argument('-l,', 
                         '--labels', 
                         nargs = "*",
                         help='', 
                         required = False)
                     
    parser.add_argument('-t,', 
                         '--title', 
                         help='', 
                         required = False,
                         default = '')
                                     
    parser.add_argument('-o,', 
                         '--out', 
                         help = 'png or pdf', 
                         required = False) 
                         
    
def venn(args):
    files =  args.input_files
    labels =  args.labels
    plot_title =  args.title
    out = args.out
        
    # check input
    check_max3(files)
    
    if labels != None:
        if len(labels) != len(files):
            sys.stderr.write('error: number of labels and input files are unequal\n')
            sys.exit()
    
    # name labels if not exists
    if not labels:
        labels = files
        
    # read files
    content_files = []
    for f in files:
        content_files.append(read_file(f))
    
    # create sets
    sets = []
    for c in content_files:
        sets.append(set(c))
    
    # venn2
    if len(files) == 2:
        venn2([sets[0], sets[1]], 
        set_labels = (labels[0], labels[1]))
        
    # venn3
    if len(files) == 3:
        venn3([sets[0], sets[1], sets[2]], 
              set_labels = (labels[0], labels[1], labels[2]))
    
    if plot_title != None:
        plt.title('%s' % plot_title)
    
    
    if not out:
        plt.show()
    else:
        plt.savefig(out)
        
        
        
def read_file(f):
    with open(f, 'r') as F:
        liste = []
        for line in F:
            liste.append(line.strip())
    return(liste)