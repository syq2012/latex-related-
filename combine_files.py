import os.path
import sys
# get content from input file (no \begin document) from title
# write to output file 
def get_input_content(title, output):
    try:
        f = open(os.path.abspath('') + '/' + title + '.tex', 'r') 
        try:
            while line:= f.readline():
                # print(line)
                output.write(line)
        except:
            print("error writing file " + title)
        finally:
            f.close()
    except:
        output.write('\n')
        output.write('\\input{' + title + '}\n')
        print('error opening ' + title)

# get content from subfile in given title 
# write to output file
def get_subfile_content(title, output):
    try:
        f = open(os.path.abspath('') + '/' + title + '.tex', 'r') 
        try:
            init = False
            while line:= f.readline():
                # print(line)'

                if init:
                    output.write(line)
                if line.startswith('\\begin{document}\n'):
                	init = True        	
        except:
            print("error writing file " + title)
        finally:
            f.close()
    except:
        output.write('\n')
        output.write('\\subfile{' + title + '}\n')
        print('error opening ' + title)

# go to folder 
# replace \include{x} with content of x.tex if exist 
# store new file in output
def combine(source, output, folder= ''):
    try:
        path = os.path.abspath(folder)
        f = open(path + '/' + source + '.tex', 'r')       
        if os.path.isfile(path + '/' + output + '.tex'):
            if input("output file already exist. are you sure? (y/n)") != "y":
                return
        res = open(path + '/' + output + '.tex', 'w')
        while line := f.readline():
            if line.startswith('\\input'):
                print('adding ' + line[len('\\input{'):-2])
                get_input_content(line[len('\\input{'):-2], res)
            elif line.startswith('\\subfile'):
                print('adding ' + line[len('\\subfile{'):-2])
                get_subfile_content(line[len('\\subfile{'):-2], res)
            else:
                res.write(line)
        f.close()
        res.close()
    except:
        print('error opening file ' + source)  

if __name__ == '__main__':
	if (len(sys.argv) < 3):
		print('please type source file name, output file name and folder')
		exit() 
	else:
		# source file, output file, folder the source file is in
		combine(sys.argv[1], sys.argv[2], sys.argv[3])