

from pytest import approx
import ghalton

def test_halton():
	sequencer = ghalton.Halton(5)
	points = sequencer.get(100)
	assert points[0] == approx([0.5, 0.33333333333, 0.2, 0.14285714, 0.0909090909])
	assert points[1] == approx([0.25, 0.6666666666666666, 0.4, 0.2857142857142857, 0.18181818181818182])
	assert points[99] == approx([0.1484375, 0.411522633744856, 0.032, 0.2915451895043732, 0.1652892561983471])
	points = sequencer.get(100)
	assert points[0] != approx([0.5, 0.33333333333, 0.2, 0.14285714, 0.0909090909])
	sequencer.reset()
	points = sequencer.get(100)
	assert points[0] == approx([0.5, 0.33333333333, 0.2, 0.14285714, 0.0909090909])

def test_seeded():
	sequencer68 = ghalton.GeneralizedHalton(5, 68)
	points = sequencer68.get(100)
	assert points[0] == approx([0.5, 0.6666666666666666, 0.4, 0.8571428571428571, 0.7272727272727273])
	assert points[1] == approx([0.25, 0.3333333333333333, 0.6, 0.14285714285714285, 0.2727272727272727])

def test_perm():
	perms = ((0, 1),
			 (0, 2, 1),
			 (0, 4, 2, 3, 1),
			 (0, 6, 5, 4, 3, 2, 1),
			 (0, 8, 2, 10, 4, 9, 5, 6, 1, 7, 3))
	sequencer = ghalton.GeneralizedHalton(perms)
	points = sequencer.get(100)
	assert points[0] == approx([0.5, 0.6666666666666666, 0.8, 0.8571428571428571, 0.7272727272727273])

def test_preset_config():
	dim = 5
	sequencer = ghalton.GeneralizedHalton(ghalton.EA_PERMS[:dim])
	points = sequencer.get(100)
	assert points[0] == approx([0.5, 0.6666666666666666, 0.8, 0.8571428571428571, 0.7272727272727273])

