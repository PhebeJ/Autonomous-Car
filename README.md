# Autonomous-Car

Autonomous Car 

## Commands

```
cd src

python gridworld.py -m
python gridworld.py -h
python gridworld.py -g MazeGrid
python gridworld.py -a value -i 100 -k 10
python gridworld.py -a value -i 5
python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.2 --livingReward 0.0
python gridworld.py -a q -k 5 -m
python gridworld.py -a q -k 100 
python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1
python crawler.py
python car.py -p CarQAgent -x 2000 -n 2010 -l smallGrid 
python car.py -p CarQAgent -n 10 -l smallGrid -a numTraining=10
python car.py -p ApproximateQAgent -x 2000 -n 2010 -l smallGrid 
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid 
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumClassic 
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 150 -l mediumGrid -q -f

python car.py -p KeyboardAgent -g DirectionalGhost -x 0 -n 60 -l demoGrid1 -k 0
python car.py -p KeyboardAgent -g DirectionalGhost -x 0 -n 60 -l demoGrid1 -k 1
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 0 -n 60 -l demoGrid1
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 0 -n 60 -l demoGrid2
python car.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l demoGrid2
python car.py -p ApproximateQAgent -g DirectionalGhost -a extractor=SimpleExtractor -x 0 -n 60 -l demoGrid3
```