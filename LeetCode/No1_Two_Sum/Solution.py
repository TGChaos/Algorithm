#!/usr/bin/python
#encoding=utf8

import sys,getopt

def main(argv):
	input_num_list = [];
	target_sum = "";
	try:
		opts,args = getopt.getopt(argv,"",["inputlist=","target_number="]);
	except getopt.GetoptError:
		print "Solution.py --inputlist <> --target_number X \n"
		sys.exit(2)
	for opt,arg in opts:
		if(opt == "--inputlist"):
			input_num_str = arg;
			input_num_list = input_num_str.split(",");
		if(opt == "--target_number"):
			target_sum = arg;
	
	final_result = getSolution(input_num_list,target_sum);
	
	print final_result
	
	#print "your input number list is ",input_num_list;
	#print "your want to find sum of ",target_sum;

def getSolution(input_num_list,target_number):
	for i in range(len(input_num_list)):
		for j in range(i+1,len(input_num_list)):	
			if ((int(input_num_list[i]) + int(input_num_list[j])) == int(target_number)):
				print input_num_list[i],"+",input_num_list[j],"=",target_number
				result = [i,j];
				return result;
			else:
				result = [-1,-1];
	return result;

if __name__ == "__main__":
	main(sys.argv[1:])
