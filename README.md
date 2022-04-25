# CEE201_project
### [Github repository for this project](https://github.com/A72craft/CEE201_Project.git)
## Introduction:
In this project we are asked to come up with a comprehensive covid-19 plan which is made of three parts: opening testing centers, providing the testing material, and picking up all the tests. In the following three parts we will be formatting the problem given and solving it with python.
## Part 1. Opening testing centers (facility location problem)

### Decision variables & Parameters

	Ni = 1 if site is selected and 0 if it is not.
	i =0,1, 2 ,…,9 candidate site indices
	j =0,1, 2 ,…,29 neighborhood indices
	Cij = the cost(distance) between the site and the neighborhood
	Bool(ij) = 1 if the neighborhood j will go to testing site i, 0 if not
### Objective

The objective is that the sum of the cost needs to be minimized. And the cost is equal to the distance times the population of the neighborhood.

>$\sum$(Cij*Boolij)

	MINIMIZE
	233773.39455000003*Bool_(0,_0) + 109201.64834999999*Bool_(0,_1) + 110113.577725*Bool_(0,_2) + 35355.339049999995*Bool_(0,_3) + 97788.03607500001*Bool_(0,_4) + 132876.82265000002*Bool_(0,_5) + 88670.73925*Bool_(0,_6) + 141509.716975*Bool_(0,_7) + 103591.746775*Bool_(0,_8) + 195576.07215000002*Bool_(0,_9) + 18973.665962*Bool_(1,_0) + 129274.90087999999*Bool_(1,_1) + 116516.0933*Bool_(1,_2) + 226291.84699999998*Bool_(1,_3) + 157784.66338*Bool_(1,_4) + 151907.86682*Bool_(1,_5) + 181107.70276*Bool_(1,_6) + 93509.35782*Bool_(1,_7) + 161058.99539999999*Bool_(1,_8) + 74027.0221*Bool_(1,_9) + 153378.6165*Bool_(10,_0) + 190394.32765000002*Bool_(10,_1) + 145773.797375*Bool_(10,_2) + 242538.656725*Bool_(10,_3) + 222963.00142500002*Bool_(10,_4) + 75208.044775*Bool_(10,_5) + 243233.42697499998*Bool_(10,_6) + 158113.883*Bool_(10,_7) + 231638.18769999998*Bool_(10,_8) + 85000.0*Bool_(10,_9) + 151208.46538*Bool_(11,_0) + 41182.52056*Bool_(11,_1) + 55713.5531*Bool_(11,_2) + 61057.35008*Bool_(11,_3) + 31622.7766*Bool_(11,_4) + 109562.7674*Bool_(11,_5) + 34985.71136*Bool_(11,_6) + 73756.35566*Bool_(11,_7) + 37576.588460000006*Bool_(11,_8) + 132966.1611*Bool_(11,_9) + 113564.95938*Bool_(12,_0) + 114825.95525999999*Bool_(12,_1) + 132306.46242*Bool_(12,_2) + 267000.0*Bool_(12,_3) + 144031.24662*Bool_(12,_4) + 237360.48534*Bool_(12,_5) + 176694.65187*Bool_(12,_6) + 91241.43795*Bool_(12,_7) + 144810.22062*Bool_(12,_8) + 163685.67437999998*Bool_(12,_9) + 201121.8536*Bool_(13,_0) + 88600.22575*Bool_(13,_1) + 65192.02405*Bool_(13,_2) + 325960.12025*Bool_(13,_3) + 164924.225*Bool_(13,_4) + 246221.44505*Bool_(13,_5) + 221359.4362*Bool_(13,_6) + 7071.0678100000005*Bool_(13,_7) + 177552.80904999998*Bool_(13,_8) + 186681.54705*Bool_(13,_9) + 171026.313775*Bool_(14,_0) + 47169.90564999999*Bool_(14,_1) + 91787.79875*Bool_(14,_2) + 137295.30217500002*Bool_(14,_3) + 32596.012025*Bool_(14,_4) + 186296.135225*Bool_(14,_5) + 52559.4901*Bool_(14,_6) + 85586.21385*Bool_(14,_7) + 27950.849725000004*Bool_(14,_8) + 176776.6953*Bool_(14,_9) + 160162.41756*Bool_(15,_0) + 55317.26674*Bool_(15,_1) + 90443.35244*Bool_(15,_2) + 100019.998*Bool_(15,_3) + 30000.0*Bool_(15,_4) + 161987.65386*Bool_(15,_5) + 30265.4919*Bool_(15,_6) + 90000.0*Bool_(15,_7) + 22803.5085*Bool_(15,_8) + 162443.83644*Bool_(15,_9) + 93145.04818499999*Bool_(16,_0) + 23430.749024999997*Bool_(16,_1) + 49203.658395*Bool_(16,_2) + 87361.318665*Bool_(16,_3) + 23717.08245*Bool_(16,_4) + 107131.92800999999*Bool_(16,_5) + 38710.4637*Bool_(16,_6) + 42953.463195000004*Bool_(16,_7) + 22896.50628*Bool_(16,_8) + 97672.92357*Bool_(16,_9) + 65215.02894*Bool_(17,_0) + 27730.84925*Bool_(17,_1) + 17464.249200000002*Bool_(17,_2) + 42485.29157*Bool_(17,_3) + 34828.149529999995*Bool_(17,_4) + 31780.49716*Bool_(17,_5) + 40311.28874*Bool_(17,_6) + 31575.306810000002*Bool_(17,_7) + 38418.74542*Bool_(17,_8) + 48877.397639999996*Bool_(17,_9) + 74276.51041999999*Bool_(18,_0) + 23345.23506*Bool_(18,_1) + 25000.0*Bool_(18,_2) + 30413.81265*Bool_(18,_3) + 22825.42442*Bool_(18,_4) + 47434.164899999996*Bool_(18,_5) + 25238.85893*Bool_(18,_6) + 36400.54945*Bool_(18,_7) + 26076.80962*Bool_(18,_8) + 62393.909960000005*Bool_(18,_9) + 183847.7631*Bool_(19,_0) + 79849.85912000001*Bool_(19,_1) + 84899.94110000001*Bool_(19,_2) + 26076.80962*Bool_(19,_3) + 68000.0*Bool_(19,_4) + 112017.85572*Bool_(19,_5) + 59464.27498*Bool_(19,_6) + 108406.64185999999*Bool_(19,_7) + 72249.56748*Bool_(19,_8) + 156588.63304*Bool_(19,_9) + 290814.3738*Bool_(2,_0) + 137640.83697*Bool_(2,_1) + 142270.86843*Bool_(2,_2) + 30149.62686*Bool_(2,_3) + 120037.49415*Bool_(2,_4) + 171656.634*Bool_(2,_5) + 105513.03236999999*Bool_(2,_6) + 178921.7706*Bool_(2,_7) + 126142.77624*Bool_(2,_8) + 246456.89277*Bool_(2,_9) + 153733.5357*Bool_(20,_0) + 69065.18661*Bool_(20,_1) + 106066.01718*Bool_(20,_2) + 214536.71016000002*Bool_(20,_3) + 88588.93836*Bool_(20,_4) + 222182.35755000002*Bool_(20,_5) + 120000.0*Bool_(20,_6) + 76485.29271*Bool_(20,_7) + 88232.64702*Bool_(20,_8) + 178846.30272*Bool_(20,_9) + 49203.658395*Bool_(21,_0) + 80498.44719*Bool_(21,_1) + 84852.813735*Bool_(21,_2) + 157063.68135*Bool_(21,_3) + 96304.20552*Bool_(21,_4) + 131496.19767*Bool_(21,_5) + 112749.722835*Bool_(21,_6) + 63639.610305*Bool_(21,_7) + 96805.21680000001*Bool_(21,_8) + 84905.830185*Bool_(21,_9) + 167705.0983*Bool_(22,_0) + 181796.589625*Bool_(22,_1) + 137295.30217500002*Bool_(22,_2) + 220510.77070000002*Bool_(22,_3) + 211453.30455*Bool_(22,_4) + 52500.0*Bool_(22,_5) + 229265.13035*Bool_(22,_6) + 155563.49185*Bool_(22,_7) + 220354.82749999998*Bool_(22,_8) + 97082.4392*Bool_(22,_9) + 175419.49719*Bool_(23,_0) + 106850.36263999999*Bool_(23,_1) + 44821.869645*Bool_(23,_2) + 206707.52284*Bool_(23,_3) + 150540.69219*Bool_(23,_4) + 93194.688685*Bool_(23,_5) + 180173.52745*Bool_(23,_6) + 81932.89937*Bool_(23,_7) + 162702.9502*Bool_(23,_8) + 112871.60846500001*Bool_(23,_9) + 177279.44043*Bool_(24,_0) + 16970.562747*Bool_(24,_1) + 69971.42274*Bool_(24,_2) + 158404.54538999998*Bool_(24,_3) + 39115.21443*Bool_(24,_4) + 184664.56077*Bool_(24,_5) + 74094.53421*Bool_(24,_6) + 66272.16609*Bool_(24,_7) + 44598.20625*Bool_(24,_8) + 174413.30223*Bool_(24,_9) + 142850.446275*Bool_(25,_0) + 62500.0*Bool_(25,_1) + 98520.302475*Bool_(25,_2) + 176511.33107500002*Bool_(25,_3) + 70400.63919999999*Bool_(25,_4) + 196022.95784999998*Bool_(25,_5) + 93974.73065*Bool_(25,_6) + 77014.609*Bool_(25,_7) + 68282.501425*Bool_(25,_8) + 163878.76617500003*Bool_(25,_9) + 44181.444059999994*Bool_(26,_0) + 144277.51038*Bool_(26,_1) + 136528.38532*Bool_(26,_2) + 244294.9038*Bool_(26,_3) + 170856.66508*Bool_(26,_4) + 177369.67046000002*Bool_(26,_5) + 194010.309*Bool_(26,_6) + 111211.5102*Bool_(26,_7) + 173216.62738000002*Bool_(26,_8) + 100079.96802*Bool_(26,_9) + 120542.523615*Bool_(27,_0) + 86559.22828499999*Bool_(27,_1) + 109510.273485*Bool_(27,_2) + 142507.894515*Bool_(27,_3) + 82975.90011*Bool_(27,_4) + 168006.6963*Bool_(27,_5) + 90049.98612*Bool_(27,_6) + 95459.415465*Bool_(27,_7) + 79159.648815*Bool_(27,_8) + 143577.5052*Bool_(27,_9) + 18062.39187*Bool_(28,_0) + 68426.968365*Bool_(28,_1) + 56304.973139999995*Bool_(28,_2) + 138982.91262*Bool_(28,_3) + 90808.86520500001*Bool_(28,_4) + 87000.0*Bool_(28,_5) + 108135.331875*Bool_(28,_6) + 40388.736059999996*Bool_(28,_7) + 93938.80987499999*Bool_(28,_8) + 35780.581320000005*Bool_(28,_9) + 265766.81508000003*Bool_(29,_0) + 93914.85504*Bool_(29,_1) + 133221.61985999998*Bool_(29,_2) + 90199.77828*Bool_(29,_3) + 51088.15911*Bool_(29,_4) + 219164.32191*Bool_(29,_5) + 17492.855685*Bool_(29,_6) + 150479.23446*Bool_(29,_7) + 49203.658410000004*Bool_(29,_8) + 249559.61211*Bool_(29,_9) + 54230.98745*Bool_(3,_0) + 49000.0*Bool_(3,_1) + 59203.04046*Bool_(3,_2) + 96566.03958*Bool_(3,_3) + 54120.236509999995*Bool_(3,_4) + 96176.92031*Bool_(3,_5) + 63158.5307*Bool_(3,_6) + 46615.44808*Bool_(3,_7) + 53141.32102*Bool_(3,_8) + 72917.7619*Bool_(3,_9) + 33634.060125*Bool_(4,_0) + 157341.189775*Bool_(4,_1) + 129059.095*Bool_(4,_2) + 266516.885*Bool_(4,_3) + 195400.2303*Bool_(4,_4) + 150208.18885*Bool_(4,_5) + 223732.541225*Bool_(4,_6) + 109914.73967499999*Bool_(4,_7) + 201308.22139999998*Bool_(4,_8) + 49812.147124999996*Bool_(4,_9) + 131576.97367500002*Bool_(5,_0) + 37583.24095*Bool_(5,_1) + 71501.748225*Bool_(5,_2) + 160195.193425*Bool_(5,_3) + 57008.77125*Bool_(5,_4) + 169059.90062499998*Bool_(5,_5) + 84852.81375*Bool_(5,_6) + 52559.4901*Bool_(5,_7) + 58363.08765*Bool_(5,_8) + 142521.928125*Bool_(5,_9) + 311306.92252*Bool_(6,_0) + 82462.11252000001*Bool_(6,_1) + 140000.0*Bool_(6,_2) + 146696.96656*Bool_(6,_3) + 25612.496948*Bool_(6,_4) + 268328.15728000004*Bool_(6,_5) + 24331.05012*Bool_(6,_6) + 158240.32356000002*Bool_(6,_7) + 28284.271248*Bool_(6,_8) + 293748.19148*Bool_(6,_9) + 114769.33388*Bool_(7,_0) + 38418.74542*Bool_(7,_1) + 16124.515496*Bool_(7,_2) + 95603.34722000001*Bool_(7,_3) + 59093.14682*Bool_(7,_4) + 74027.0221*Bool_(7,_5) + 74966.65926*Bool_(7,_6) + 43680.65934*Bool_(7,_7) + 66211.78142*Bool_(7,_8) + 89196.41248000001*Bool_(7,_9) + 51478.1507*Bool_(8,_0) + 5830.951895*Bool_(8,_1) + 15556.34919*Bool_(8,_2) + 56302.753039999996*Bool_(8,_3) + 20880.613019999997*Bool_(8,_4) + 54561.89146*Bool_(8,_5) + 32310.98884*Bool_(8,_6) + 13341.66406*Bool_(8,_7) + 23345.23506*Bool_(8,_8) + 49091.750830000004*Bool_(8,_9) + 38137.90765*Bool_(9,_0) + 17846.568300000003*Bool_(9,_1) + 14230.24947*Bool_(9,_2) + 17102.631375*Bool_(9,_3) + 19416.487839999998*Bool_(9,_4) + 17066.048165*Bool_(9,_5) + 20615.528130000002*Bool_(9,_6) + 21224.985275000003*Bool_(9,_7) + 21100.947845*Bool_(9,_8) + 29300.17065*Bool_(9,_9) + 0.0

### Constraints

A total of 4 testing sites will be opened:

	N0+N1+N2+N3+N4+N5+N6+N7+N8+N9 = 4
Each neighborhood will go to only one testing site:

	j00:N000+N100+N200+N300+N400+N500+N600+N700+N800+N900 = 1
	j01:N001+N101+N201+N301+N401+N501+N601+N701+N801+N901 = 1
	j02:N002+N102+N202+N302+N402+N502+N602+N702+N802+N902 = 1
	.
	.
	.
	j29:N029+N129+N229+N329+N429+N529+N629+N729+N829+N929 = 1
The capacity of the testing site will not exceed 25000

	2500 C(0,0) + 2000 C(1,0) + 2500 C(10,0) + 
	2000 C(11,0)+3000 C(12,0) + 5000 C(13,0) + 
	2500 C(14,0) + 2000 C(15,0)+1500 C(16,0) + 
	1000 C(17,0) + 1000 C(18,0) + 2000 C(19,0)+
	3000 C(2,0) + 3000 C(20,0) + 1500 C(21,0) + 
	2500 C(22,0)+3500 C(23,0) + 3000 C(24,0) + 
	2500 C(25,0) + 2000 C(26,0)+1500 C(27,0) + 
	1500 C(28,0) + 3000 C(29,0) + 1000 C(3,0)+
	2500 C(4,0) + 2500 C(5,0) + 4000 C(6,0) + 
	2000 C(7,0)+1000 C(8,0) + 500 C(9,0)
	- 25000*N0 <= 0
	.
	.
	.
	 (Total of 10 equations)
### Code
Importing packages
```python
import pulp #pulp will be used to produce the problem
import numpy as np
```
Problem information
```python
#The capacity of the testing site
capacity = [25000,25000,25000,25000,25000,25000,25000,25000,25000,25000] 
#The demand of the neighborhood
demand = [2500,2000,3000,1000,2500,2500,4000,2000,1000,500, 
          2500,2000,3000,5000,2500,2000,1500,1000,1000,2000,
          3000,1500,2500,3500,3000,2500,2000,1500,1500,3000]
Cij = #This is a 30*10 matrix
np.array([[93.50935782,43.68065934,44.04543109,14.14213562,39.11521443,53.15072906,
                 35.4682957,56.60388679,41.43669871, 78.23042886], [9.486832981,
                64.63745044, 58.25804665, 113.1459235, 78.89233169,75.95393341,
                90.55385138, 46.75467891, 80.5294977, 37.01351105],[96.9381246,
                45.88027899,47.42362281, 10.04987562, 40.01249805, 57.218878,
                35.17101079, 59.6405902, 42.04759208,82.15229759], [54.23098745,
                49.0, 59.20304046, 96.56603958, 54.12023651,
				96.17692031,63.1585307,
                46.61544808, 53.14132102, 72.9177619], [13.45362405, 62.93647591,
                51.623638, 106.606754,78.16009212, 60.08327554, 89.49301649,
                43.96589587, 80.52328856, 19.92485885], [52.63078947,15.03329638,
                28.60069929,64.07807737,22.8035085,
				67.62396025,33.9411255,21.02379604,
                23.34523506, 57.00877125], [77.82673063, 20.61552813, 35.0,
                36.67424164, 6.403124237,67.08203932, 6.08276253, 39.56008089,
                7.071067812, 73.43704787], [57.38466694, 19.20937271,8.062257748,
                47.80167361, 29.54657341, 37.01351105, 37.48332963, 21.84032967,
                33.10589071,44.59820624], [51.4781507, 5.830951895, 15.55634919,
                56.30275304, 20.88061302, 54.56189146,32.31098884, 13.34166406,
                23.34523506, 49.09175083], [76.2758153, 35.6931366, 28.46049894,
                34.20526275, 38.83297568, 34.13209633, 41.23105626, 42.44997055,
                42.20189569, 58.6003413],[61.3514466, 76.15773106, 58.30951895,
                97.01546269, 89.18520057, 30.08321791, 97.29337079,63.2455532,
                92.65527508, 34.0],
		        [75.60423269,20.59126028,27.85677655,30.52867504,
                15.8113883, 54.7813837, 17.49285568, 36.87817783, 18.78829423,
                66.48308055],[37.85498646, 38.27531842, 44.10215414, 89.0,
                48.01041554, 79.12016178, 58.89821729,30.41381265, 48.27007354,
                54.56189146], [40.22437072, 17.72004515, 13.03840481, 65.19202405,
                32.984845, 49.24428901, 44.27188724, 1.414213562, 35.51056181,
                37.33630941], [68.41052551,18.86796226, 36.7151195, 54.91812087,
                13.03840481, 74.51845409, 21.02379604, 34.23448554,11.18033989,
                70.71067812], [80.08120878, 27.65863337, 45.22167622,
                50.009999, 15.0,80.99382693, 15.13274595, 45.0, 11.40175425,
                81.22191822], [62.09669879, 15.62049935,32.80243893,
                58.24087911, 15.8113883, 71.42128534, 25.8069758,
                28.63564213, 15.26433752,65.11528238], [65.21502894,
                27.73084925, 17.4642492, 42.48529157, 34.82814953, 31.78049716,
                40.31128874, 31.57530681, 38.41874542, 48.87739764],
                [74.27651042, 23.34523506, 25.0,30.41381265, 22.82542442,
                47.4341649, 25.23885893, 36.40054945, 26.07680962, 62.39390996],
                [91.92388155, 39.92492956, 42.44997055, 13.03840481,
                34.0, 56.00892786, 29.73213749,54.20332093, 36.12478374,
                78.29431652], [51.2445119, 23.02172887, 35.35533906, 71.51223672,
                29.52964612, 74.06078585, 40.0, 25.49509757, 29.41088234,
                59.61543424], [32.80243893,53.66563146, 56.56854249,
                104.7091209, 64.20280368, 87.66413178, 75.16648189,
                42.42640687, 64.5368112, 56.60388679], [67.08203932,
                72.71863585, 54.91812087,88.20430828, 84.58132182, 21.0,
                91.70605214, 62.22539674, 88.141931, 38.83297568],
                [50.11985634, 30.52867504, 12.80624847, 59.05929224,
                43.01162634, 26.62705391,51.4781507, 23.40939982,
                46.4865572, 32.24903099], [59.09314681, 5.656854249,
                23.32380758, 52.80151513, 13.03840481, 61.55485359,
                24.69817807, 22.09072203,14.86606875, 58.13776741],
                [57.14017851, 25.0, 39.40812099, 70.60453243, 28.16025568,
                78.40918314, 37.58989226, 30.8058436, 27.31300057,
                65.55150647], [22.09072203,72.13875519, 68.26419266,
                122.1474519, 85.42833254, 88.68483523, 97.0051545, 55.6057551,
                86.60831369, 50.03998401], [80.36168241, 57.70615219,
                73.00684899, 95.00526301,55.31726674, 112.0044642,
                60.03332408, 63.63961031, 52.77309921, 95.7183368],
                [12.04159458, 45.61797891, 37.53664876, 92.65527508,
                60.53924347, 58.0, 72.09022125,26.92582404, 62.62587325,
                23.85372088], [88.58893836, 31.30495168, 44.40720662,
                30.06659276, 17.02938637, 73.05477397, 5.830951895,
                50.15974482, 16.40121947, 83.18653737]])
```
Creating the model & variables
```python
#create the model
model = pulp.LpProblem("part1",pulp.LpMinimize)
#set Cij,which is whether the j neighborhood will go to the i site
Boo = pulp.LpVariable.dicts("Bool",((i, j) for i in range(30) for j in range(10)),
						  lowBound=0,cat='Binary')
#set N, which is whether the i site will be open
N = pulp.LpVariable.dicts("N",((i) for i in range(10)),cat='Binary')
```
Create the constraints
```python
#each neighborhood will only go to one testing site
for i in range(30):
    model += pulp.lpSum([C[i,j] for j in range(10)]) == 1
#the capacity will not be exceeded
for j in range(10):
    model += pulp.lpSum([demand[i]*C[i,j]  for i in range(30)]) <= N[j]*capacity[j]
#Only 4 testing sites will open
model += pulp.lpSum([N[i] for i in range(10)]) == 4
```
Create the optimization objective
```python
#Minimize the sum of the distances
model += pulp.lpSum([Boo[i,j]*Cij[i,j]*demand[i] for i in range(30) 
					 for j in range(10)])
```
Solve and print the solution
```python
model.solve()
#create the solution matrix,where X is the C matrix and Y the N matrix
X = np.zeros(30*10)
Y = np.zeros(10)
i = 0
#assign the variables to the matrix
for variable in model.variables():
    if i<300:
        X[i]= variable.varValue
    else:
        Y[i-300] = variable.varValue
    i += 1
X = np.reshape(X,(30,10))
print(model)
print('C =\n',X)
print('N =', Y)
print('Optimal objective value:',pulp.value(model.objective))
```
### The solution
	N = [1. 0. 0. 1. 0. 0. 0. 1. 1. 0.]
	Optimal objective value: 1433017.5506299995
The testing sites that should be opened is testing site 1,4,8,9. 
The minimum cost is **1433017.5506299995**
## Part 2. Providing testing materials (transportation problem)
### Decision variables & Parameters
	*i is equivalant to the suppliers of range(6)
	*j is equivalant to the testing sites of range(4) 
	*Rij, equals to 1 if the route between i.th supplier and j.th site is open
	*Costij is the cost for the route
### Objective
Minimize the total cost
>$\sum$(Costij*Rij)

	42000*Route_(0,_0) + 31500*Route_(0,_1) + 46000*Route_(0,_2) + 20000*Route_(0,_3) + 42000*Route_(1,_0) + 21000*Route_(1,_1) + 69000*Route_(1,_2) + 60000*Route_(1,_3) + 42000*Route_(2,_0) + 52500*Route_(2,_1) + 138000*Route_(2,_2) + 60000*Route_(2,_3) + 84000*Route_(3,_0) + 21000*Route_(3,_1) + 138000*Route_(3,_2) + 120000*Route_(3,_3) + 56000*Route_(4,_0) + 21000*Route_(4,_1) + 69000*Route_(4,_2) + 60000*Route_(4,_3) + 56000*Route_(5,_0) + 21000*Route_(5,_1) + 138000*Route_(5,_2) + 120000*Route_(5,_3) + 0
###  Constraints
Each testing site must be linked to 1 and only 1 supplier

	Route_(0,_0)+Route_(1,_0)+Route_(2,_0)+Route_(3,_0)+Route_(4,_0)+ Route_(5,_0) = 1
	.
	.
	.
	
 
The total number of suppliers supplying must be equal to 4.
(It is assumed that 1 supplier can supply to only one testing site)

	Route_(0,_0)+Route_(0,_1)+Route_(0,_2)+Route_(0,_3)+Route_(1,_0)+ Route_(1,_1)+ 
	Route_(1,_2)+Route_(1,_3)+Route_(2,_0)+Route_(2,_1)+Route_(2,_2)+ Route_(2,_3)+ 
	Route_(3,_0)+Route_(3,_1)+Route_(3,_2)+Route_(3,_3)+Route_(4,_0)+ Route_(4,_1)+ 
	Route_(4,_2)+Route_(4,_3)+Route_(5,_0)+Route_(5,_1)+Route_(5,_2)+ Route_(5,_3) = 4
### Code 
Importing packages
```python
import pulp #pulp will be used to produce the problem
import numpy as np
```
Problem information
```python
#The supplier is the row and the site is the column
cost = np.array([[3,3,2,1],
                 [3,2,3,3],
                 [3,5,6,3],
                 [6,2,6,6],
                 [4,2,3,3],
                 [4,2,6,6]])
pop = np.array([14000,10500,23000,20000])
```
Creating the model & variables
```python
#create the model
model = pulp.LpProblem("part2",pulp.LpMinimize)
#set the Rij boolean variable
C = pulp.LpVariable.dicts("Cost",((i, j) for i in range(6) for j in range(4)),
						  lowBound=0,cat='Binary')
```
Create the constraints
```python
#Each testing site must be linked to 1 and only 1 supplier
for j in range(4):
    model += pulp.lpSum([R[i,j] for i in range(6)]) == 1
#The total number of suppliers must be equal to or less then 4
    model += pulp.lpSum([R[i,j] for i in range(6) for j in range(4)]) == 4
```
Create the optimization objective
```python
#Minimize the sum of the costs
model += pulp.lpSum([cost[i,j]*R[i,j]*pop[j] for i in range(6) 
					 for j in range(4)])
```
Solve and print the solution
```python
model.solve()
#create the solution matrix,where X is the R matrix and Y the suppliers matrix
X = np.zeros(6*4)
i = 0
#assign the variables to the matrix
for variable in model.variables():
    if i<24:
        X[i]= variable.varValue
    i += 1
X = np.reshape(X,(6,4))
print(model)
print('R =\n',X)
print('Minimum cost:',pulp.value(model.objective))
```
### The solution
	R = [[0. 0. 1. 1.]
	     [0. 0. 0. 0.]
	     [1. 0. 0. 0.]
	     [0. 0. 0. 0.]
	     [0. 0. 0. 0.]
	     [0. 1. 0. 0.]]
	Minimum cost: 129000.0
Testing site 1 will be supplied by supplier 3
Testing site 4 will be supplied by supplier 6
Testing site 8 will be supplied by supplier 1
Testing site 9 will be supplied by supplier 1
The minimum cost is 129000.0
## Part 3. Picking up all the tests (traveling salesperson problem)
### Decision variables & Parameters
	*i(j) is the equivalent of the testing site and the lab
		1 to 4 for the testing site, 5 for the lab
	*Cij stands for the cost between i and j
	*Xij is 1 if the route is taken in the tour
### Objective
Minimize the total cost

>$\sum$(Cij*Xij)

	104.69002*X_(0,_1) + 38.832976*X_(0,_2) + 73.925638*X_(0,_3) + 38.209946*X_(0,_4) + 104.6900186*X_(1,_0) + 66.60330322*X_(1,_2) + 43.737855*X_(1,_3) + 66.483081*X_(1,_4) + 38.83297568*X_(2,_0) + 66.603303*X_(2,_1) + 36.674242*X_(2,_3) + 5.6568542*X_(2,_4) + 73.92563831*X_(3,_0) + 43.73785546*X_(3,_1) + 36.67424164*X_(3,_2) + 40.112342*X_(3,_4) + 38.209946*X_(4,_0) + 66.483081*X_(4,_1) + 5.656854249*X_(4,_2) + 40.11234224*X_(4,_3) + 0.0
###  Constraints
All the Inbound constraint for the nodes
	
	Testing site 1:
	X21+X31+X41+X51 = 1
	.
	.
	.
	Lab 1 (node 5)
	X15+X25+X35+X45 = 1
	
All the Outbound constraint for the nodes

	Testing site 1:
	X12+X13+X14+X16 = 1
	.
	.
	.
	Lab 1 (node 5)
	X51 + X52 + X53 +X54 = 1
Subtour constraints  (2 nodes)  

	X12 + X21 <= 1
	.
	.
	.
Subtour constraints  (3 nodes) 

	X12 + X23 + X31 <= 2
	.
	.
	.
Subtour constraints  (4 nodes) 

	X12 + X23 + X34 + X41 <= 3
	.
	.
	.

### Code
Importing packages
```python
import pulp #pulp will be used to produce the problem
import numpy as np
```
Problem information
```python
#i is the row and j is the column
c = np.array([[0,104.69002,38.832976,73.925638,38.209946],
              [104.6900186,0,66.60330322,43.737855,66.483081],
              [38.83297568,66.603303,0,36.674242,5.6568542],
              [73.92563831,43.73785546,36.67424164,0,40.112342],
              [38.209946,66.483081,5.656854249,40.11234224,0]])
```
Creating the model & variables
```python
#create the model
model = pulp.LpProblem("part3",pulp.LpMinimize)
#set the Xij boolean variables 
x = pulp.LpVariable.dicts("X",((i, j) for i in range(5) for j in range(5)),
						  lowBound=0,cat='Binary')
```
Create the constraints
```python
#the inbound/outbound constraint 
for i in range(5):
    model += pulp.lpSum([x[i,j] for j in range(5) if i != j]) == 1
for i in range(5):
    model += pulp.lpSum([x[i,i]]) == 0
#subtours (2 nodes)
for i in range(5):
    for j in range(5):
        if i != j:
            model += pulp.lpSum([x[i,j]+x[j,i]]) <= 1
#subtours (3 nodes)
for i in range(5):
    for j in range(5):
        for k in range(5):
            if (i != j and i!=k and j != k):
                model += pulp.lpSum([x[i,j]+x[j,k]+x[k,i]]) <= 2
#subtours (4 nodes)
for i in range(5):
        for k in range(5):
            for l in range(5):
                if (i != j and i!=k and i != l and
                    j != k and j != l and k != l):
                    model += pulp.lpSum([x[i,j]+x[j,k]+x[k,l]+x[l,i]]) <= 3
```
Create the optimization objective
```python
#all the cost times x is the minimum
model += pulp.lpSum([c[i,j]*x[i,j] for i in range(5) 
					 for j in range(5) if i!=j])
```
Solve and print the solution
```python
model.solve()
#create the solution matrix,where X is the R matrix and Y the suppliers matrix
X = np.zeros(5*5)
i = 0
#assign the variables to the matrix
for variable in model.variables():
    if i<25:
        X[i]= variable.varValue
    i += 1
X = np.reshape(X,(5,5))
print(model)
print('X =\n',X)
print('Minimum cost:',pulp.value(model.objective))
```
### The solution 
	X =[[0. 0. 1. 0. 0.]
    	[0. 0. 0. 0. 1.]
	    [0. 0. 0. 1. 0.]
    	[0. 1. 0. 0. 0.]
    	[1. 0. 0. 0. 0.]]
		Minimum cost: 223.93810046
The route is
>X51 + X13 + X34 +X42 + X25

Where 1,2,3,4 is testing site 1,4,8,9 and 5 is the lab

>Lab -> Site 1 -> Site 8 -> Site 9 -> Site 4 -> Lab



## Misc
### Importing excel sheet data to a array(part 1)
```python
import xlrd
with xlrd.open_workbook('data.xlsx') as data:
    sheet = data.sheet_by_index(0)
    rows = []
    for row in sheet.get_rows():
        rows.append([cell.value for cell in row])
print(rows)
```