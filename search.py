# USAGE
# python search.py --index index2.csv --query queries2/img_231.jpg --result-path data


# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
from pyimagesearch.searcher import Searcher
import argparse
import cv2

"""
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())
"""

def find_similar(query):
	"""
	query (str): path to the img
	ex : queries2\img_231.jpg

	return
	list_img (list) : 3 paths of img similar
	"""

	# initialize list
	list_img = []

	# initialize the image descriptor
	cd = ColorDescriptor((8, 12, 3))

	# load the query image and describe it
	query = cv2.imread(query)
	features = cd.describe(query)

	# perform the search
	searcher = Searcher("index2.csv")
	results = searcher.search(features)

	# display the query
	# cv2.imshow("Query", query)

	# loop over the results
	for (score, resultID) in results:

		# add img to list
		list_img.append(str(resultID).replace("\\","/"))

	return list_img

