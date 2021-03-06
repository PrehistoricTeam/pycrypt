import languagescorer
import czechfrequencies as cze

class CzechScorer(languagescorer.LanguageScorer):
	"""Czech scorer, credits for frequencies go to MFF"""
	def __init__(self):
		self.setIdealNgramFrequencies([cze.monograms, cze.bigrams, cze.trigrams, cze.tetragrams, cze.pentagrams])
		self.setWeights([10, 100, 1000, 10000, 100000])