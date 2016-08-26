import time

class Results:

	def log_results_to_file(self, context, title, testresults):
		f = open(title, "a")
		f.write('\n\n'+testresults+'\n')
		f.write("-----------------------------------------------------------")
		f.close()